---
title: "[Solution] Bash Binary Operator Expected Error Fix"
description: "Fix '[: binary operator expected' in Bash. Resolve missing operands in test bracket expressions and conditional logic."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Bash Binary Operator Expected Error Fix

The `[: binary operator expected` error occurs when a binary comparison operator (like `-eq`, `-gt`, `=`, `!=`) receives fewer than two operands.

## What This Error Means

Binary operators require exactly two operands: `[ operand1 operator operand2 ]`. When either operand is missing due to an empty variable, wrong quoting, or syntax mistake, Bash cannot evaluate the comparison.

A typical error:

```
script.sh: line 5: [: binary operator expected
```

## Why It Happens

Common causes include:

- **Empty first operand** — `[ $a -eq $b ]` when `$a` is empty.
- **Empty second operand** — `[ "$a" -eq ]` missing the second value.
- **Extra spaces creating empty arguments** — `[ "$a"  -eq  "$b" ]` is fine, but `[ "$a" -eq ]` is not.
- **Using wrong operator** — `[: "$a" =]` instead of `[ "$a" = "$b" ]`.
- **Variable with spaces** — Word splitting creates too many arguments.

## How to Fix It

### Fix 1: Quote all variables

```bash
# WRONG: Unquoted variables
if [ $a -eq $b ]; then
    echo "equal"
fi

# RIGHT: Quote both operands
if [ "$a" -eq "$b" ]; then
    echo "equal"
fi
```

### Fix 2: Ensure both operands exist

```bash
# RIGHT: Check both operands are set
if [ "${a+x}" ] && [ "${b+x}" ]; then
    if [ "$a" -eq "$b" ]; then
        echo "equal"
    fi
else
    echo "One or both variables not set"
fi
```

### Fix 3: Use default values

```bash
# RIGHT: Provide defaults
a=${a:-0}
b=${b:-0}
if [ "$a" -gt "$b" ]; then
    echo "a is greater"
fi
```

### Fix 4: Use correct operators

```bash
# RIGHT: String comparison
if [ "$str1" = "$str2" ]; then
    echo "strings match"
fi

# RIGHT: Integer comparison
if [ "$num1" -ne "$num2" ]; then
    echo "not equal"
fi

# RIGHT: File tests (unary, not binary)
if [ -f "$filename" ]; then
    echo "file exists"
fi
```

### Fix 5: Use case statement for string matching

```bash
# RIGHT: Avoid test brackets for complex comparisons
case "$choice" in
    start|stop|restart)
        echo "valid action"
        ;;
    *)
        echo "invalid"
        ;;
esac
```

## Common Mistakes

- **Mixing unary and binary operators** — `-f` is unary (one operand), `-eq` is binary (two).
- **Not quoting variables** — The most common source of missing operands.
- **Using `==` in single brackets** — POSIX `[ ]` uses `=` for string equality.

## Related Pages

- [Bash Unary Operator Error](bash-unary-operator-error) — Missing single operand
- [Bash Integer Expression Error](bash-integer-expression) — Non-numeric values
- [Bash Test Argument Error](bash-test-argument) — Too many test arguments
