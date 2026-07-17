---
title: "[Solution] Python SyntaxError — Source File Cannot Be Encoded"
description: "Fix Python SyntaxError when source file cannot be encoded. Learn about encoding issues in Python source files and how to resolve them."
languages: ["python"]
severities: ["error"]
error_types: ["syntax"]
weight: 5
---

# SyntaxError — Source File Cannot Be Encoded

A `SyntaxError` with the message "source file cannot be encoded" is raised when Python cannot decode a source file using the specified encoding. This happens when the file contains characters that are not valid for the declared encoding.

## Description

Python source files must be decodable according to their encoding declaration. If a file declares `# -*- coding: ascii -*-` but contains non-ASCII characters (like accented letters or Chinese characters), Python raises a `SyntaxError`. This is common when files are saved with one encoding but declare another.

Common patterns:

- **ASCII declared but contains non-ASCII** — file saved as UTF-8 but declares ASCII.
- **Wrong encoding declaration** — file contains Latin-1 characters but declares UTF-8.
- **BOM mismatch** — Byte Order Mark doesn't match declared encoding.
- **Mixed encodings** — file contains characters from different encodings.

## Common Causes

```python
# Cause 1: ASCII encoding with non-ASCII content
# -*- coding: ascii -*-
print("café")  # SyntaxError — 'é' is not ASCII

# Cause 2: Wrong encoding declaration
# -*- coding: ascii -*-
print("你好")  # SyntaxError — Chinese characters not in ASCII

# Cause 3: File saved with wrong encoding
# File saved as Latin-1 but declares UTF-8
# -*- coding: utf-8 -*-
print("café")  # May cause SyntaxError if file is actually Latin-1

# Cause 4: BOM mismatch
# UTF-8 BOM with ASCII declaration
```

## Solutions

### Fix 1: Use UTF-8 encoding (Python 3 default)

```python
# Wrong
# -*- coding: ascii -*-
print("café")  # SyntaxError

# Correct — use UTF-8
# -*- coding: utf-8 -*-
print("café")  # Works

# Or just remove the cookie (UTF-8 is default in Python 3)
print("café")
```

### Fix 2: Save file with correct encoding

```bash
# Check file encoding
file -i myfile.py

# Convert to UTF-8
iconv -f latin1 -t utf8 myfile.py > myfile_utf8.py

# Or use Python
python -c "
with open('myfile.py', 'rb') as f:
    content = f.read()
with open('myfile.py', 'wb') as f:
    f.write(content.decode('latin1').encode('utf-8'))
"
```

### Fix 3: Remove non-ASCII characters or escape them

```python
# Wrong
# -*- coding: ascii -*-
print("café")

# Correct — escape non-ASCII
# -*- coding: ascii -*-
print("caf\u00e9")

# Or use ASCII-safe representation
print("cafe")  # If accent is not essential
```

### Fix 4: Check and fix encoding in your editor

```bash
# VS Code: set encoding in settings.json
# "files.encoding": "utf8"

# Vim: set encoding
:set fileencoding=utf-8

# Emacs: set encoding
# -*- coding: utf-8 -*-
```

## Related Errors

- [Invalid encoding declaration](encoding-cookie) — malformed encoding cookie.
- [SyntaxError](../syntaxerror) — general syntax errors.
- [UnicodeDecodeError](../unicodedecodeerror) — decoding errors at runtime.
