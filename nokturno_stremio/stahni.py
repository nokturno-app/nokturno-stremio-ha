"""Při sestavení obrazu stáhne balík doplňku podle update.json, ověří SHA-256 a rozbalí do /app."""
import hashlib
import io
import json
import os
import sys
import urllib.request
import zipfile

url, cil = sys.argv[1], sys.argv[2]
hlavicky = {"User-Agent": "Nokturno zavadec"}
with urllib.request.urlopen(urllib.request.Request(url, headers=hlavicky), timeout=60) as r:
    info = json.load(r)
with urllib.request.urlopen(urllib.request.Request(info["url"], headers=hlavicky), timeout=300) as r:
    data = r.read()
if hashlib.sha256(data).hexdigest() != str(info["sha256"]).lower():
    sys.exit(f"otisk balíku {info['version']} nesedí")
with zipfile.ZipFile(io.BytesIO(data)) as z:
    z.extractall(cil)
if not os.path.isfile(os.path.join(cil, "nokturno", "server.py")):
    sys.exit("balík nemá nokturno/server.py")
with open(os.path.join(cil, "version.txt"), "w", encoding="utf-8") as f:
    f.write(str(info["version"]) + "\n")
print("Nokturno", info["version"], "rozbaleno do", cil)
