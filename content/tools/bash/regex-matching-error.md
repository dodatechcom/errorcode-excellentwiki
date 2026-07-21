---
title: "[Solution] Bash Regex Matching Error"
description: "Fix Bash regex matching errors when using =~ operator with incorrect or unquoted patterns."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# Bash Regex Matching Error

Bash regex matching with the =~ operator fails or produces unexpected results.

```
bash: =~: command not found
```

## Common Causes

- Using =~ in [ ] instead of [[ ]]
- Pattern stored in variable without proper quoting
- Regex pattern contains special characters
- Using bash version < 3.0
- Missing capture group handling

## How to Fix

### Use [[ ]] for Regex Matching

```bash
# Wrong - [ ] does not support =~
if [ "$input" =~ ^[0-9]+$ ]; then

# Correct
if [[ "$input" =~ ^[0-9]+$ ]]; then
    echo "Numeric input"
fi
```

### Store Pattern in Variable

```bash
# Correct - store pattern in variable
pattern='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if [[ "$email" =~ $pattern ]]; then
    echo "Valid email"
fi
```

### Use Capture Groups

```bash
if [[ "$input" =~ ([0-9]+)-([0-9]+) ]]; then
    start="${BASH_REMATCH[1]}"
    end="${BASH_REMATCH[2]}"
    echo "Range: $start to $end"
fi
```

### Escape Special Characters

```bash
# Escape dots and other special chars
if [[ "$input" =~ ^[0-9]+\.[0-9]+$ ]]; then
    echo "Valid decimal number"
fi
```

## Examples

```bash
#!/bin/bash
# Common regex patterns
validate_ip() {
    local ip=$1
    local pattern='^([0-9]{1,3}\.){3}[0-9]{1,3}$'
    if [[ "$ip" =~ $pattern ]]; then
        echo "Valid IP format"
    else
        echo "Invalid IP"
        return 1
    fi
}

validate_ip "192.168.1.1"
validate_ip "999.999.999.999"
```
