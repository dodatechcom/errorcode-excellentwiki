---
title: "[Solution] Bash Bad Substitution Error"
description: "Fix 'bad substitution' in Bash when variable expansion syntax is incorrect."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Bash Bad Substitution Error Fix

This error occurs when Bash encounters invalid syntax for variable expansion or parameter substitution.

## Description

Bash provides powerful parameter expansion features like `${var}`, `${var:-default}`, and `${var/pattern/replacement}`. When the syntax is malformed — wrong braces, invalid operators, or using Bash features in sh — this error occurs.

## Common Causes

- **Mismatched braces** — `${var` without `}`.
- **Invalid parameter expansion operator** — using unsupported syntax.
- **Using Bash syntax in sh** — `${var//pattern}` doesn't work in POSIX sh.
- **Nested expansions done incorrectly** — e.g., `${${var}}` is invalid.

## How to Fix

### Fix 1: Close all parameter expansions properly

```bash
# Wrong
echo ${var

# Right
echo ${var}
```

### Fix 2: Use bash instead of sh for advanced features

```bash
# Wrong (run with sh)
#!/bin/sh
echo ${var//old/new}

# Right (run with bash)
#!/bin/bash
echo ${var//old/new}
```

### Fix 3: Avoid direct nesting of expansions

```bash
# Wrong
echo ${${var}}

# Right — use a temporary variable
temp=${var}
echo ${temp}
```

### Fix 4: Use proper default value syntax

```bash
# Wrong
echo ${var:default}

# Right
echo ${var:-default}
```

## Examples

```bash
$ var="hello"
$ echo ${var
bash: bad substitution: no closing `}` in `${var'

$ echo ${var//e/a}
bash: bad substitution: syntax error in expression
# (when running under sh)

$ echo ${var:0:3}
bash: bad substitution
```

## Related Errors

- [Unbound Variable](unbound-variable) — variable not set when `set -u` is active.
- [Arithmetic Error](arithmetic-error) — errors in arithmetic expressions.
