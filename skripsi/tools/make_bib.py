"""Generate ref.bib from referensi_terverifikasi.json (verified via Crossref/arXiv/dblp).

Run from the skripsi folder:  python tools/make_bib.py
Only metadata from the verified JSON is used; nothing is invented here.
"""
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "referensi_terverifikasi.json"
TARGET = ROOT / "ref.bib"

# Proper nouns / names that APA sentence case must keep capitalised.
PROPER = {
    # people, places and named methods
    "Wilcoxon", "Friedman", "Holm", "Holt", "Winters", "Holt-Winters", "Poisson", "Gaussian", "Bayesian", "Markov",
    "Apriori", "Monte", "Carlo", "Indonesia", "Indonesian", "Bandung", "Jakarta", "Java", "Sumatra", "Aceh",
    "Gayo", "Toraja", "Flores", "Bali", "Sulawesi", "Ethiopia", "Ethiopian", "Honduras", "Brazil", "Colombia",
    "Edinburgh", "Ukraine", "Asia", "Europe", "Davis", "California", "Starbucks", "Arabica", "Robusta",
    "Bread", "Basket",  # dataset title "The Bread Basket" (name of the Edinburgh bakery)
    # software, standards and organisations
    "Python", "JavaScript", "TypeScript", "Laravel", "Django", "Flask", "Angular", "React", "Svelte", "Blazor",
    "Vue", "Android", "Windows", "Linux", "Excel", "Google", "Lighthouse", "Kaggle", "Scrum", "Agile",
    "Web", "Internet", "Things", "COVID-19", "Covid-19",
}
LATEX_ESCAPES = {"&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_", "$": r"\$"}


def escape(text):
    return "".join(LATEX_ESCAPES.get(ch, ch) for ch in str(text))


def protect_title(title):
    words = []
    for word in re.split(r"(\s+)", escape(title)):
        core = re.sub(r"[^\w\-]", "", word)
        needs = (
            sum(ch.isupper() for ch in core) >= 2
            or any(ch.isdigit() for ch in core)
            or core in PROPER
            or core.rstrip("s") in PROPER
        )
        words.append("{" + word + "}" if needs and word.strip() else word)
    return "".join(words)


# BibTeX abbreviates given names byte by byte, so a given name that starts with a multi-byte UTF-8
# letter ("Édouard", "Önder") is cut to its first byte and the .bbl becomes invalid UTF-8
# ("Invalid UTF-8 byte sequence" in pdflatex). Such initials are written as BibTeX special
# characters ({\'E}douard), which BibTeX keeps whole when it abbreviates ({\'E}.).
TEX_ACCENTS = {"̀": "`", "́": "'", "̂": "^", "̃": "~", "̄": "=", "̆": "u",
               "̇": ".", "̈": '"', "̊": "r", "̋": "H", "̌": "v", "̧": "c",
               "̨": "k"}
TEX_LETTERS = {"Ł": r"\L", "ł": r"\l", "Ø": r"\O", "ø": r"\o", "Æ": r"\AE", "æ": r"\ae", "Œ": r"\OE",
               "œ": r"\oe", "Å": r"\AA", "å": r"\aa"}


def tex_initial(ch):
    if ord(ch) < 128:
        return ch
    if ch in TEX_LETTERS:
        return "{" + TEX_LETTERS[ch] + "}"
    decomposed = unicodedata.normalize("NFD", ch)
    if len(decomposed) == 2 and ord(decomposed[0]) < 128 and decomposed[1] in TEX_ACCENTS:
        accent = TEX_ACCENTS[decomposed[1]]
        separator = " " if accent.isalpha() else ""
        return "{\\" + accent + separator + decomposed[0] + "}"
    raise SystemExit(f"no BibTeX-safe form for initial {ch!r}; add it to TEX_LETTERS")


def person(name):
    last, given = escape(name).split(",", 1)
    given = re.sub(r"(^|[\s\-])([^\x00-\x7f])", lambda m: m.group(1) + tex_initial(m.group(2)), given)
    return last + "," + given


def authors(names):
    # Verified person names are "Last, First"; anything without a comma is an
    # institution and is braced so BibTeX does not split it into name parts.
    formatted = []
    for name in (n.strip() for n in names):
        formatted.append(person(name) if "," in name else "{" + escape(name.strip("{}")) + "}")
    return " and ".join(formatted)


def entry(ref):
    kind = ref["entry_type"]
    venue = ref.get("venue", "")
    fields = {"author": authors(ref["authors"]), "title": protect_title(ref["title"]), "year": str(ref["year"])}
    if kind == "article":
        fields["journal"] = escape(venue)
    elif kind in ("inproceedings", "incollection"):
        # Proceedings titles keep their capitalisation (apacite would sentence-case them).
        fields["booktitle"] = "{" + escape(venue) + "}"
    elif kind == "book":
        fields["publisher"] = escape(ref.get("publisher") or venue)
    elif kind == "phdthesis":
        fields["school"] = escape(ref.get("publisher") or venue)
    elif kind == "techreport":
        fields["institution"] = escape(ref.get("publisher") or venue)
    else:  # misc, standard, documentation, preprint
        kind = "misc"
        fields["howpublished"] = escape(venue)
    for key in ("volume", "number", "pages"):
        if kind == "misc" and key == "number":
            continue  # standards/documentation carry their number in howpublished
        if ref.get(key):
            fields[key] = escape(ref[key]).replace("-", "--") if key == "pages" else escape(ref[key])
    if ref.get("publisher") and kind in ("inproceedings", "incollection", "article") and kind != "article":
        fields["publisher"] = escape(ref["publisher"])
    if ref.get("doi"):
        fields["doi"] = ref["doi"].lower().replace("https://doi.org/", "")
    elif ref.get("url"):
        fields["url"] = ref["url"]
    if kind == "misc" and ref.get("url"):
        fields["url"] = ref["url"]
        fields["lastchecked"] = "30 September 2026"  # rendered "Diakses <tanggal>, dari <URL>"
    body = ",\n".join(f"  {k:<12} = {{{v}}}" for k, v in fields.items())
    return f"@{kind}{{{ref['key']},\n{body}\n}}\n"


def main():
    refs = json.loads(SOURCE.read_text(encoding="utf-8"))
    keys = [r["key"] for r in refs]
    duplicates = {k for k in keys if keys.count(k) > 1}
    if duplicates:
        raise SystemExit(f"duplicate keys: {sorted(duplicates)}")
    header = ("% ref.bib -- dibuat otomatis oleh tools/make_bib.py dari referensi_terverifikasi.json\n"
              "% Setiap entri diverifikasi terhadap Crossref / arXiv / dblp / halaman penerbit (30 September 2026).\n"
              f"% {len(refs)} entri; {sum(r['year'] >= 2021 for r in refs)} terbit 2021-2026. Hanya entri yang disitasi muncul di daftar referensi.\n\n")
    TARGET.write_text(header + "\n".join(entry(r) for r in sorted(refs, key=lambda r: r["key"])), encoding="utf-8")
    print(f"wrote {TARGET} with {len(refs)} entries")


if __name__ == "__main__":
    main()
