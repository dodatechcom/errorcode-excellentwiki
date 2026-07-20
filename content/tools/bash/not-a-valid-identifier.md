---
title: "[Solution] Not a Valid Identifier"
description: "Fix 'not a valid identifier' error in Bash variable assignment."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Not a Valid Identifier

The identifier used for a variable, function, or environment variable is not valid.

### Common Causes
- Variable name starts with a number or contains invalid characters.
- Exporting a variable with invalid syntax.
- Sourcing a file with malformed `export` statements.

### How to Fix
```bash
# Valid identifiers: start with letter/underscore
valid_var="ok"
_valid_var="ok"
123var="bad"    # invalid

# Check export syntax
export VAR=value    # correct
export VAR=value    # no spaces around =

# Debug the source file
bash -n sourced_file.sh
```

### Example
```bash
# Broken
export my-var="test"
my-var="test"

# Fixed
export my_var="test"
```
