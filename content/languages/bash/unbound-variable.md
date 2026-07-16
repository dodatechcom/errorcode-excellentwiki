---
title: "[Solution] Bash Unbound Variable Error"
description: "Fix 'unbound variable' in Bash when set -u is active and a variable is not set."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["unbound-variable", "set-u", "uninitialized-variable"]
weight: 5
---

# Bash Unbound Variable Error Fix

This error occurs when `set -u` (or `set -o nounset`) is enabled and Bash tries to expand a variable that hasn't been set.

## Description

The `set -u` option makes Bash treat unset variables as errors rather than silently expanding them to empty strings. This is a safety feature to catch typos and logic bugs, but it can cause unexpected failures if variables may legitimately be unset.

## Common Causes

- **Variable not initialized** — referencing `$VAR` before it's assigned a value.
- **Optional config variable** — an environment variable that may or may not be set.
- **Typo in variable name** — `$USER_NMAE` instead of `$USER_NAME`.
- **Array element doesn't exist** — accessing `${arr[5]}` when the array has fewer elements.

## How to Fix

### Fix 1: Provide a default value

```bash
# Use ${var:-default} to supply a fallback
echo "${MY_VAR:-default_value}"
```

### Fix 2: Initialize variables before use

```bash
MY_VAR=""
# or
MY_VAR="initial value"
```

### Fix 3: Check if the variable is set first

```bash
if [[ -n "${MY_VAR:-}" ]]; then
    echo "$MY_VAR"
fi
```

### Fix 4: Use set +u for optional sections

```bash
set +u
# Section where variables may be unset
source optional-config.sh
set -u
```

## Examples

```bash
$ set -u
$ echo "$UNSET_VAR"
bash: UNSET_VAR: unbound variable

$ unset name
$ echo "Hello, ${name:-stranger}"
Hello, stranger
```

## Related Errors

- [Bad Substitution](bad-substitution) — incorrect variable expansion syntax.
- [Conditional Expression Expected](conditional-expr) — errors in test expressions.
