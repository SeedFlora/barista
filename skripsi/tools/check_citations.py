"""Check thesis citations against the verified reference list and BINUS rules.

Run from the skripsi folder:  python tools/check_citations.py [--min-recent 30]

Checks:
* every cited key exists in referensi_terverifikasi.json / ref.bib;
* BINUS rule: "et al." only for more than five authors, so sources with 1-5
  authors must use the starred natbib forms (\\citet* / \\citep*), which print the
  full author list, and sources with 6+ authors the unstarred forms;
* no hand-written "et al." in the prose;
* number of distinct cited references published 2021-2026 (default minimum 30).
Exit status 1 when a rule is violated.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CITE = re.compile(r"\\(citet|citep|citealp|citeauthor|citeyear|cite)(\*?)\s*(?:\[[^\]]*\]\s*){0,2}\{([^}]*)\}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-recent", type=int, default=30)
    parser.add_argument("files", nargs="*", default=[f"bab{i}.tex" for i in range(1, 6)] + ["abstrak.tex", "lampiran.tex"])
    args = parser.parse_args()
    refs = {r["key"]: r for r in json.loads((ROOT / "referensi_terverifikasi.json").read_text(encoding="utf-8"))}
    problems, cited = [], {}
    for name in args.files:
        path = ROOT / name
        if not path.exists():
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            # Strip LaTeX comments but keep escaped percent signs ("21\%"); splitting on every "%"
            # silently skipped all citations that follow a percentage on the same line.
            code = re.sub(r"(?<!\\)%.*", "", line)
            if re.search(r"\bet al\b", code) and "\\cite" not in code:
                problems.append(f"{name}:{number}: hand-written 'et al.' (let apacite format citations)")
            for command, star, keys in CITE.findall(code):
                for key in (k.strip() for k in keys.split(",") if k.strip()):
                    if key not in refs:
                        problems.append(f"{name}:{number}: unknown key '{key}' (not in verified list)")
                        continue
                    cited.setdefault(key, set()).add(name)
                    authors = len(refs[key]["authors"])
                    if command in ("citet", "citep", "citealp", "citeauthor"):
                        if authors <= 5 and authors >= 3 and not star:
                            problems.append(f"{name}:{number}: \\{command}{{{key}}} has {authors} authors; use \\{command}*")
                        if authors >= 6 and star:
                            problems.append(f"{name}:{number}: \\{command}*{{{key}}} has {authors} authors; drop * (et al. allowed)")
                    if command == "cite":
                        problems.append(f"{name}:{number}: use \\citet*/\\citep* (or \\citet/\\citep for 6+ authors) instead of \\cite")
    recent = sorted(k for k in cited if 2021 <= refs[k]["year"] <= 2026)
    print(f"distinct cited references: {len(cited)}; published 2021-2026: {len(recent)} (minimum {args.min_recent})")
    by_file = {}
    for key, files in cited.items():
        for name in files:
            by_file.setdefault(name, []).append(key)
    for name in sorted(by_file):
        print(f"  {name}: {len(by_file[name])} keys")
    if len(recent) < args.min_recent:
        problems.append(f"only {len(recent)} distinct 2021-2026 references cited; need {args.min_recent}")
    for problem in problems:
        print("PROBLEM", problem)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
