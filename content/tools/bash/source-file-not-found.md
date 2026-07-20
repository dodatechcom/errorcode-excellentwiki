---
title: "[Solution] Source File Not Found Error"
description: "Fix 'source: file not found' errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Source File Not Found Error

The `source` or `.` command cannot find the file to execute.

### Common Causes
- File path is incorrect.
- File does not exist.
- Working directory changed.
- File is not executable/readable.

### How to Fix
```bash
# Use absolute path
source /full/path/to/config.sh

# Use SCRIPT_DIR for relative paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/config.sh"

# Check file exists before sourcing
if [[ -f "$file" ]]; then
    source "$file"
else
    echo "Warning: $file not found" >&2
fi

# Use . instead of source for POSIX compatibility
. /path/to/config.sh
```

### Example
```bash
# Broken
source config.sh    # file not in $PWD

# Fixed
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/config.sh"
```
