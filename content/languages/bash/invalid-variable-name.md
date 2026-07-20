---
title: "[Solution] Bash Invalid Variable Name Error"
description: "Fix 'bash: invalid variable name' when a variable assignment uses illegal characters."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "variables", "naming", "syntax", "invalid-name"]
severity: "error"
---

# Invalid Variable Name

## Error Message

```
bash: invalid variable name
```

## Common Causes

- Using spaces in variable names (e.g., `my var=value`)
- Using hyphens instead of underscores (e.g., `my-var=value`)
- Starting a variable name with a number (e.g., `1var=value`)
- Using special characters like `@`, `#`, `$`, or `!` in variable names

## Solutions

### Solution 1: Use Valid Variable Name Characters

Bash variable names must start with a letter or underscore and can only contain letters, digits, and underscores. No spaces, hyphens, or special characters.

```bash
# Wrong — invalid names
my-var="test"       # hyphen not allowed
my var="test"       # space not allowed
1var="test"         # cannot start with digit
my@var="test"       # special character not allowed

# Right — valid names
my_var="test"       # underscore OK
myVar="test"        # camelCase OK
_var="test"         # leading underscore OK
MY_VAR_2="test"     # digits OK after first char
readonly VERSION="1.0" 
```

### Solution 2: Use Indirect References for Dynamic Names

If you need to construct variable names dynamically, use indirect expansion (`${!ref}`) or `declare` to create variables with computed names.

```bash
# Dynamic variable names with indirect expansion
prefix="MY"
suffix="VAR"
ref="${prefix}_${suffix}"
declare "$ref=hello"
echo "${!ref}"  # Output: hello

# Using eval (use cautiously)
name="dynamic_var"
eval "${name}='dynamic value'"
echo "${!name}" 
```

## Prevention Tips

- Variable names: letters, digits, underscores only; must start with a letter or `_`
- Use `snake_case` or `UPPER_SNAKE_CASE` for consistency
- Run `bash -n script.sh` to catch invalid variable names early

## Related Errors

- [Invalid Option]({< relref "/languages/bash/invalid-option" >})
- [Readonly Variable]({< relref "/languages/bash/readonly-variable" >})
