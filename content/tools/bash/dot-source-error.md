---
title: "[Solution] Dot (.) Source Command Error"
description: "Fix errors when using the dot (.) command to source files."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Dot (.) Source Command Error

The `.` (dot) command to source a file in the current shell context fails.

### Common Causes
- File not found or not readable.
- Syntax error in the sourced file.
- Sourcing a binary file instead of a shell script.

### How to Fix
```bash
# Correct syntax
. ./config.sh
source ./config.sh    # equivalent in bash

# Check before sourcing
[[ -r "$file" ]] && . "$file"

# Debug the sourced file
bash -n config.sh    # syntax check only

# Source with error handling
if ! . "$file"; then
    echo "Failed to source $file" >&2
fi
```

### Example
```bash
# Broken
. nonexistent.sh    # file not found

# Fixed
if [[ -f "config.sh" ]]; then
    . config.sh
fi
```
