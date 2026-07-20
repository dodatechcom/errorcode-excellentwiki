---
title: "[Solution] Missing `esac` Keyword"
description: "Fix missing esac in Bash case statements."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Missing `esac` Keyword

A `case` statement must end with `esac` (case spelled backwards).

### Common Causes
- Forgetting to close the `case` block.
- Misspelling `esac`.

### How to Fix
```bash
# Validate case/esac pairs
grep -c '^case ' script.sh
grep -c '^esac' script.sh

shellcheck script.sh
```

### Example
```bash
# Broken
case "$1" in
    start) echo "starting" ;;
    stop)  echo "stopping" ;;

# Fixed
case "$1" in
    start) echo "starting" ;;
    stop)  echo "stopping" ;;
esac
```
