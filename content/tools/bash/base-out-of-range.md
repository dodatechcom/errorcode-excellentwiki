---
title: "[Solution] Base Out of Range Error"
description: "Fix 'base out of range' errors with Bash arithmetic base conversion."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Base Out of Range Error

The numeric base used in `16#hex` or `2#bin` syntax is invalid or a digit exceeds the base.

### Common Causes
- Base outside range 2-64.
- Digit exceeds the specified base (e.g., `8#9`).
- Non-numeric characters in the number.

### How to Fix
```bash
# Valid bases: 2-64
echo $(( 16#FF ))    # 255
echo $(( 2#1010 ))   # 10
echo $(( 8#77 ))     # 63

# Invalid: digit exceeds base
# echo $(( 8#99 ))   # error: 9 not valid in octal

# Convert hex to decimal
echo $(( 0x1F ))     # 31

# Convert binary
echo $(( 2#1101 ))   # 13
```

### Example
```bash
# Broken
echo $(( 8#18 ))    # 8 is not valid in octal

# Fixed
echo $(( 8#17 ))    # 15
```
