---
title: "[Solution] Python Deprecated Features — Migration Guide & Replacements"
description: "Python deprecated feature migration guides. Update print statement, raw_input, and has_key for Python 3. Copy-paste fixes."
deprecated: ["python"]
---

Python 3 introduced deliberate incompatibilities with Python 2, and many Python 2 constructs were removed entirely by the time Python 2 reached end-of-life in 2020. Each entry below explains the deprecated feature, why it was removed, and the modern replacement you can copy into your codebase today.

## Deprecated Features

| Deprecated | Description | Replacement |
|------------|-------------|-------------|
| [print statement](/deprecated/python/print-statement/) | Python 2 syntax — `print "hello"` removed in Python 3 | Use the `print()` function: `print("hello")` |
| [raw_input()](/deprecated/python/raw-input-to-input/) | Python 2 input function — removed in Python 3 | Use `input()` which behaves like Python 2's `raw_input()` |
| [dict.has_key()](/deprecated/python/has-key/) | Removed in Python 3 — checks if key exists in dictionary | Use the `in` operator: `if key in my_dict:` |

## Quick Check

```bash
# Find all deprecation warnings in your project
python3 -W all -m pytest
```
