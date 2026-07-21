---
title: "[Solution] Bash String Comparison Error"
description: "Fix Bash string comparison errors when comparing strings using incorrect operators."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# Bash String Comparison Error

Bash string comparison produces unexpected results due to incorrect operator usage.

```
bash: [: ==: unary operator expected
```

## Common Causes

- Using = instead of == inside [[ ]]
- Using == instead of = inside [ ]
- Unquoted variables causing word splitting
- Comparing empty variables without quotes
- Mixing integer and string comparisons

## How to Fix

### Use Correct Comparison Syntax

```bash
# Inside [[ ]] - use ==
if [[ "$str1" == "$str2" ]]; then
    echo "Equal"
fi

# Inside [ ] - use =
if [ "$str1" = "$str2" ]; then
    echo "Equal"
fi
```

### Always Quote Variables

```bash
# Wrong - empty variable causes syntax error
if [ $name = "admin" ]; then

# Correct
if [[ "$name" == "admin" ]]; then
```

### Use Pattern Matching

```bash
# Match pattern
if [[ "$filename" == *.log ]]; then
    echo "Log file"
fi

# Regex matching
if [[ "$email" =~ ^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$ ]]; then
    echo "Valid email"
fi
```

### Compare with Default Values

```bash
# Check if variable is set and non-empty
if [[ -n "${MY_VAR:-}" ]]; then
    echo "Variable is set"
fi

# Use default if empty
value="${MY_VAR:-default}"
```

## Examples

```bash
#!/bin/bash
str1="hello"
str2="Hello"

# Case-sensitive
if [[ "$str1" != "$str2" ]]; then
    echo "Strings are different"
fi

# Case-insensitive
if [[ "${str1,,}" == "${str2,,}" ]]; then
    echo "Case-insensitive match"
fi

# Check string contains substring
if [[ "$str1" == *ell* ]]; then
    echo "Contains 'ell'"
fi
```
