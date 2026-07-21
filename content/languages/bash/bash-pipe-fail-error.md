---
title: "[Solution] Bash Pipe Fail Error -- Ignoring Pipe Exit Codes"
description: "Fix bash pipefail errors when using pipes that silently ignore intermediate command failures."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Pipe Fail Error

This error occurs when pipe chains ignore failures in intermediate commands because `pipefail` is not enabled.

## Common Causes

- `set -e` does not catch pipe failures by default
- Middle command in pipe fails silently
- Forgetting that only last command's exit status matters by default
- Using `set -o pipefail` inconsistently

## How to Fix

### Enable pipefail

```bash
# WRONG: middle failure ignored
cat nonexistent.txt | grep "pattern" | wc -l

# CORRECT: enable pipefail
set -o pipefail
cat nonexistent.txt | grep "pattern" | wc -l
# exits with first non-zero status
```

### Use pipefail with set -e

```bash
set -euo pipefail
# All pipe failures cause script to exit
```

## Examples

```bash
#!/bin/bash
set -o pipefail

# Safe pipe with error checking
result=$(cat data.txt | grep "error" | wc -l)
if [ $? -ne 0 ]; then
    echo "Pipe failed"
    exit 1
fi
echo "Found $result errors"
```
