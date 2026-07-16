---
title: "[Solution] Python UnicodeEncodeError — ASCII Codec Can't Encode"
description: "Fix Python UnicodeEncodeError when encoding strings with ASCII codec. Learn about Unicode encoding and how to handle non-ASCII characters."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["unicodeencodeerror", "ascii", "encode", "unicode"]
weight: 5
---

# UnicodeEncodeError — 'ascii' Codec Can't Encode

A `UnicodeEncodeError` with the message "'ascii' codec can't encode character" is raised when you try to encode a string containing non-ASCII characters using the ASCII codec. ASCII only supports characters in the 0-127 range.

## Description

ASCII encoding only supports 128 characters (0-127), which includes basic English letters, digits, and punctuation. Characters outside this range (accented letters, Chinese/Japanese/Korean characters, emoji, etc.) cannot be encoded to ASCII. This error commonly occurs when writing to files, sending data over networks, or using `str.encode('ascii')`.

Common patterns:

- **Encoding non-ASCII to ASCII** — `"café".encode("ascii")`.
- **Writing to stdout with ASCII encoding** — printing Unicode to a terminal with ASCII locale.
- **File write with ASCII encoding** — opening a file with ASCII encoding and writing Unicode.
- **System default encoding** — Python 2's default was ASCII; Python 3 defaults to UTF-8.

## Common Causes

```python
# Cause 1: Direct encoding to ASCII
text = "café"
encoded = text.encode("ascii")  # UnicodeEncodeError: 'ascii' codec can't encode character 'é'

# Cause 2: Writing Unicode to file with ASCII encoding
with open("file.txt", "w", encoding="ascii") as f:
    f.write("Hello, 世界")  # UnicodeEncodeError

# Cause 3: Printing to stdout with ASCII locale
import sys
sys.stdout.reconfigure(encoding="ascii")
print("Hello, 世界")  # UnicodeEncodeError

# Cause 4: String formatting with non-ASCII
text = "Name: José"
encoded = text.encode("ascii", errors="strict")  # UnicodeEncodeError
```

## Solutions

### Fix 1: Use UTF-8 encoding instead of ASCII

```python
# Wrong
text = "café"
encoded = text.encode("ascii")  # UnicodeEncodeError

# Correct
encoded = text.encode("utf-8")  # Works
```

### Fix 2: Use errors parameter for fallback

```python
text = "café"

# Wrong
encoded = text.encode("ascii")  # UnicodeEncodeError

# Correct — replace non-ASCII with ?
encoded = text.encode("ascii", errors="replace")  # b'caf?'

# Or ignore non-ASCII
encoded = text.encode("ascii", errors="ignore")  # b'caf'

# Or use XML character references
encoded = text.encode("ascii", errors="xmlcharrefreplace")  # b'caf&#233;'
```

### Fix 3: Set the correct encoding for files

```python
# Wrong
with open("file.txt", "w", encoding="ascii") as f:
    f.write("Hello, 世界")

# Correct
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Hello, 世界")
```

### Fix 4: Configure stdout encoding

```python
import sys
import io

# Wrong
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="ascii")

# Correct
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
```

### Fix 5: Use Unicode-aware string methods

```python
text = "café"

# Wrong
encoded = text.encode("ascii")  # UnicodeEncodeError

# Correct — use unicode_escape for safe encoding
encoded = text.encode("unicode_escape")  # b'caf\\xe9'
```

## Related Errors

- [UnicodeDecodeError](../unicodedecodeerror) — decoding bytes with wrong encoding.
- [UnicodeWarning](../unicodewarning) — Unicode-related warnings.
- [UnicodeEncodeError](str-encode) — string encoding issues.
