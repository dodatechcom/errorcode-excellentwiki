---
title: "[Solution] Bash Conditional Expression Expected Error"
description: "Fix 'conditional expression expected' in Bash when a test condition is malformed."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Bash Conditional Expression Expected Error Fix

This error occurs when Bash encounters an incomplete or malformed conditional expression in `if`, `while`, or `[[ ]]` constructs.

## Description

Bash conditional expressions require proper syntax with operands and operators. When the expression is empty, missing an operand, or uses incorrect syntax, Bash reports that it expected a conditional expression.

## Common Causes

- **Empty variable in condition** — `[[ $var == "value" ]]` where `$var` is unset.
- **Missing operand** — `[[ -f ]]` without specifying a filename.
- **Using `=` instead of `==` in `[[ ]]`** — while `=` works, some edge cases fail.
- **Unquoted variable causes word splitting** — leading to malformed expression.

## How to Fix

### Fix 1: Quote variables in conditions

```bash
# Wrong — fails if var is empty
[[ $var == "value" ]]

# Right — safe even if empty
[[ "$var" == "value" ]]
```

### Fix 2: Always provide both operands

```bash
# Wrong
[[ -f ]]

# Right
[[ -f "$FILE" ]]
```

### Fix 3: Use proper comparison operators

```bash
# Wrong — = in [[ ]] can be ambiguous
[[ $a = $b ]]

# Right — use == for string comparison
[[ "$a" == "$b" ]]
```

### Fix 4: Initialize variables before conditional checks

```bash
var=""

if [[ "$var" == "value" ]]; then
    echo "matched"
fi
```

## Examples

```bash
$ unset x
$ [[ $x == "yes" ]]
bash: conditional expression expected

$ [[ -f ]]
bash: conditional expression expected: missing argument

$ if [ $UNSET_VAR -eq 1 ]; then
bash: conditional expression expected
```

## Related Errors

- [Unbound Variable](unbound-variable) — unset variables with `set -u`.
- [Too Many Arguments](too-many-arguments) — malformed test expressions.
