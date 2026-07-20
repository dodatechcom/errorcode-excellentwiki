---
title: "[Solution] Python UnicodeTranslateError — str.translate() Failure"
description: "Fix Python UnicodeTranslateError from str.translate() and mapping tables. Handle character translation, table creation, and untranslatable characters."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 29
---

# Python UnicodeTranslateError — str.translate() Failure

A `UnicodeTranslateError` is raised when `str.translate()` encounters a character that cannot be translated according to the provided mapping table. This is the rarest of the `UnicodeError` subclasses and occurs when translation tables contain invalid mappings or characters outside the supported Unicode range.

## Common Causes

```python
# Cause 1: Invalid Unicode code point in translation table
table = str.maketrans({0x110000: "X"})  # Code point beyond Unicode range
"Hello".translate(table)  # UnicodeTranslateError: character maps to <undefined>

# Cause 2: Translation table maps to an invalid string value
table = str.maketrans({"H": "XYZ", "e": "\ud800"})  # Surrogate code point
"Hello".translate(table)  # UnicodeTranslateError

# Cause 3: Empty or malformed mapping dictionary
table = str.maketrans({})  # Empty table — no error here, but:
table = str.maketrans({65: None})  # Mapping to None (delete) — works for ordinals
# Using incorrect types causes TypeError, not UnicodeTranslateError

# Cause 4: Translation with None values (delete characters)
table = str.maketrans({ord("l"): None})
"Hello".translate(table)  # 'Heo' — this works, but:

# Cause 5: Binary translation table corruption
table = bytes.maketrans(b"abc", b"xyz")
# Works for bytes, but mixing str/bytes translation raises errors
```

## How to Fix

### Fix 1: Validate Unicode code points in translation tables

```python
# Wrong — code point 0x110000 is beyond valid Unicode range (max is 0x10FFFF)
table = str.maketrans({0x110000: "X"})
text = "Hello".translate(table)  # UnicodeTranslateError

# Correct — use valid code points only
MAX_UNICODE = 0x10FFFF
code_point = 0x00E9  # é — valid
table = str.maketrans({code_point: "e"})
text = "café".translate(table)  # 'cafe'
```

### Fix 2: Create translation tables correctly with str.maketrans()

```python
# Method 1: Dictionary mapping ordinals to strings or None
table = str.maketrans({
    ord("H"): "J",    # H → J
    ord("e"): "a",    # e → a
    ord("l"): None,   # Delete l
})
"Hello".translate(table)  # 'Jao'

# Method 2: Two strings of equal length (replace each char)
table = str.maketrans("abc", "xyz")
"abcde".translate(table)  # 'xyzde'

# Method 3: Three strings — third string specifies chars to delete
table = str.maketrans("abc", "xyz", "de")
"abcde".translate(table)  # 'xyz' (d and e deleted)
```

### Fix 3: Handle surrogate code points in translation

```python
# Wrong — surrogate code points (0xD800–0xDFFF) are invalid in strings
text = "Hello"
table = str.maketrans({ord("H"): chr(0xD800)})
text.translate(table)  # UnicodeTranslateError

# Correct — avoid surrogate code points
text = "Hello"
table = str.maketrans({ord("H"): "J"})
text.translate(table)  # 'Jello'
```

### Fix 4: Build safe translation tables from user data

```python
def safe_translate_table(mapping):
    """Build a translation table, filtering out invalid mappings."""
    safe = {}
    for key, value in mapping.items():
        code = ord(key) if isinstance(key, str) else key
        if 0 <= code <= 0x10FFFF:
            if isinstance(value, str):
                if all(0 <= ord(c) <= 0x10FFFF for c in value):
                    safe[code] = value
            elif value is None:
                safe[code] = None
    return str.maketrans(safe)

table = safe_translate_table({"H": "J", "e": "a", "l": None})
"Hello".translate(table)  # 'Jao'
```

### Fix 5: Use str.replace() for simple character substitutions

```python
# If translate() is causing issues, use replace() for simple cases
text = "Hello, World"

# Wrong — may fail with complex mappings
table = str.maketrans({"H": "J"})
text.translate(table)

# Simpler alternative for single replacements
text = text.replace("H", "J")

# Chain replacements
text = text.replace("H", "J").replace("e", "a").replace("ll", "x")
# 'Jaxo, World'
```

## Prevention Checklist

- Only use valid Unicode code points (0x0–0x10FFFF) in translation tables.
- Avoid surrogate code points (0xD800–0xDFFF) in any string operation.
- Use `str.maketrans()` to build translation tables — do not construct raw `bytes` tables manually.
- Validate user-provided translation mappings before passing them to `str.translate()`.
- For simple substitutions, prefer `str.replace()` over `str.translate()`.

## Related Errors

- [UnicodeEncodeError](/languages/python/unicodeencodeerror/) — string-to-bytes encoding failure.
- [UnicodeDecodeError](/languages/python/unicodedecodeerror/) — bytes-to-string decoding failure.
- [UnicodeError](/languages/python/unicodeerror/) — base class for all Unicode codec errors.
- [TypeError](/languages/python/typeerror/) — incorrect types passed to `str.maketrans()` or `str.translate()`.
