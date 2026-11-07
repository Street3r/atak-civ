#!/usr/bin/env python3
"""Helper tooling for the Finnish (fi) localization of ATAK-CIV.

Subcommands
  dump    Print untranslated strings (English + reference languages) in batches
          so they can be translated by hand.
  build   Merge translation files (key<TAB>value) into values-fi/strings.xml,
          keeping the order and section comments of the English source.
  check   Validate values-fi/strings.xml against the English source
          (unknown keys, format placeholders, escaping, XML well-formedness).

Translation files are plain UTF-8 text, one entry per line:
    key<TAB>Finnish value (Android resource escaping, same as strings.xml)
Lines starting with '#' are ignored. Later files override earlier ones.
The token {SP} is expanded to an escaped space (backslash-u0020).

String arrays with literal (non-@string) items are translated in arrays.txt in
the same work directory, one item per line:
    array_name[index]<TAB>Finnish value
build writes values-fi/arrays.xml with only those arrays; untranslated items
are copied from the English source, so item counts always match. Arrays whose
displayed text is parsed back by the code (e.g. Enum.valueOf on the selected
spinner text) must not be listed there.
"""
import argparse
import collections
import glob
import os
import re
import sys
import xml.etree.ElementTree as ET

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RES = os.path.join(ROOT, "atak", "ATAK", "app", "src", "main", "res")
EN = os.path.join(RES, "values", "strings.xml")
FI = os.path.join(RES, "values-fi", "strings.xml")
EN_ARRAYS = os.path.join(RES, "values", "arrays.xml")
FI_ARRAYS = os.path.join(RES, "values-fi", "arrays.xml")
ARRAY_KEY_RE = re.compile(r"^([A-Za-z0-9_]+)\[(\d+)\]$")

STRING_RE = re.compile(r'<string name="([^"]+)"([^>]*)>(.*?)</string>', re.S)
PLACEHOLDER_RE = re.compile(r"%(?:\d+\$)?[-#+ 0,(]*\d*(?:\.\d+)?[a-zA-Z%]")


def load(path):
    """Return OrderedDict key -> (attrs, raw value)."""
    out = collections.OrderedDict()
    if not os.path.exists(path):
        return out
    with open(path, encoding="utf-8") as fh:
        for key, attrs, val in STRING_RE.findall(fh.read()):
            out[key] = (attrs, val)
    return out


def translatable(en):
    return collections.OrderedDict(
        (k, v) for k, (a, v) in en.items() if 'translatable="false"' not in a)


def read_tsv(paths):
    out = collections.OrderedDict()
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            for n, line in enumerate(fh, 1):
                line = line.rstrip("\n")
                if not line.strip() or line.startswith("#"):
                    continue
                if "\t" not in line:
                    sys.exit(f"{p}:{n}: missing TAB: {line[:80]}")
                key, val = line.split("\t", 1)
                # {SP} is shorthand for an escaped, non-collapsible space
                out[key.strip()] = val.replace("{SP}", chr(92) + "u0020")
    return out


def read_keep(work):
    """Keys deliberately left in English (keep.txt: one key per line, # comments)."""
    path = os.path.join(work or "", "keep.txt")
    if not work or not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return [l.split("#", 1)[0].strip() for l in fh if l.split("#", 1)[0].strip()]


def placeholders(s):
    return sorted(m for m in PLACEHOLDER_RE.findall(s) if m != "%%")


# Keys whose Finnish text deliberately drops the leading space of the English
# fragment because it attaches directly to the preceding word ("KML-kulkujälki",
# "Alpha, alkuaika").
WHITESPACE_OK = {
    "track_exported",
    "track_export_failed",
    "server_export_failed",
    "beginning_at",
}


def problems(key, en_val, fi_val):
    errs = []
    if placeholders(en_val) != placeholders(fi_val):
        errs.append(f"placeholders {placeholders(en_val)} != {placeholders(fi_val)}")
    if en_val.count("\\n") != fi_val.count("\\n"):
        errs.append(f"\\n count {en_val.count(chr(92)+'n')} != {fi_val.count(chr(92)+'n')}")
    # unescaped apostrophe / quote (Android drops or rejects them)
    stripped = re.sub(r"\\.", "", fi_val)
    if "'" in stripped and not (fi_val.startswith('"') and fi_val.endswith('"')):
        errs.append("unescaped apostrophe")
    inner = fi_val[1:-1] if fi_val.startswith('"') and fi_val.endswith('"') and len(fi_val) > 1 else fi_val
    if '"' in re.sub(r"\\.", "", inner):
        errs.append("unescaped double quote")
    if fi_val[:1] in ("@", "?") and en_val[:1] not in ("@", "?"):
        errs.append("value starts with @ or ? (needs escaping)")
    if re.search(r"&(?!(amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)", fi_val):
        errs.append("bare &")
    if "<" in fi_val and "<" not in en_val:
        errs.append("raw <")
    if not fi_val.strip():
        errs.append("empty")
    # surrounding whitespace markers should survive
    for mark in ("\\u0020",):
        if key in WHITESPACE_OK:
            break
        if en_val.startswith(mark) != fi_val.startswith(mark) or en_val.endswith(mark) != fi_val.endswith(mark):
            errs.append(f"leading/trailing {mark} mismatch")
    return errs


def load_arrays(path):
    """Return OrderedDict name -> (attrs, [raw item values]) for <string-array>."""
    out = collections.OrderedDict()
    if not os.path.exists(path):
        return out
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    for m in re.finditer(r'<string-array\s+([^>]*)>(.*?)</string-array>', src, re.S):
        attrs = m.group(1)
        name = re.search(r'name="([^"]+)"', attrs).group(1)
        out[name] = (attrs, re.findall(r"<item>(.*?)</item>", m.group(2), re.S))
    return out


def read_array_tr(work):
    path = os.path.join(work or "", "arrays.txt")
    if not work or not os.path.exists(path):
        return collections.OrderedDict()
    return read_tsv([path])


def array_problems(en_arrays, tr):
    """Validate arrays.txt entries; returns list of (key, message)."""
    out = []
    for key, val in tr.items():
        m = ARRAY_KEY_RE.match(key)
        if not m:
            out.append((key, "key must look like name[index]")); continue
        name, idx = m.group(1), int(m.group(2))
        if name not in en_arrays:
            out.append((key, "unknown array")); continue
        attrs, items = en_arrays[name]
        if 'translatable="false"' in attrs:
            out.append((key, "array is translatable=false")); continue
        if idx >= len(items):
            out.append((key, f"index out of range ({len(items)} items)")); continue
        if items[idx].startswith("@"):
            out.append((key, f"item is a reference ({items[idx]}); translate the string instead")); continue
        out.extend((key, e) for e in problems(key, items[idx], val))
    return out


def cmd_dump(args):
    en = translatable(load(EN))
    done = read_tsv(sorted(glob.glob(os.path.join(args.work, "*.tsv")))) if args.work else {}
    done = dict(done, **{k: "" for k in read_keep(args.work)})
    refs = {lang: load(os.path.join(RES, f"values-{lang}", "strings.xml")) for lang in args.ref}
    keys = [k for k in en if k not in done]
    if args.start:
        keys = keys[keys.index(args.start):] if args.start in keys else keys
    keys = keys[: args.count]
    for k in keys:
        print(f"## {k}\n en: {en[k]}")
        for lang, d in refs.items():
            if k in d and d[k][1] != en[k] and (lang == args.ref[0] or len(en[k]) <= args.short):
                print(f" {lang}: {d[k][1]}")
    print(f"# remaining after this batch: {len([k for k in en if k not in done]) - len(keys)}", file=sys.stderr)


def cmd_build(args):
    with open(EN, encoding="utf-8") as fh:
        src = fh.read()
    en = load(EN)
    tr = read_tsv(sorted(glob.glob(os.path.join(args.work, "*.tsv"))))
    unknown = [k for k in tr if k not in en or 'translatable="false"' in en[k][0]]
    if unknown:
        print(f"WARNING: {len(unknown)} unknown/non-translatable keys ignored: {unknown[:10]}", file=sys.stderr)
    lines = ['<?xml version="1.0" encoding="utf-8"?>', "<resources>"]
    body = src.split("<resources>", 1)[1].rsplit("</resources>", 1)[0]
    # walk comments and strings in source order
    for m in re.finditer(r"(<!--.*?-->)|" + STRING_RE.pattern, body, re.S):
        if m.group(1):
            if not args.no_comments:
                lines.append("  " + m.group(1))
            continue
        key, attrs = m.group(2), m.group(3)
        if 'translatable="false"' in attrs or key not in tr:
            continue
        lines.append(f'  <string name="{key}">{tr[key]}</string>')
    lines.append("</resources>")
    # drop comment lines that ended up with nothing after them before next comment
    cleaned = []
    for i, l in enumerate(lines):
        if l.strip().startswith("<!--"):
            nxt = next((x for x in lines[i + 1:] if not x.strip().startswith("<!--")), "")
            if not nxt.strip().startswith("<string"):
                continue
        cleaned.append(l)
    os.makedirs(os.path.dirname(FI), exist_ok=True)
    with open(FI, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(cleaned) + "\n")
    n = sum(1 for k in tr if k in en and 'translatable="false"' not in en[k][0])
    print(f"wrote {FI}: {n}/{len(translatable(en))} strings")
    build_arrays(args.work)


def build_arrays(work):
    tr = read_array_tr(work)
    if not tr:
        return
    en_arrays = load_arrays(EN_ARRAYS)
    bad = array_problems(en_arrays, tr)
    if bad:
        for k, e in bad:
            print(f"arrays.txt {k}: {e}", file=sys.stderr)
        sys.exit("arrays.txt has problems; values-fi/arrays.xml not written")
    by_name = collections.defaultdict(dict)
    for key, val in tr.items():
        m = ARRAY_KEY_RE.match(key)
        by_name[m.group(1)][int(m.group(2))] = val
    lines = ['<?xml version="1.0" encoding="utf-8"?>', "<resources>"]
    for name, (attrs, items) in en_arrays.items():
        if name not in by_name:
            continue
        lines.append(f'    <string-array name="{name}">')
        for i, item in enumerate(items):
            lines.append(f"        <item>{by_name[name].get(i, item)}</item>")
        lines.append("    </string-array>")
    lines.append("</resources>")
    with open(FI_ARRAYS, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"wrote {FI_ARRAYS}: {len(by_name)} arrays, {len(tr)} items")


def cmd_check(args):
    if args.file and os.path.basename(args.file) == "arrays.txt":
        tr = read_tsv([args.file])
        bad = array_problems(load_arrays(EN_ARRAYS), tr)
        for k, e in bad:
            print(f"{k}: {e}")
        print(f"checked {len(tr)} array items, {len(bad)} problems")
        sys.exit(1 if bad else 0)
    en = load(EN)
    path = args.file or FI
    if not path.endswith(".tsv"):
        try:
            ET.parse(path)
        except ET.ParseError as e:
            sys.exit(f"XML parse error: {e}")
    if path.endswith(".tsv"):
        fi = {k: ("", v) for k, v in read_tsv([args.file]).items()}
    else:
        fi = load(path)
    bad = 0
    for k, (_, v) in fi.items():
        if k not in en:
            print(f"{k}: unknown key"); bad += 1; continue
        if 'translatable="false"' in en[k][0]:
            print(f"{k}: marked translatable=false in source"); bad += 1; continue
        for e in problems(k, en[k][1], v):
            print(f"{k}: {e}\n   en: {en[k][1]}\n   fi: {v}"); bad += 1
    total = len(translatable(en))
    print(f"checked {len(fi)} strings, {total - len(fi)} untranslated, {bad} problems")
    if not args.file and os.path.exists(FI_ARRAYS):
        bad += check_built_arrays()
    sys.exit(1 if bad else 0)


def check_built_arrays():
    """values-fi/arrays.xml: well-formed, known arrays, same item counts as English."""
    try:
        ET.parse(FI_ARRAYS)
    except ET.ParseError as e:
        print(f"arrays.xml parse error: {e}")
        return 1
    en_arrays, fi_arrays = load_arrays(EN_ARRAYS), load_arrays(FI_ARRAYS)
    bad = 0
    for name, (_, items) in fi_arrays.items():
        if name not in en_arrays:
            print(f"arrays.xml {name}: unknown array"); bad += 1; continue
        if len(items) != len(en_arrays[name][1]):
            print(f"arrays.xml {name}: {len(items)} items, English has {len(en_arrays[name][1])}"); bad += 1
    print(f"checked {len(fi_arrays)} arrays, {bad} problems")
    return bad


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("dump")
    d.add_argument("--work", help="directory of *.tsv files already translated")
    d.add_argument("--ref", nargs="*", default=["de", "uk", "es"])
    d.add_argument("--short", type=int, default=40, help="show secondary refs only for strings up to this length")
    d.add_argument("--start")
    d.add_argument("--count", type=int, default=200)
    b = sub.add_parser("build")
    b.add_argument("--work", required=True)
    b.add_argument("--no-comments", action="store_true")
    c = sub.add_parser("check")
    c.add_argument("--file")
    args = p.parse_args()
    {"dump": cmd_dump, "build": cmd_build, "check": cmd_check}[args.cmd](args)


if __name__ == "__main__":
    main()
