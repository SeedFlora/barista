"""Gambar konseptual Bab 2 (PNG 300 dpi di pic/), digambar penulis dari sumber yang disitasi di bab2.tex.

Jalankan dari folder skripsi:  D:\\barista\\app\\backend\\.venv\\Scripts\\python.exe tools/gambar_bab2.py

1. pic/bagan_kendali_seduh.png  - bagan kendali seduh: kotak Golden Cup (SCAA, 2015: TDS 1,15-1,35 %,
   EY 18-22 %), batas atas kekuatan SCA 310-2021 (1,55 %), sembilan zona, dan garis rasio seduh tetap dari
   neraca massa Guinard dkk. (2023): PE = TDS/(1 - TDS) (R - R_abs), R_abs = 2,1  ->  TDS = PE / (PE + R - R_abs).
   R = 15 adalah resep V60 arahan (15 g : 225 ml); R = 16,5 dan 20,2 adalah batas rasio Golden Cup
   55 g/L +/- 10 % (1000/60,5 dan 1000/49,5; perhitungan penulis, 1 ml air dianggap 1 g).
2. pic/rolling_origin.png - skema evaluasi rolling origin (titik asal bergeser mingguan, horizon 7 hari).
Tidak ada angka hasil penelitian pada kedua gambar.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Patch, Rectangle  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402
import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
PIC = ROOT / "pic"
BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
INK, INK2, MUTED, GRID, BASE = "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
R_ABS = 2.1


def koma(fmt):
    return FuncFormatter(lambda v, _: (fmt % v).replace(".", ","))


def gaya():
    plt.rcParams.update({
        "figure.facecolor": "#ffffff", "axes.facecolor": "#ffffff", "axes.edgecolor": BASE,
        "axes.linewidth": 0.8, "axes.labelcolor": INK2, "axes.labelsize": 9,
        "axes.spines.top": False, "axes.spines.right": False,
        "xtick.color": MUTED, "ytick.color": MUTED, "xtick.labelcolor": INK2, "ytick.labelcolor": INK2,
        "xtick.labelsize": 8, "ytick.labelsize": 8, "legend.frameon": False, "legend.fontsize": 8,
        "font.family": "sans-serif", "font.sans-serif": ["Segoe UI", "DejaVu Sans", "Arial"],
        "savefig.dpi": 300, "savefig.bbox": "tight",
    })


def tds_dari_pe(pe, rasio):
    """TDS (fraksi) pada rendemen pe (fraksi) untuk rasio seduh air/kopi tertentu (neraca massa)."""
    k = rasio - R_ABS
    return pe / (pe + k)


def bagan_kendali():
    fig, ax = plt.subplots(figsize=(6.3, 4.6))
    x0, x1, y0, y1 = 14.0, 26.0, 0.80, 2.00
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
    # Sembilan zona: batas Golden Cup pada kedua sumbu.
    for x in (18, 22):
        ax.axvline(x, color=BASE, lw=0.8, zorder=1)
    for y in (1.15, 1.35):
        ax.axhline(y, color=BASE, lw=0.8, zorder=1)
    ax.add_patch(Rectangle((18, 1.15), 4, 0.20, facecolor="#dbeee4", edgecolor=AQUA, lw=1.4, zorder=2))
    ax.text(20, 1.25, "Golden Cup\n(ideal)", ha="center", va="center", fontsize=8.5, color=INK, zorder=6)
    # Batas atas kekuatan SCA 310-2021.
    ax.axhline(1.55, color=YELLOW, lw=1.2, ls=(0, (5, 3)), zorder=3)
    ax.text(14.15, 1.565, "batas atas kekuatan SCA 310-2021 (1,55%)", fontsize=7, color=INK2,
            va="bottom", zorder=6)
    # Garis rasio seduh tetap.
    pe = np.linspace(x0, x1, 200) / 100
    garis = [(15.0, "R = 15 (V60 arahan, 1:15)", ORANGE, "-", 2.0),
             (1000 / 60.5, "R = 16,5 (batas Golden Cup, 60,5 g/L)", BLUE, (0, (2, 2)), 1.3),
             (1000 / 49.5, "R = 20,2 (batas Golden Cup, 49,5 g/L)", BLUE, (0, (2, 2)), 1.3)]
    for rasio, label, warna, gaya_garis, tebal in garis:
        ax.plot(pe * 100, tds_dari_pe(pe, rasio) * 100, color=warna, ls=gaya_garis, lw=tebal, zorder=4,
                label=label)
    # Nama zona di luar bidang gambar: kolom (rendemen) di atas, baris (kekuatan) di kanan.
    for xk, teks in ((16, "kurang terekstraksi"), (20, "ideal"), (24, "terlalu terekstraksi")):
        ax.text(xk, 1.015, teks, transform=ax.get_xaxis_transform(), ha="center", va="bottom",
                fontsize=7.5, color=INK2)
    for yb, teks in ((0.975, "encer"), (1.25, "ideal"), (1.675, "pekat")):
        ax.text(1.015, yb, teks, transform=ax.get_yaxis_transform(), ha="left", va="center",
                fontsize=7.5, color=INK2, rotation=90)
    ax.set_xlabel("Rendemen ekstraksi, EY (%)")
    ax.set_ylabel("Kekuatan seduhan, TDS (%)")
    ax.xaxis.set_major_formatter(koma("%.0f"))
    ax.yaxis.set_major_formatter(koma("%.2f"))
    ax.set_yticks([0.8, 1.0, 1.15, 1.35, 1.55, 1.8, 2.0])
    ax.set_xticks([14, 16, 18, 20, 22, 24, 26])
    ax.legend(loc="lower right", handlelength=2.6, borderaxespad=0.3)
    fig.savefig(PIC / "bagan_kendali_seduh.png")
    plt.close(fig)


def rolling_origin():
    fig, ax = plt.subplots(figsize=(6.3, 2.9))
    n_awal, h, langkah, k = 56, 7, 7, 4
    for i in range(k):
        asal = n_awal + i * langkah
        y = k - i
        ax.barh(y, asal, left=0, height=0.55, color="#cde2fb", edgecolor=BLUE, lw=0.8)
        ax.barh(y, h, left=asal, height=0.55, color=ORANGE, edgecolor=ORANGE, lw=0.8)
        ax.plot([asal, asal], [y - 0.42, y + 0.42], color=INK, lw=1.0)
        ax.text(asal + h + 1.2, y, f"titik asal {i + 1}", va="center", fontsize=7.5, color=INK2)
    ax.text(n_awal + k * langkah + 2, 0.35, "...", fontsize=11, color=INK2)
    ax.set_ylim(0, k + 0.8)
    ax.set_xlim(0, n_awal + k * langkah + 22)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("Waktu (hari)")
    tanda = [Patch(facecolor="#cde2fb", edgecolor=BLUE, label="data latih hingga titik asal (model dilatih ulang)"),
             Patch(facecolor=ORANGE, edgecolor=ORANGE, label="data uji: horizon h = 7 hari setelah titik asal")]
    ax.legend(handles=tanda, loc="upper left", bbox_to_anchor=(0.0, 1.18), ncol=1)
    ax.grid(False)
    fig.savefig(PIC / "rolling_origin.png")
    plt.close(fig)


if __name__ == "__main__":
    gaya()
    bagan_kendali()
    rolling_origin()
    for nama in ("bagan_kendali_seduh.png", "rolling_origin.png"):
        print(PIC / nama, (PIC / nama).stat().st_size, "bytes")
