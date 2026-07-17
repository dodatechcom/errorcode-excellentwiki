---
title: "[Solution] Python SyntaxError — Invalid Encoding Declaration"
description: "Fix Python SyntaxError caused by invalid encoding declarations. Learn how encoding cookies work and how to declare encodings correctly."
languages: ["python"]
severities: ["error"]
error_types: ["syntax"]
weight: 5
---

# SyntaxError — Invalid Encoding Declaration

A `SyntaxError` with the message "invalid encoding declaration" is raised when an encoding cookie in a Python source file is malformed or uses an invalid encoding name. Encoding cookies must appear in the first two lines of the file.

## Description

Python source files can contain an encoding declaration (also called an encoding cookie) to specify the character encoding. The format is `# -*- coding: <encoding> -*-` or `# coding=<encoding>`. This cookie must appear in the first two lines of the file. Invalid encoding names or malformed cookies cause `SyntaxError`.

Common patterns:

- **Misspelled encoding** — `# -*- coding: utf-8 -*-` as `# -*- coding: utf-8 -*-` with typo.
- **Invalid encoding name** — `# -*- coding: invalid-encoding -*-`.
- **Cookie in wrong position** — encoding declaration after line 2.
- **Malformed cookie syntax** — missing `coding:` part.

## Common Causes

```python
# Cause 1: Misspelled encoding name
# -*- coding: utf-8 -*-  # If misspelled as "utf-8" with wrong chars

# Cause 2: Invalid encoding name
# -*- coding: invalid-encoding -*-
print("Hello")

# Cause 3: Cookie after line 2
print("First line")
print("Second line")
# -*- coding: utf-8 -*-  # Too late — SyntaxError

# Cause 4: Malformed cookie
# -*- coding utf-8 -*-  # Missing colon
print("Hello")
```

## Solutions

### Fix 1: Use correct encoding cookie format

```python
# Wrong
# -*- coding utf-8 -*-  # Missing colon

# Correct
# -*- coding: utf-8 -*-
print("Hello")
```

### Fix 2: Use a valid encoding name

```python
# Wrong
# -*- coding: invalid-encoding -*-
print("Hello")

# Correct
# -*- coding: utf-8 -*-
print("Hello")
```

### Fix 3: Place encoding cookie in first two lines

```python
# Wrong — cookie after line 2
print("Line 1")
print("Line 2")
# -*- coding: utf-8 -*-  # SyntaxError

# Correct — cookie in first line
# -*- coding: utf-8 -*-
print("Line 1")
print("Line 2")
```

### Fix 4: Remove encoding cookie for UTF-8 (Python 3 default)

```python
# Python 3 defaults to UTF-8 — no cookie needed
print("Hello, 世界")
```

## Related Errors

- [SyntaxError: source file cannot be编码](encoding-cookie-2) — related encoding issue.
- [SyntaxError](../syntaxerror) — general syntax errors.
- [SyntaxWarning](../syntaxwarning) — syntax-related warnings.
