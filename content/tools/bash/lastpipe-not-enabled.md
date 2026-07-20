---
title: "[Solution] Lastpipe Not Enabled"
description: "Enable and fix lastpipe ($pipestatus) errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Lastpipe Not Enabled

The `lastpipe` option allows the last command in a pipeline to run in the current shell.

### Common Causes
- `shopt -s lastpipe` not enabled.
- Using `$PIPESTATUS` without `pipefail`.
- Last command in pipe runs in subshell by default.

### How to Fix
```bash
# Enable lastpipe
shopt -s lastpipe

# Now the last command runs in current shell
echo "hello" | read -r var
echo "$var"    # hello (with lastpipe)

# Check lastpipe status
shopt lastpipe

# Use process substitution as alternative
read -r var < <(echo "hello")
echo "$var"
```

### Example
```bash
# Broken (var is empty in parent)
echo "hello" | read -r var
echo "$var"    # empty

# Fixed
shopt -s lastpipe
echo "hello" | read -r var
echo "$var"    # hello
```
