---
title: "[Solution] Python unicodedata Error — Unicode Character Data Failures"
description: "Fix Python unicodedata errors including lookup errors, name/numeric category, east_asian_width, and bidirectional issues. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 254
---

# Python unicodedata Error — Unicode Character Data Failures

The `unicodedata` module provides access to the Unicode Character Database. Errors occur when looking up names for characters that have no name, using invalid code points, or misinterpreting character properties.

## Common Causes

```python
# Cause 1: Looking up name for character with no name
import unicodedata

unicodedata.name("\x00")  # ValueError: no such name

# Cause 2: Invalid code point in lookup
import unicodedata

unicodedata.name(chr(0x110000))  # ValueError: no such name (out of range)

# Cause 3: Misinterpreting east_asian_width
import unicodedata

# CJK characters have width 'W' (wide)
width = unicodedata.east_asian_width("中")  # Returns 'W'
# Halfwidth katakana has width 'H'
width = unicodedata.east_asian_width("ｶ")  # Returns 'H'

# Cause 4: Bidirectional property for non-character
import unicodedata

# Control characters may return unexpected bidi class
bidi = unicodedata.bidirectional("\x00")  # Returns 'BN' (Boundary Neutral)

# Cause 5: Getting numeric value for non-numeric character
import unicodedata

unicodedata.numeric("A")  # ValueError: not a numeric character
```

## How to Fix

### Fix 1: Handle missing character names

```python
import unicodedata

def safe_name(char, default="NO NAME"):
    try:
        return unicodedata.name(char)
    except ValueError:
        return default

print(safe_name("A"))       # LATIN CAPITAL LETTER A
print(safe_name("\x00"))    # NO NAME
print(safe_name("😀"))      # GRINNING FACE

# Get name or code point representation
def name_or_codepoint(char):
    try:
        return unicodedata.name(char)
    except ValueError:
        return f"U+{ord(char):04X}"

print(name_or_codepoint("A"))    # LATIN CAPITAL LETTER A
print(name_or_codepoint("\x00")) # U+0000
```

### Fix 2: Validate code points before lookup

```python
import unicodedata

def safe_character_info(char):
    code = ord(char)
    if not (0 <= code <= 0x10FFFF):
        return None

    info = {
        "char": char,
        "codepoint": f"U+{code:04X}",
        "name": None,
        "category": unicodedata.category(char),
        "bidi": unicodedata.bidirectional(char),
        "width": unicodedata.east_asian_width(char),
    }

    try:
        info["name"] = unicodedata.name(char)
    except ValueError:
        pass

    return info

print(safe_character_info("A"))
print(safe_character_info("\x00"))
```

### Fix 3: Handle east_asian_width correctly

```python
import unicodedata

def char_display_width(char):
    """Estimate display width (0, 1, or 2 columns)."""
    eaw = unicodedata.east_asian_width(char)
    if eaw in ("W", "F"):  # Wide or Fullwidth
        return 2
    elif eaw in ("H", "Na"):  # Halfwidth or Narrow
        return 1
    elif eaw == "A":  # Ambiguous — depends on context
        return 1  # Conservative estimate
    else:  # 'N' Neutral, 'Other'
        return 1

# Test with various characters
test_chars = ["A", "中", "ｶ", "é", "😀", "\t", "\n"]
for char in test_chars:
    width = char_display_width(char)
    eaw = unicodedata.east_asian_width(char)
    print(f"'{char}' -> width={width}, eaw={eaw}")
```

### Fix 4: Use bidirectional property safely

```python
import unicodedata

def is_rtl(char):
    """Check if character is right-to-left."""
    bidi = unicodedata.bidirectional(char)
    return bidi in ("R", "AL", "RLE", "RLO", "RLI")

def get_bidi_info(char):
    bidi = unicodedata.bidirectional(char)
    return {
        "char": char,
        "bidi_class": bidi,
        "is_rtl": bidi in ("R", "AL", "RLE", "RLO", "RLI"),
        "is_ltr": bidi in ("L", "LRE", "LRO", "LRI"),
    }

print(get_bidi_info("A"))   # LTR
print(get_bidi_info("ع"))   # RTL Arabic letter
print(get_bidi_info("\x00")) # Boundary Neutral
```

### Fix 5: Get numeric values safely

```python
import unicodedata

def safe_numeric(char, default=None):
    try:
        return unicodedata.numeric(char)
    except (TypeError, ValueError):
        return default

# Numeric characters
print(safe_numeric("1"))      # 1.0
print(safe_numeric("½"))      # 0.5
print(safe_numeric("⅓"))      # 0.3333333333333333
print(safe_numeric("A"))      # None

# Get category information
def char_category_info(char):
    cat = unicodedata.category(char)
    return {
        "char": char,
        "category": cat,
        "general_category": cat[0],
        "subcategory": cat[1] if len(cat) > 1 else "",
        "description": unicodedata.name(char, "No description"),
    }

print(char_category_info("A"))  # Letter, uppercase
print(char_category_info("1"))  # Number, decimal digit
```

## Examples

```python
# Real-world: Unicode character analysis
import unicodedata

def analyze_text(text):
    results = []
    for char in text:
        try:
            name = unicodedata.name(char)
        except ValueError:
            name = f"U+{ord(char):04X}"

        results.append({
            "char": char,
            "name": name,
            "category": unicodedata.category(char),
            "bidi": unicodedata.bidirectional(char),
            "east_asian_width": unicodedata.east_asian_width(char),
            "numeric": safe_numeric(char),
        })
    return results

analysis = analyze_text("Hello世界")
for item in analysis:
    print(f"{item['char']}: {item['name']} ({item['category']})")

# Real-world: Text width calculator for terminal display
import unicodedata

def calculate_width(text):
    width = 0
    for char in text:
        eaw = unicodedata.east_asian_width(char)
        if eaw in ("W", "F"):
            width += 2
        elif char in ("\n", "\r"):
            width = 0  # Newline resets
        elif unicodedata.category(char).startswith("C"):
            width += 0  # Control characters
        else:
            width += 1
    return width

print(calculate_width("Hello世界"))  # 10 (5 + 2*2 + 1)
```

## Related Errors

- [ValueError](/languages/python/valueerror/) — no such name for character
- [TypeError](/languages/python/typeerror/) — wrong argument type
- [UnicodeDecodeError](/languages/python/unicodedecodeerror/) — encoding issues
