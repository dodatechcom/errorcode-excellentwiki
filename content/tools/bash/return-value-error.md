---
title: "[Solution] Bash Return Value Error"
description: "Fix Bash return value errors when functions or commands return unexpected success or failure codes."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Bash Return Value Error

Bash functions or commands return unexpected values that break script logic.

```
Expected exit code 0, got 1
```

## Common Causes

- Function uses return with value > 255
- Missing return statement in function
- Last command in function implicitly becomes return value
- Incorrect use of exit vs return
- Arithmetic overflow in return value

## How to Fix

### Use Return for Status, Variables for Data

```bash
# Wrong - trying to return data from function
get_value() {
    return 42  # This is the exit code, not data
}

# Correct - use echo for data, return for status
get_value() {
    echo 42
    return 0
}
result=$(get_value)
```

### Use Global/Associative Arrays for Multiple Returns

```bash
declare -gA RESULTS

fetch_data() {
    RESULTS[name]="example"
    RESULTS[code]=0
    RESULTS[output]="data here"
    return 0
}

fetch_data
echo "Name: ${RESULTS[name]}"
echo "Code: ${RESULTS[code]}"
```

### Limit Return Values to 0-255

```bash
# Wrong - return value must be 0-255
my_func() {
    return 300  # Will wrap to 44
}

# Correct - use exit for larger values
my_func() {
    exit 300  # Only use in main script
}
```

### Check Return Values Explicitly

```bash
#!/bin/bash
set -e

my_func || {
    echo "Function failed with code $?" >&2
    # Handle error
}
```

## Examples

```bash
# Safe function with error handling
safe_divide() {
    local dividend=$1
    local divisor=$2

    if [[ $divisor -eq 0 ]]; then
        echo "Error: division by zero" >&2
        return 1
    fi

    echo $(( dividend / divisor ))
    return 0
}

result=$(safe_divide 10 2) || exit 1
echo "Result: $result"
```
