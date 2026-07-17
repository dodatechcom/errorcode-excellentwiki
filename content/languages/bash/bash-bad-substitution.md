---
title: "[Solution] Bash Bad Substitution Error"
description: "Fix 'bash: bad substitution' when using variable expansion syntax incorrectly in Bash scripts."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["bad-substitution", "variable-expansion", "parameter-expansion"]
weight: 5
---

# Bash Bad Substitution Error Fix

The `bad substitution` error occurs when Bash encounters invalid variable expansion syntax, such as missing `$`, wrong brace placement, or unsupported operations.

## What This Error Means

Bash's parameter expansion uses `${variable}` syntax with operations like `${var:-default}`, `${var#pattern}`, and `${var//old/new}`. The `bad substitution` error means Bash found `${}` syntax it couldn't parse.

## Common Causes

- Missing `$` before braces: `{var}` instead of `${var}`
- Unmatched braces in variable expansion
- Using `${var/pattern/replacement}` in `sh` instead of `bash`
- Special characters not properly quoted in expansion

## How to Fix

### 1. Check brace matching

```bash
# WRONG: unmatched brace
echo ${variable

# RIGHT: matched braces
echo ${variable}
```

### 2. Ensure dollar sign precedes braces

```bash
# WRONG: missing $
echo {myvar}

# RIGHT: with $
echo ${myvar}
```

### 3. Use bash shebang for advanced expansion

```bash
#!/bin/bash
# Wrong in sh: ${var//pattern/replacement}
# Right in bash:
echo ${PATH//:/\n}
```

### 4. Quote variables with special characters

```bash
# WRONG: unquoted expansion with spaces
name="hello world"
echo ${name}

# RIGHT: quoted
echo "${name}"
```

## Related Errors

- [Syntax Error](syntax-error) — general syntax issues
- [Unbound Variable](unbound-variable) — unset variable errors
