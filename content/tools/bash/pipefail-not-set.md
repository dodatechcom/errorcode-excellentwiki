---
title: "[Solution] Pipefail Not Set Error"
description: "Enable set -o pipefail to catch pipeline errors."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Pipefail Not Set Error

Without `pipefail`, only the exit code of the last command in a pipeline is checked.

### Common Causes
- Early pipeline failures go undetected.
- `set -e` doesn't catch failures in non-final pipeline stages.
- Unexpected behavior with `&&` and pipelines.

### How to Fix
```bash
# Enable pipefail (recommended in all scripts)
set -o pipefail

# Now any pipeline stage failure is caught
false | true
echo $?    # 1 (with pipefail)

# Combine with set -e
set -eo pipefail

# Check all pipeline exit codes
command1 | command2 | command3
echo "${PIPESTATUS[@]}"    # exit codes of all 3 commands
```

### Example
```bash
# Broken (exit code is 0, hiding failure)
false | true | echo "ok"
echo $?    # 0

# Fixed
set -o pipefail
false | true | echo "ok"
echo $?    # 0 (last command succeeded, but check PIPESTATUS)
```
