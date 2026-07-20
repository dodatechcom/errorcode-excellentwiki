---
title: "[Solution] Verbose Mode (set -v) Error"
description: "Fix verbose mode output issues in Bash scripts."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Verbose Mode (set -v) Error

`set -v` prints each line as it is read, which can be very noisy.

### Common Causes
- `set -v` enabled globally.
- Verbose output interfering with script logic.
- Mixing verbose and xtrace modes.

### How to Fix
```bash
# Enable verbose only for specific sections
set -v
source problem_file.sh
set +v

# Use PS4 to control xtrace instead of verbose
set -x    # shows execution, not reading

# Check current settings
set -o | grep -E 'verbose|xtrace'

# Disable both
set +v +x
```

### Example
```bash
# Broken
set -v
source large_config.sh    # massive output

# Fixed
bash -v large_config.sh > /tmp/verbose.log 2>&1
```
