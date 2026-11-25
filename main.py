"""Make the AI Judge Laugh entry.

The single original line lives in entry.txt next to this file. This
script reads it, checks it fits the sealed gate (1-200 characters,
UTF-8, one line, not only whitespace), then writes an exact byte
copy to $MAKEFUN_OUTPUT_DIR/entry.txt, falling back to
/output/entry.txt when that variable is not set. After writing, the
copy is read back and compared by SHA-256 so a partial write can
never pass silently. Stdlib only.
"""

import hashlib
import os


def source_file():
    folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder, "entry.txt")


def load_line_bytes(path):
    with open(path, "rb") as handle:
        return handle.read()


def decode_line(raw):
    return raw.decode("utf-8")


def check_line(text):
    cleaned = text.strip()
    if not 1 <= len(cleaned) <= 200:
        raise ValueError(
            f"entry must be 1-200 characters, got {len(cleaned)}"
        )
    if not cleaned:
        raise ValueError("entry must not be only whitespace")
    if text != cleaned:
        raise ValueError("entry.txt must hold exactly one line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    return cleaned


def output_folder():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def store_copy(raw, directory):
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    with open(target, "wb") as handle:
        handle.write(raw)
    with open(target, "rb") as handle:
        stored = handle.read()
    if hashlib.sha256(stored).hexdigest() != hashlib.sha256(raw).hexdigest():
        raise ValueError("output is not byte-identical to entry.txt")
    return target


def run():
    raw = load_line_bytes(source_file())
    text = check_line(decode_line(raw))
    target = store_copy(raw, output_folder())
    print(f"wrote {len(raw)} bytes ({len(text)} chars) to {target}")


if __name__ == "__main__":
    run()
