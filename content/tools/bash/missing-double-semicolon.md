---
title: "[Solution] Missing `;;` in Case Statement"
description: "Bash case statement missing double semicolon separator."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Missing `;;` in Case Statement

Each pattern in a `case` statement must end with `;;`.

### Common Causes
- Forgetting `;;` between case patterns.
- Using `;` instead of `;;`.

### How to Fix
```bash
# Ensure every case branch ends with ;;
sed -n '/case/,/esac/p' script.sh

shellcheck script.sh
```

### Example
```bash
# Broken
case "$1" in
    start) echo "starting"
    stop) echo "stopping" ;;

# Fixed
case "$1" in
    start) echo "starting" ;;
    stop)  echo "stopping" ;;
esac
```
