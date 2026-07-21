---
title: "[Solution] Bash Read Line Error -- Incorrect Input Parsing"
description: "Fix bash read errors when parsing input lines with incorrect delimiter or variable assignment."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Read Line Error

This error occurs when `read` is used incorrectly, such as wrong IFS or not handling EOF properly.

## Common Causes

- `read` returns non-zero at EOF, causing issues with `while read`
- IFS not set correctly for multi-field input
- Using `read` without `-r` flag, interpreting backslashes
- Not quoting variable in `while read` causing word splitting

## How to Fix

### Use correct while read pattern

```bash
# WRONG: missing -r and quotes
while read line; do
    echo $line
done < file.txt

# CORRECT: -r flag and proper quoting
while IFS= read -r line; do
    echo "$line"
done < file.txt
```

### Parse multi-field input

```bash
while IFS=: read -r user _ uid _; do
    if [ "$uid" -ge 1000 ]; then
        echo "User: $user (UID: $uid)"
    fi
done < /etc/passwd
```

## Examples

```bash
#!/bin/bash
while IFS=, read -r name age city; do
    echo "Name: $name, Age: $age, City: $city"
done <<EOF
Alice,30,New York
Bob,25,San Francisco
Charlie,35,Chicago
EOF
```
