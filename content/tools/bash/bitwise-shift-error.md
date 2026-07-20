---
title: "[Solution] Bitwise Shift Error"
description: "Fix bitwise shift operator errors in Bash arithmetic."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Bitwise Shift Error

The bitwise shift operator `<<` or `>>` has invalid operands or syntax.

### Common Causes
- Shift amount is negative or too large.
- Non-integer operand.
- Confusion with redirection `<<`.

### How to Fix
```bash
# Correct bitwise operations
echo $(( 1 << 3 ))    # 8 (shift left by 3)
echo $(( 16 >> 2 ))   # 4 (shift right by 2)

# Shift amount must be 0-63 for 64-bit
echo $(( 1 << 63 ))   # min int64

# Use with bitmasks
mask=$(( 1 << 5 ))
echo $(( 42 & mask )) # test bit 5

# Parentheses to avoid confusion with heredoc
(( result = 1 << 3 ))
```

### Example
```bash
# Broken
echo $(( 1 << -1 ))    # negative shift

# Fixed
echo $(( 1 << 3 ))     # 8
```
