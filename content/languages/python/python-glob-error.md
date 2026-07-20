---
title: "[Solution] Python glob Error — Glob Pattern Matching Errors"
description: "Fix Python glob errors including pattern syntax, recursive glob, escape characters, and no matches found. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 231
---

# Python glob Error — Glob Pattern Matching Errors

The `glob` module finds pathname patterns. Errors involve invalid pattern syntax, recursive glob issues, escape characters, and unexpected results.

## Common Causes

```python
import glob

# Error: Invalid glob pattern with unclosed bracket
files = glob.glob("/tmp/[abc")
# ValueError: Bad pattern (unclosed bracket)
```

```python
import glob

# Error: Recursive glob with ** without recursive=True
files = glob.glob("/tmp/**/*.txt")
# Returns nothing — ** requires recursive=True
```

```python
import glob
import os

# Error: Pattern with special characters not escaped
path = os.path.join("/tmp", "file[1].txt")
files = glob.glob(path)
# Matches file1.txt instead of file[1].txt
```

```python
import glob

# Error: Case sensitivity confusion
files = glob.glob("*.TXT")  # Won't match .txt on case-sensitive systems
# Returns empty list
```

```python
import glob

# Error: Pattern with invalid escape sequences
files = glob.glob("\\")  # Backslash issues
# On some systems, this may cause unexpected behavior
```

## How to Fix

### Fix 1: Use Proper Pattern Syntax

```python
import glob

# Validate bracket patterns
pattern = "[abc].txt"
files = glob.glob(f"/tmp/{pattern}")
print(files)  # matches a.txt, b.txt, c.txt

# For literal brackets, use escape
import glob
literal_bracket = glob.escape("[test].txt")
files = glob.glob(f"/tmp/{literal_bracket}")
```

### Fix 2: Use recursive=True with ** Pattern

```python
import glob

# Correct: enable recursive matching
files = glob.glob("/tmp/**/*.txt", recursive=True)
print(files)

# Or use Path for modern approach
from pathlib import Path
files = list(Path("/tmp").glob("**/*.txt"))
print(files)
```

### Fix 3: Escape Special Characters

```python
import glob
import os

# Use glob.escape() for literal file names
filename = "file[1].txt"
escaped = glob.escape(filename)
files = glob.glob(f"/tmp/{escaped}")
print(files)  # matches file[1].txt literally
```

### Fix 4: Handle Case Sensitivity

```python
import glob
import os

# Case-insensitive matching
def case_insensitive_glob(directory, pattern):
    if os.name == "nt":
        return glob.glob(os.path.join(directory, pattern))
    # On Linux/Mac, use a custom approach
    all_files = glob.glob(os.path.join(directory, "*"))
    return [f for f in all_files if f.lower().endswith(pattern.lower().replace("*", ""))]

files = case_insensitive_glob("/tmp", "*.TXT")
```

## Examples

```python
import glob
from pathlib import Path

# Find all Python files recursively
py_files = glob.glob("**/*.py", recursive=True)
print(f"Found {len(py_files)} Python files")

# Find files matching multiple patterns
import os
patterns = ["*.py", "*.txt", "*.md"]
matched = []
for pattern in patterns:
    matched.extend(glob.glob(f"src/{pattern}"))
print(matched)

# Using Path for modern glob
src = Path("src")
py_files = list(src.glob("**/*.py"))
txt_files = list(src.glob("**/*.txt"))
```

## Related Errors

- [Python ValueError](/languages/python/python-valueerror/)
- [Python FileNotFoundError](/languages/python/python-filenotfounderror/)
- [Python OSError](/languages/python/python-oserror/)
