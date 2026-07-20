---
title: "[Solution] Python UnicodeEncodeError — Encoding Failure Fix"
description: "Fix Python UnicodeEncodeError when encoding strings. Handle character encoding, bytes conversion, and error handlers like strict, ignore, replace, and backslashreplace."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 27
---

# Python UnicodeEncodeError — Encoding Failure Fix

A `UnicodeEncodeError` is raised when a Unicode string cannot be encoded into a target byte encoding (like ASCII, Latin-1, or UTF-8) because it contains characters that the encoding cannot represent.

## Common Causes

```python
# Cause 1: Encoding non-ASCII characters to ASCII
text = "Hello, 世界"
encoded = text.encode("ascii")  # UnicodeEncodeError: 'ascii' codec can't encode characters

# Cause 2: Writing Unicode to a file opened in text mode with strict encoding
with open("output.txt", "w", encoding="ascii") as f:
    f.write("Café résumé")  # UnicodeEncodeError: 'ascii' codec can't encode 'é'

# Cause 3: Printing Unicode to a terminal that doesn't support it
import sys
print(sys.stdout.encoding)  # Might be 'ascii' on some servers
print("日本語")  # UnicodeEncodeError if stdout encoding is ASCII

# Cause 4: Formatting bytes with f-string defaults
name = "José"
msg = f"Hello {name}".encode("latin-1")  # Works for 'é', but:
emoji = "Hello 🌍".encode("latin-1")  # UnicodeEncodeError: character maps to <undefined>

# Cause 5: Using str.encode() with strict error handler (default)
data = "Price: €50"
bytes_data = data.encode("utf-8")  # Works
bytes_data = data.encode("ascii")  # UnicodeEncodeError
```

## How to Fix

### Fix 1: Use UTF-8 encoding instead of ASCII

```python
# Wrong
text = "Hello, 世界"
encoded = text.encode("ascii")  # UnicodeEncodeError

# Correct
encoded = text.encode("utf-8")  # b'Hello, \xe4\xb8\x96\xe7\x95\x8c'

# Or write files with UTF-8 encoding
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Café résumé 世界")
```

### Fix 2: Use error handlers to manage unencodable characters

```python
text = "Hello, 世界 🌍"

# ignore — skip characters that can't be encoded
text.encode("ascii", errors="ignore")  # b'Hello, '

# replace — substitute with ? or specified replacement
text.encode("ascii", errors="replace")  # b'Hello, ?? ???'

# backslashreplace — use \uXXXX escape sequences
text.encode("ascii", errors="backslashreplace")  # b'Hello, \\u4e16\\u754c \\U0001f30d'

# xmlcharrefreplace — use XML character references
text.encode("ascii", errors="xmlcharrefreplace")  # b'Hello, &#19990;&#30028; &#127757;'

# strict — default, raises UnicodeEncodeError
text.encode("ascii", errors="strict")  # UnicodeEncodeError
```

### Fix 3: Handle stdout encoding for server environments

```python
import sys
import io

# Fix for servers with ASCII stdout
sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer,
    encoding="utf-8",
    errors="replace"
)

print("Hello, 世界")  # Works even on ASCII-only terminals
```

### Fix 4: Sanitize strings before encoding

```python
def safe_encode(text, target_encoding="ascii"):
    """Encode text safely, replacing unencodable characters."""
    try:
        return text.encode(target_encoding)
    except UnicodeEncodeError:
        # Normalize unicode first
        import unicodedata
        normalized = unicodedata.normalize("NFKD", text)
        return normalized.encode(target_encoding, errors="replace")

result = safe_encode("Café résumé", "ascii")
# b'Caf? r?sum?' or similar with replacements
```

### Fix 5: Set encoding for subprocess and environment variables

```python
import os

# Wrong — may fail if LANG is not set
os.environ["MY_VAR"] = "über"

# Correct — ensure UTF-8 locale
os.environ["LANG"] = "en_US.UTF-8"
os.environ["MY_VAR"] = "über"

# For subprocess
import subprocess
env = os.environ.copy()
env["PYTHONIOENCODING"] = "utf-8"
subprocess.run(["python", "script.py"], env=env)
```

## Prevention Checklist

- Always use `encoding="utf-8"` when opening files for text I/O.
- Set `PYTHONIOENCODING=utf-8` for server and CI environments.
- Use `errors="replace"` or `errors="backslashreplace"` when encoding user-supplied text.
- Normalize Unicode strings with `unicodedata.normalize()` before encoding.
- Check `sys.stdout.encoding` in scripts that may run in non-UTF-8 terminals.

## Related Errors

- [UnicodeDecodeError](/languages/python/unicodedecodeerror/) — bytes cannot be decoded to a string.
- [UnicodeError](/languages/python/unicodeerror/) — base class for all Unicode encoding/decoding errors.
- [UnicodeTranslateError](/languages/python/unicodetranslateerror/) — character cannot be translated.
- [LookupError](/languages/python/encodingerror/) — unknown encoding name.
