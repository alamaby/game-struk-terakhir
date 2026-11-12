#!/usr/bin/env python3
"""Cek konsistensi scaffold Ren'Py tanpa perlu Ren'Py terinstal.

Cek:
- semua label yang di-jump ada
- semua flag/stat yang dipakai di script.rpy didefinisikan di characters.rpy
- semua image yang dipakai di script.rpy didefinisikan di script.rpy
Jalankan: python3 tools/check_script.py
"""
import re, pathlib, sys

root = pathlib.Path(__file__).resolve().parent.parent
script = (root / "game" / "script.rpy").read_text()
chars = (root / "game" / "characters.rpy").read_text()

labels = set(re.findall(r"^label (\w+):", script, re.M))
jumps = set(re.findall(r"\bjump (\w+)", script))
missing_labels = jumps - labels

defined_vars = set(re.findall(r"^default (\w+)", chars, re.M))
# variabel yang dipakai dengan $ var = / $ var +=
used_vars = set(re.findall(r"^\s*\$\s*(\w+)\s*(?:=|\+=|-=)", script, re.M))
# variabel di kondisi if
used_vars |= set(re.findall(r"\b(bukti_\w+|tanya_pak_wirya|lapor_bu_ratna|simpan_sendiri|percaya_\w+|hide_count|ketelitian|kepercayaan|keberanian|dituduh_curi_lilin)\b", script))
missing_vars = used_vars - defined_vars

defined_images = set(re.findall(r"^image (\w+(?: \w+)*)", script, re.M))
# scene bg X / show X at — ambil nama image yang dipakai
used_images = set()
for m in re.finditer(r"^\s*scene bg (\w+)", script, re.M):
    used_images.add(f"bg {m.group(1)}")
for m in re.finditer(r"^\s*show (\w+(?: \w+)?) at", script, re.M):
    used_images.add(m.group(1))
missing_images = used_images - defined_images

ok = True
for name, missing in [("label", missing_labels), ("variabel", missing_vars), ("image", missing_images)]:
    if missing:
        ok = False
        print(f"MISSING {name}: {sorted(missing)}")
    else:
        print(f"OK {name}: semua terdefinisi ({len(jumps if name=='label' else used_vars if name=='variabel' else used_images)} dipakai)")

print(f"Labels: {sorted(labels)}")
sys.exit(0 if ok else 1)
