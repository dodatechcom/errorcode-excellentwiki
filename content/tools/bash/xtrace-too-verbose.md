---
title: "[Solution] Xtrace (set -x) Too Verbose Output"
description: "Control and reduce verbose xtrace output in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Xtrace (set -x) Too Verbose Output

`set -x` produces excessive trace output that is hard to read.

### Common Causes
- `set -x` enabled globally in a complex script.
- No PS4 customization for context.
- Loops generating many trace lines.

### How to Fix
```bash
# Customize PS4 for better trace output
export PS4='+${BASH_SOURCE}:${LINENO}: '

# Enable xtrace only around specific commands
set -x
critical_command
set +x

# Use a function to toggle xtrace
trace_on() { set -x; }
trace_off() { set +x; }

# Log xtrace to a file
exec {fd}> /tmp/trace.log
BASH_XTRACEFD=$fd
set -x
```

### Example
```bash
# Broken (verbose output)
set -x
for i in $(seq 1 100); do
    echo "$i"
done
set +x

# Fixed (targeted xtrace)
for i in $(seq 1 100); do
    [[ $i -eq 50 ]] && set -x
    echo "$i"
    [[ $i -eq 50 ]] && set +x
done
```
