param([switch]$Docker)

$ErrorActionPreference = 'Stop'
$sourceDir = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$outputDir = Join-Path $sourceDir 'build'
New-Item -ItemType Directory -Path $outputDir -Force | Out-Null

if ($Docker) {
    & docker build --tag barista-skripsi $sourceDir
    if ($LASTEXITCODE -ne 0) { throw 'Build image Docker gagal.' }
    & docker run --rm --mount "type=bind,source=$outputDir,target=/output" barista-skripsi
    if ($LASTEXITCODE -ne 0) { throw 'Kompilasi skripsi di Docker gagal.' }
    return
}

foreach ($command in @('pdflatex', 'bibtex')) {
    if (-not (Get-Command $command -ErrorAction SilentlyContinue)) {
        throw "$command belum tersedia. Pasang MiKTeX/TeX Live atau jalankan dengan -Docker."
    }
}

$previousBibInputs = $env:BIBINPUTS
$logPath = Join-Path $outputDir 'compile-native.log'

function Invoke-TeXCommand {
    param([string]$Tool, [string[]]$ToolArguments, [string]$Log, [switch]$AppendOutput)
    # MiKTeX mengirim pengingat pembaruan ke stderr meski kompilasi berhasil.
    # Nilai exit process menentukan kegagalan; stderr tetap tersimpan di log.
    $ErrorActionPreference = 'Continue'
    & $Tool @ToolArguments 2>&1 | ForEach-Object { $_.ToString() } |
        Out-File -LiteralPath $Log -Append:$AppendOutput -Encoding utf8
    if ($LASTEXITCODE -ne 0) { throw "$Tool gagal. Baca $Log" }
}

Push-Location $sourceDir
try {
    $latexArguments = @('-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-output-directory=build', 'Skripsi.tex')
    Invoke-TeXCommand -Tool pdflatex -ToolArguments $latexArguments -Log $logPath

    # BibTeX dijalankan dari build; direktori sumber berisi ref.bib.
    $env:BIBINPUTS = $sourceDir + [IO.Path]::PathSeparator + $previousBibInputs
    Push-Location $outputDir
    try {
        Invoke-TeXCommand -Tool bibtex -ToolArguments @('Skripsi') -Log (Join-Path $outputDir 'bibtex-native.log')
    } finally { Pop-Location }

    foreach ($pass in 2..3) {
        Invoke-TeXCommand -Tool pdflatex -ToolArguments $latexArguments -Log $logPath -AppendOutput
    }
    Write-Host "Selesai: $outputDir/Skripsi.pdf"
} finally {
    $env:BIBINPUTS = $previousBibInputs
    Pop-Location
}
