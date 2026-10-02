"""Render diagram PlantUML skripsi (pic/uml/*.puml -> pic/*.png, 300 dpi).

Pemakaian (dari folder mana pun):
    python D:\\barista\\skripsi\\pic\\uml\\render.py              # semua diagram skripsi
    python D:\\barista\\skripsi\\pic\\uml\\render.py erd use_case  # hanya diagram tertentu
    python D:\\barista\\skripsi\\pic\\uml\\render.py --paper       # versi bahasa Inggris untuk makalah

Diagram memakai layout Smetana (!pragma layout smetana di _style.iuml) sehingga tidak memerlukan Graphviz.
PLANTUML_LIMIT_SIZE dinaikkan agar gambar 300 dpi yang lebar tidak terpotong.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PIC = HERE.parent
JAR = Path(r"D:\barista\tools\plantuml.jar")
PAPER_SRC = Path(r"D:\barista\paper\figs\uml")
PAPER_OUT = PAPER_SRC.parent


def render(sources: list[Path], out_dir: Path) -> None:
    cmd = ["java", "-DPLANTUML_LIMIT_SIZE=16384", "-Djava.awt.headless=true", "-jar", str(JAR),
           "--format", "png", "--charset", "UTF-8", "--stop-on-error", "--output-dir", str(out_dir),
           *map(str, sources)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout, result.stderr, sep="\n")
        raise SystemExit(result.returncode)
    try:
        from PIL import Image, PngImagePlugin
    except ImportError:  # Pillow optional: sets the 300 dpi tag (pHYs) and reports sizes
        return
    for src in sources:
        png = out_dir / f"{src.stem}.png"
        with Image.open(png) as img:
            img.load()
            meta = PngImagePlugin.PngInfo()
            for key, value in getattr(img, "text", {}).items():  # keep the embedded PlantUML source
                meta.add_itxt(key, value)
            img.save(png, dpi=(300, 300), pnginfo=meta, optimize=True)
        with Image.open(png) as img:
            print(f"{png.name}: {img.width} x {img.height} px, dpi={img.info.get('dpi')}, "
                  f"{img.width / 300 * 2.54:.1f} x {img.height / 300 * 2.54:.1f} cm @300 dpi")


def main(argv: list[str]) -> None:
    if "--paper" in argv:
        names = [a for a in argv if a != "--paper"]
        sources = [p for p in sorted(PAPER_SRC.glob("*.puml")) if not names or p.stem in names]
        render(sources, PAPER_OUT)
        return
    sources = [p for p in sorted(HERE.glob("*.puml")) if not argv or p.stem in argv]
    render(sources, PIC)


if __name__ == "__main__":
    main(sys.argv[1:])
