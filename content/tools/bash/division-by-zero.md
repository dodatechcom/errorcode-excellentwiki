---
title: "[Solution] Division by Zero Error"
description: "Fix 'division by 0' errors in Bash arithmetic."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Division by Zero Error

Arithmetic division or modulo by zero is undefined.

### Common Causes
- Denominator variable is 0 or unset.
- No guard against zero divisor.
- Dynamic calculations producing zero.

### How to Fix
```bash
divisor=0

# Guard against division by zero
if (( divisor != 0 )); then
    result=$(( 100 / divisor ))
else
    echo "Error: division by zero" >&2
    result=0
fi

# Use default value
divisor=${divisor:-1}

# Bash 4.4+ error message: "division by 0"
```

### Example
```bash
# Broken
a=10
b=0
echo $(( a / b ))    # division by 0

# Fixed
if (( b != 0 )); then
    echo $(( a / b ))
fi
```
