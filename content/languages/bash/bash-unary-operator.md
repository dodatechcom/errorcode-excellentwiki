---
title: "[Solution] Bash Unary Operator Expected Error Fix"
description: "Fix '[: unary operator expected' in Bash. Resolve missing or empty test arguments causing single-operand errors."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Bash Unary Operator Expected Error Fix

The `[: unary operator expected` error occurs when the `[` (test) command receives too few arguments, typically because a variable is empty or unquoted.

## What This Error Means

A unary operator tests a single operand (like `-z "$var"` to check if empty). When the operand is missing due to an unset variable, the test command cannot evaluate the expression.

A typical error:

```
script.sh: line 4: [: unary operator expected
```

## Why It Happens

Common causes include:

- **Empty variable without quotes** — `[ -z $var ]` when `$var` is empty produces `[ -z ]` which is true.
- **Missing argument entirely** — `[ ]` with no arguments.
- **Variable with spaces** — Word splitting creates multiple arguments.
- **Unset positional parameters** — `[ -n $1 ]` when no arguments are passed.
- **Command substitution returning nothing** — `[ -f $(which cmd) ]` when `cmd` is missing.

## How to Fix It

### Fix 1: Always quote variables in test expressions

```bash
# WRONG: Unquoted variable
if [ -z $name ]; then
    echo "empty"
fi

# RIGHT: Quote the variable
if [ -z "$name" ]; then
    echo "empty"
fi
```

### Fix 2: Provide default values

```bash
# WRONG: $1 may not exist
if [ -n $1 ]; then
    echo "has argument"
fi

# RIGHT: Use default value
if [ -n "${1:-}" ]; then
    echo "has argument"
fi
```

### Fix 3: Use -n and -z correctly

```bash
# RIGHT: Check for empty string
value=""
if [ -z "$value" ]; then
    echo "empty"
fi

# RIGHT: Check for non-empty string
value="hello"
if [ -n "$value" ]; then
    echo "has value"
fi
```

### Fix 4: Guard before test

```bash
# RIGHT: Check variable exists first
if [ "${var+x}" ]; then
    if [ "$var" -gt 0 ]; then
        echo "positive"
    fi
else
    echo "variable not set"
fi
```

### Fix 5: Use [[ ]] for safer testing

```bash
# RIGHT: Double brackets are more forgiving
if [[ -z "$var" ]]; then
    echo "empty"
fi

# Double brackets don't word-split variables
if [[ $var == "test" ]]; then
    echo "match"
fi
```

## Common Mistakes

- **Forgetting quotes around variables** — This is the single most common cause.
- **Using `[ ]` when `[[ ]]` would be safer** — Double brackets are Bash-specific but safer.
- **Assuming empty variables evaluate to false** — An unset variable causes a syntax error, not false.

## Related Pages

- [Bash Binary Operator Error](bash-binary-operator-error) — Binary comparison issues
- [Bash Integer Expression Error](bash-integer-expression) — Non-numeric value errors
- [Bash Test Argument Error](bash-test-argument) — Too many test arguments
