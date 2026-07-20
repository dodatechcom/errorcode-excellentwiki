---
title: "[Solution] Bash Indirect Expansion Error"
description: "Fix 'bash: indirect expansion error' when using `${!ref}` or nameref variables incorrectly."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "variables", "indirect-expansion", "nameref", "indirection"]
severity: "error"
---

# Indirect Reference Error

## Error Message

```
bash: indirect expansion error
```

## Common Causes

- Using `${!variable}` when the variable doesn't contain a valid variable name
- Using `declare -n` (nameref) with a variable that conflicts with the nameref itself
- Referencing a nameref that points to an unset variable
- Using indirect expansion in a POSIX sh script (not supported)

## Solutions

### Solution 1: Ensure the Referenced Variable Name is Valid

Indirect expansion `${!ref}` expects `ref` to contain the name of another variable. Make sure `ref` holds a valid variable name.

```bash
#!/bin/bash

# Variable containing a variable name
myvar="Hello, World"
ref="myvar"

# Right — indirect expansion works
echo "${!ref}"  # Output: Hello, World

# Wrong — ref doesn't contain a valid variable name
ref="123invalid"
echo "${!ref}"  # Error: indirect expansion error

# Right — use valid variable names
ref="myvar"
echo "${!ref}"  # Output: Hello, World 
```

### Solution 2: Use declare -n Namerefs (Bash 4.3+)

Namerefs provide a cleaner way to create indirect references. Define the nameref with `declare -n` and it automatically dereferences.

```bash
#!/bin/bash

# Create a variable
greeting="Hello"

# Create a nameref pointing to greeting
declare -n ref=greeting
echo "$ref"  # Output: Hello

# Modify through the nameref
ref="World"
echo "$greeting"  # Output: World

# Use in functions for flexible variable assignment
set_value() {
    local -n result_ref="$1"
    result_ref="$2"
}

set_value myvar "test value"
echo "$myvar"  # Output: test value 
```

## Prevention Tips

- Ensure `${!ref}` references a valid, existing variable name
- Use `declare -n` for clean indirect references (Bash 4.3+)
- Avoid circular nameref chains which cause undefined behavior

## Related Errors

- [Parameter Expansion Error]({< relref "/languages/bash/parameter-expansion" >})
- [Array Error]({< relref "/languages/bash/array-error" >})
