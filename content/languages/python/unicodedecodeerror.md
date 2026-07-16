---
title: "[Solution] Python UnicodeDecodeError — Can't Decode Byte Sequence Fix"
description: "Fix Python UnicodeDecodeError when decoding bytes fails. Specify encoding like utf-8 or latin-1, use errors parameter, or handle BOM."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["unicodedecodeerror", "unicode", "encoding", "bytes", "utf-8"]
weight: 72
---

# UnicodeDecodeError — Can't Decode Byte Sequence Fix

A `UnicodeDecodeError` is raised when Python tries to decode a byte sequence using a specific encoding but encounters bytes that are invalid for that encoding. It's a subclass of `ValueError`.

## Description

Python 3 strings are Unicode by default, but files, network data, and system interactions often use bytes. When converting bytes to str, Python must decode them using a specific encoding (usually UTF-8). If the bytes don't match the expected encoding, the error occurs.

Common scenarios:

- **Wrong encoding assumption** — file is Latin-1 but decoded as UTF-8.
- **Corrupted file data** — bytes are truncated or damaged.
- **Mixed encodings** — file contains characters from multiple encodings.
- **Binary file read as text** — image or compiled file opened without binary mode.
- **BOM (Byte Order Mark)** — encoding declaration at file start not handled.

## Common Causes

```python
# Cause 1: Wrong encoding for the file
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()  # UnicodeDecodeError if file is Latin-1

# Cause 2: Decoding bytes with wrong encoding
data = b"café"
decoded = data.decode("ascii")  # UnicodeDecodeError: é not in ASCII

# Cause 3: Binary file read as text
with open("image.png", "r") as f:
    content = f.read()  # UnicodeDecodeError on binary data

# Cause 4: Corrupted or truncated data
partial_bytes = b"\xc3\xa9"  # Valid UTF-8 for "é"
truncated = partial_bytes[:1]  # b"\xc3" — incomplete sequence
decoded = truncated.decode("utf-8")  # UnicodeDecodeError

# Cause 5: BOM not handled
data = b"\xef\xbb\xbfHello"  # UTF-8 with BOM
decoded = data.decode("utf-8")  # Includes BOM character in string
```

## Solutions

### Fix 1: Specify the correct encoding

```python
# Wrong — assumes UTF-8
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Correct — match the file's actual encoding
with open("data.txt", "r", encoding="latin-1") as f:
    content = f.read()

# Or use chardet to detect encoding
import chardet
with open("data.txt", "rb") as f:
    raw = f.read()
    detected = chardet.detect(raw)
    print(detected)  # {'encoding': 'ISO-8859-1', 'confidence': 0.99}
```

### Fix 2: Use the errors parameter to handle invalid bytes

```python
# Wrong — crashes on bad bytes
data = b"hello \xff world"
decoded = data.decode("utf-8")  # UnicodeDecodeError

# Correct — replace or ignore bad bytes
decoded = data.decode("utf-8", errors="replace")  # "hello  world"
decoded = data.decode("utf-8", errors="ignore")   # "hello  world"
decoded = data.decode("utf-8", errors="backslashreplace")  # "hello \\xff world"
decoded = data.decode("utf-8", errors="xmlcharrefreplace")  # "hello &#255; world"
```

### Fix 3: Open binary files in binary mode

```python
# Wrong — reading binary file as text
with open("image.png", "r") as f:
    content = f.read()

# Correct — use binary mode
with open("image.png", "rb") as f:
    content = f.read()
```

### Fix 4: Handle BOM (Byte Order Mark)

```python
# Wrong — BOM included in decoded string
data = b"\xef\xbb\xbfHello"
decoded = data.decode("utf-8")  # "\ufeffHello"

# Correct — use utf-8-sig to strip BOM
decoded = data.decode("utf-8-sig")  # "Hello"

# Or handle manually
if data.startswith(b"\xef\xbb\xbf"):
    data = data[3:]
decoded = data.decode("utf-8")
```

### Fix 5: Safely decode with fallback encoding chain

```python
# Wrong — single encoding assumption
def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

# Correct — try multiple encodings
def read_file(filepath):
    encodings = ["utf-8", "latin-1", "ascii", "cp1252"]
    for encoding in encodings:
        try:
            with open(filepath, "r", encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(
        encoding, b"", 0, 1, "Could not decode file"
    )
```

### Fix 6: Process bytes directly when needed

```python
# Wrong — trying to decode raw network bytes
data = socket.recv(1024)
text = data.decode("utf-8")  # May fail

# Correct — accumulate and decode safely
buffer = b""
while True:
    chunk = socket.recv(1024)
    if not chunk:
        break
    buffer += chunk
try:
    text = buffer.decode("utf-8")
except UnicodeDecodeError:
    text = buffer.decode("latin-1")
```

## Related Errors

- [UnicodeEncodeError](#) — encoding a string to bytes fails.
- [UnicodeTranslateError](#) — translating Unicode code point fails.
- [ValueError](../valueerror) — invalid value passed to a function.
