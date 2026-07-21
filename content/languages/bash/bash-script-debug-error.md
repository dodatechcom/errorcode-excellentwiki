---
title: "[Solution] Bash Script Debug Error -- Incorrect Debug Mode Usage"
description: "Fix bash debug errors when using set -x or bash -x for script debugging."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["warning"]
---

# Bash Script Debug Error

This error occurs when debug output is not captured correctly or produces too much noise.

## Common Causes

- `set -x` producing excessive output
- Debug output mixing with normal script output
- Not using BASH_XTRACEFD for trace output redirection
- Debugging in functions with complex output

## How to Fix

### Redirect debug output

```bash
# WRONG: debug output mixed with normal output
set -x
echo "normal output"

# CORRECT: redirect debug to file
exec 2>debug.log
set -x
echo "normal output"
```

### Use function-level debug

```bash
debug_func() {
    set -x
    # complex logic here
    set +x
}
```

## Examples

```bash
#!/bin/bash
# Enable debugging with trace file
exec 3>trace.log
BASH_XTRACEFD=3
set -x

# Normal code here
for i in {1..5}; do
    echo "$i"
done

set +x
exec 3>&-
```
