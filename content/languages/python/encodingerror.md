---
title: "[Solution] Python UnicodeDecodeError: 'utf-8' codec can't decode Fix"
description: "Fix Python UnicodeDecodeError: 'utf-8' codec can't decode. Specify correct encoding, use errors parameter, or read binary files properly."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["unicodedecodeerror", "utf-8", "encoding", "codec", "bytes"]
weight: 5
---

# UnicodeDecodeError: 'utf-8' codec can't decode

A `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xXX in position N` is raised when Python tries to decode bytes using UTF-8 encoding but encounters byte values that are not valid UTF-8. This is common when reading files, network data, or system output that use a different encoding.

## Description

UTF-8 encoding uses 1-4 bytes per character. Certain byte sequences are invalid in UTF-8 — for example, bytes 0x80-0xBF without a leading byte, or bytes 0xC0-0xFD that start a sequence but are truncated. Python 3 defaults to UTF-8 for most operations, so any non-UTF-8 data triggers this error.

Common patterns:

- **Latin-1 file read as UTF-8** — most common cause.
- **Binary file opened in text mode** — image, compiled, or zip file.
- **Windows-1252 encoded data** — common on Windows systems.
- **Network data with mixed encodings** — APIs returning non-UTF-8.

## Common Causes

```python
# Cause 1: Reading a Latin-1 file as UTF-8
with open("data.txt", "r", encoding="utf-8") as f:
    f.read()  # UnicodeDecodeError if file is Latin-1

# Cause 2: Binary file opened as text
with open("image.png", "r") as f:
    f.read()  # UnicodeDecodeError on binary data

# Cause 3: Decoding bytes with wrong encoding
data = b"caf\xe9"
text = data.decode("utf-8")  # UnicodeDecodeError: \xe9 invalid without context

# Cause 4: Subprocess output with system encoding
import subprocess
result = subprocess.run(["ls", "-la"], capture_output=True)
text = result.stdout.decode("utf-8")  # May fail on non-UTF-8 filenames

# Cause 5: Truncated UTF-8 sequence
data = b"\xc3\xa9"  # Valid UTF-8 for "é"
truncated = data[:1]  # b"\xc3" — incomplete
truncated.decode("utf-8")  # UnicodeDecodeError
```

## How to Fix

### Fix 1: Specify the correct encoding

```python
# Wrong — assumes UTF-8
with open("data.txt", "r") as f:
    content = f.read()

# Correct — use the file's actual encoding
with open("data.txt", "r", encoding="latin-1") as f:
    content = f.read()

# Or detect encoding automatically
import chardet
with open("data.txt", "rb") as f:
    raw = f.read()
    detected = chardet.detect(raw)
    print(detected)  # {'encoding': 'ISO-8859-1', 'confidence': 0.99}
```

### Fix 2: Use the errors parameter

```python
# Wrong — crashes on invalid bytes
data = b"hello \xff world"
text = data.decode("utf-8")

# Correct — replace or ignore invalid bytes
text = data.decode("utf-8", errors="replace")     # "hello � world"
text = data.decode("utf-8", errors="ignore")       # "hello  world"
text = data.decode("utf-8", errors="backslashreplace")  # "hello \\xff world"
```

### Fix 3: Open binary files in binary mode

```python
# Wrong
with open("image.png", "r") as f:
    content = f.read()  # UnicodeDecodeError

# Correct
with open("image.png", "rb") as f:
    content = f.read()  # Returns bytes, no decoding
```

### Fix 4: Handle subprocess output safely

```python
import subprocess

# Wrong
result = subprocess.run(["ls"], capture_output=True)
text = result.stdout.decode("utf-8")  # May fail

# Correct
result = subprocess.run(["ls"], capture_output=True)
text = result.stdout.decode("utf-8", errors="replace")
# Or use locale encoding
import locale
text = result.stdout.decode(locale.getpreferredencoding())
```

### Fix 5: Try multiple encodings

```python
def safe_decode(data, encodings=None):
    if encodings is None:
        encodings = ["utf-8", "latin-1", "cp1252", "ascii"]
    for enc in encodings:
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")

# Usage
text = safe_decode(b"caf\xe9")  # Tries UTF-8, falls back to Latin-1
```

## Examples

This error commonly occurs when:

- Reading CSV files exported from Excel (often encoded as Latin-1 or Windows-1252)
- Processing log files with non-ASCII filenames
- Reading binary configuration files as text
- Network APIs returning data in a non-UTF-8 encoding

## Related Errors

- [UnicodeEncodeError](#) — encoding a string to bytes fails
- [FileNotFoundError](filenotfounderror) — file doesn't exist
- [UnicodeDecodeError with BOM](unicodedecodeerror) — Byte Order Mark not handled
