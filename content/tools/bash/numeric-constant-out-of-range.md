---
title: "[Solution] Numeric Constant Out of Range"
description: "Fix numeric overflow errors in Bash arithmetic."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Numeric Constant Out of Range

A numeric constant exceeds the representable range of Bash integer arithmetic.

### Common Causes
- Number exceeds 64-bit signed integer range.
- Negative numbers used where unsigned expected.

### How to Fix
```bash
# Bash uses 64-bit signed integers on most systems
max_int=$(( 2**63 - 1 ))
echo "$max_int"    # 9223372036854775807

# For larger numbers, use bc
echo "2^100" | bc

# For unsigned behavior, use bit masking
echo $(( -1 & 0xFFFFFFFFFFFFFFFF ))

# Check overflow
result=$(( 9999999999999999999 + 1 ))
# May wrap around to negative
```

### Example
```bash
# Broken
echo $(( 2**63 ))    # overflow on signed 64-bit

# Fixed
echo "2^63" | bc
```
