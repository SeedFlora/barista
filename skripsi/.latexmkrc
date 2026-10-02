$out_dir = 'build';
$pdf_mode = 1;
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 %O %S';
$bibtex_use = 2;
# BibTeX runs inside build/; let it find ref.bib in the project folder (MiKTeX and TeX Live).
ensure_path('BIBINPUTS', '..');
