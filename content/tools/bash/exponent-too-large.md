---
title: "[Solution] Exponent Too Large Error"
description: "Resolve 'exponent too large' errors in Bash arithmetic."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Exponent Too Large Error

The exponent in an arithmetic expression exceeds the supported range.

### Common Causes
- Very large power calculation (e.g., `2**100`).
- Negative exponents (not supported in `(( ))`).

### How to Fix
```bash
# Use bc for large number arithmetic
echo "2^100" | bc

# Use awk for floating point
awk 'BEGIN { print 2^100 }'

# Check bash arithmetic limits
echo $(( 2**62 ))    # ok
echo $(( 2**63 ))    # may overflow on 32-bit

# Use Python for arbitrary precision
python3 -c "print(2**1000)"
```

### Example
```bash
# Broken
echo $(( 2**1000 ))    # too large

# Fixed
echo "2^1000" | bc
```
