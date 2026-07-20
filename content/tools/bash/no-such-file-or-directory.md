---
title: "[Solution] No Such File or Directory"
description: "Resolve 'No such file or directory' errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] No Such File or Directory

The file or directory referenced does not exist at the given path.

### Common Causes
- Typo in the file or directory path.
- File has been moved or deleted.
- Symlink target is missing.
- Working directory changed unexpectedly.

### How to Fix
```bash
# Check if file exists before using it
if [[ -f "$filepath" ]]; then
    cat "$filepath"
fi

# Use absolute paths for reliability
source /full/path/to/config.sh

# Check for broken symlinks
ls -la link_name
file link_name
```

### Example
```bash
# Broken
source ./config.sh  # file doesn't exist in cwd

# Fixed
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/config.sh"
```
