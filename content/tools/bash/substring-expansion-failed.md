---
title: "[Solution] Substring Expansion Failed"
description: "Resolve substring expansion errors in Bash ${var:offset:length}."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Substring Expansion Failed

The `${var:offset:length}` expansion received invalid parameters.

### Common Causes
- Offset or length is not a valid integer.
- Offset exceeds string length.
- Negative offset in older Bash versions.

### How to Fix
```bash
str="hello world"

# Valid substring extraction
echo "${str:0:5}"     # hello
echo "${str:6}"       # world

# Use arithmetic for variables
offset=6
echo "${str:$offset}"

# Bash 4.2+ supports negative offset
echo "${str: -5}"     # world (note the space)
echo "${str:(-5)}"    # world
```

### Example
```bash
# Broken
str="hello"
echo "${str:abc:3}"   # offset is not a number

# Fixed
echo "${str:0:3}"     # hel
```
