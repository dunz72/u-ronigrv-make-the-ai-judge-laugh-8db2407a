"""Copy the one-line entry to the grader output directory.

Stdlib only. Reads entry.txt next to this file, validates the single
line, writes it to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt
when that variable is unset), then verifies the copy byte-for-byte
with SHA-256.
"""

import hashlib
import os
import sys
from pathlib import Path


def entry_path() -> Path:
    return Path(__file__).resolve().parent / "entry.txt"


def output_path() -> Path:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(out_dir) / "entry.txt"


def read_entry(path: Path) -> bytes:
    if not path.is_file():
        raise SystemExit(f"entry file missing: {path}")
    data = path.read_bytes()
    if len(data) == 0:
        raise SystemExit("entry file is empty")
    return data


def check_line(data: bytes) -> str:
    text = data.decode("utf-8")
    if "\r" in text:
        raise SystemExit("entry must not contain carriage returns")
    if text.count("\n") > 1:
        raise SystemExit("entry must be a single line")
    line = text.rstrip("\n")
    if not line:
        raise SystemExit("entry line is empty")
    if len(line) > 200:
        raise SystemExit(f"entry line is {len(line)} chars, over the 200 limit")
    return line


def write_output(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify_copy(source: bytes, target_path: Path) -> str:
    copied = target_path.read_bytes()
    if copied != source:
        raise SystemExit("output bytes differ from entry.txt")
    digest = sha256_hex(copied)
    if digest != sha256_hex(source):
        raise SystemExit("SHA-256 mismatch after copy")
    return digest


def main() -> int:
    raw = read_entry(entry_path())
    check_line(raw)
    target = output_path()
    write_output(target, raw)
    digest = verify_copy(raw, target)
    print(f"wrote {target} ({len(raw)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
