#!/bin/sh
set -eu

# Sumber tetap tersedia di /work; hanya folder output yang di-mount ke host.
mkdir -p /work/build /output
if ! latexmk -pdf -halt-on-error -file-line-error -interaction=nonstopmode Skripsi.tex > /work/build/compile-docker.log 2>&1; then
    cat /work/build/compile-docker.log
    exit 1
fi
cp /work/build/Skripsi.pdf /output/Skripsi.pdf
cp /work/build/compile-docker.log /output/compile-docker.log
pdfinfo /output/Skripsi.pdf
