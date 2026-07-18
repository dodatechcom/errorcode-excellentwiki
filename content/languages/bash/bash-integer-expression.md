---
title: "[Solution] Bash Integer Expression Expected Error Fix"
description: "Fix '[: integer expression expected' in Bash. Resolve test bracket errors when variables contain non-numeric values."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Bash Integer Expression Expected Error Fix

The `[: integer expression expected` error occurs when the `[` (test) command receives a non-numeric value where it expects an integer for comparison.

## What This Error Means

When you use `[ "$var" -eq 5 ]`, Bash expects `$var` to contain a valid integer. If `$var` is empty, contains spaces, or holds a string, the test command cannot perform the numeric comparison and throws this error.

A typical error:

```
script.sh: line 3: [: : integer expression expected
```

## Why It Happens

Common causes include:

- **Empty variable** — `[ "$count" -eq 5 ]` when `$count` is unset.
- **Variable with whitespace** — `[ "$value" -gt 0 ]` when `$value` has spaces.
- **String in numeric context** — `[ "$name" -eq 1 ]` where `$name` is "hello".
- **Unquoted variable** — Word splitting causes multiple arguments to the test.
- **Command output contains non-numeric data** — Backtick expansion producing text.

## How to Fix It

### Fix 1: Set default values for variables

```bash
# WRONG: Variable may be empty
count=""
if [ "$count" -eq 5 ]; then
    echo "five"
fi

# RIGHT: Set default value
count=${count:-0}
if [ "$count" -eq 5 ]; then
    echo "five"
fi
```

### Fix 2: Validate variable is numeric before comparison

```bash
# RIGHT: Check if variable is a number first
if [[ "$value" =~ ^[0-9]+$ ]]; then
    if [ "$value" -gt 10 ]; then
        echo "Greater than 10"
    fi
else
    echo "Not a number: $value"
fi
```

### Fix 3: Use double brackets for safer comparisons

```bash
# WRONG: Single bracket fails with empty vars
if [ $count -gt 5 ]; then
    echo "big"
fi

# RIGHT: Double brackets handle empty vars
if [[ "$count" -gt 5 ]]; then
    echo "big"
fi
```

### Fix 4: Use -eq and -ne for integer comparisons

```bash
# RIGHT: Proper integer comparisons
value=${1:-0}
if [[ "$value" =~ ^-?[0-9]+$ ]]; then
    if [ "$value" -eq 0 ]; then
        echo "zero"
    elif [ "$value" -gt 0 ]; then
        echo "positive"
    else
        echo "negative"
    fi
fi
```

### Fix 5: Handle command substitution results

```bash
# WRONG: wc -l may have leading spaces
count=$(wc -l < file.txt)
if [ "$count" -gt 10 ]; then
    echo "too many lines"
fi

# RIGHT: Trim whitespace
count=$(wc -l < file.txt | tr -d ' ')
if [ "$count" -gt 10 ]; then
    echo "too many lines"
fi
```

## Common Mistakes

- **Not quoting variables** — Always use `"$var"` in test expressions.
- **Assuming variables are always set** — Use `${var:-default}` to provide defaults.
- **Using `-eq` for strings** — Use `=` for string comparison, `-eq` for integers.

## Related Pages

- [Bash Unary Operator Error](bash-unary-operator-error) — Missing operands in test
- [Bash Binary Operator Error](bash-binary-operator-error) — Binary comparison issues
- [Bash Arithmetic Error](arithmetic-error) — Arithmetic expression errors
