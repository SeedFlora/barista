"""Buat ulang diagram kerangka pemikiran Bab 2 dari rancangan naskah.

Jalankan dari folder skripsi: python tools/kerangka_pemikiran.py
Diagram ini konseptual; tidak memuat hasil evaluasi.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


OUTPUT = Path(__file__).resolve().parents[1] / "pic" / "kerangka_pemikiran.png"
INK = "#252525"
ACCENT = "#345e73"
BORDER = "#69757a"
FILL = "#f5f7f7"


def box(ax, x, y, w, h, label, fontsize=9.2):
    ax.add_patch(
        FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.004,rounding_size=0.009",
            facecolor="white", edgecolor=BORDER, linewidth=0.8,
        )
    )
    ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
            fontsize=fontsize, color=INK, linespacing=1.25)


def band(ax, y, h, title):
    ax.add_patch(
        FancyBboxPatch(
            (0.025, y), 0.95, h,
            boxstyle="round,pad=0.005,rounding_size=0.013",
            facecolor=FILL, edgecolor=BORDER, linewidth=1.0,
        )
    )
    ax.text(0.045, y + h - 0.027, title, ha="left", va="center",
            fontsize=11, fontweight="bold", color=ACCENT)


def row(ax, labels, y, h, *, x0=0.045, x1=0.955, gap=0.012, fontsize=9.2):
    width = (x1 - x0 - (len(labels) - 1) * gap) / len(labels)
    for index, label in enumerate(labels):
        box(ax, x0 + index * (width + gap), y, width, h, label, fontsize)


def arrow(ax, start, end):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=13,
                                 linewidth=1.2, color=ACCENT))


def main():
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Segoe UI", "DejaVu Sans", "Arial"],
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    })
    fig, ax = plt.subplots(figsize=(7.1, 9.2), dpi=300)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")

    band(ax, 0.824, 0.160, "1  Masalah, kebutuhan, dan peluang")
    row(ax, [
        "P1  Takaran tidak\nkonsisten antargilir",
        "P2  Pelatihan\nbarista baru lama",
        "P3  Stok bahan\nbelum terintegrasi",
        "P4  Variasi pesanan\ndihitung manual",
        "O1  Data transaksi\ndapat dimanfaatkan",
    ], 0.846, 0.090, fontsize=8.55)
    arrow(ax, (0.5, 0.818), (0.5, 0.796))

    band(ax, 0.565, 0.225, "2  Solusi dalam aplikasi web Takar")
    row(ax, [
        "S1  Resep standar\ndan SOP digital",
        "S2  Panduan seduh\ndan daftar periksa",
        "S3  Buku besar stok\nberbasis produksi",
    ], 0.670, 0.070, fontsize=9.1)
    row(ax, [
        "S4  Kalkulator takaran\nberbasis batasan",
        "S5  Pasangan menu,\nrestock, koreksi seduh",
        "S6  Asisten lokal:\nRAG dan alat aplikasi",
    ], 0.584, 0.070, fontsize=9.1)
    arrow(ax, (0.5, 0.558), (0.5, 0.536))

    band(ax, 0.401, 0.129, "3  Metode pembangunan")
    row(ax, [
        "Agile/Scrum\nuntuk S1--S6",
        "Penskalaan\nberbasis batasan",
        "FP-Growth, ramalan,\nsistem pakar",
        "BM25, Gemma 4,\nrouting alat",
    ], 0.422, 0.064, fontsize=8.85)
    arrow(ax, (0.5, 0.394), (0.5, 0.372))

    band(ax, 0.215, 0.151, "4  Evaluasi")
    row(ax, [
        "Uji fungsional\ndan kinerja web",
        "Grid, data nyata,\nsimulasi (H1--H4)",
        "Tolok ukur tanya-\njawab 60 butir (H5)",
        "UAT dan SUS\n(direncanakan)",
    ], 0.239, 0.078, fontsize=8.8)
    arrow(ax, (0.5, 0.208), (0.5, 0.186))

    band(ax, 0.021, 0.159, "5  Keluaran untuk rumusan masalah")
    row(ax, [
        "RM1  Resep, SOP,\nstok terintegrasi",
        "RM2  Variasi sesuai\nbatasan praktis",
        "RM3  Kinerja AI\ndan asisten terukur",
        "RM4  Fungsi, kinerja;\nUAT masih diperlukan",
    ], 0.046, 0.082, fontsize=8.7)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=300)
    plt.close(fig)
    print(OUTPUT)


if __name__ == "__main__":
    main()
