---
title: "[Solution] Bash While Read Error"
description: "Fix Bash while read loop errors when reading from files or stdin produces unexpected behavior."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Bash While Read Error

Bash while read loop reads empty lines, skips data, or produces unexpected results.

```
while read: command not found
read: line 5: syntax error
```

## Common Causes

- Missing -r flag causing backslash interpretation
- Pipe creates subshell losing variable changes
- File has Windows line endings (CRLF)
- IFS not set correctly for parsing
- read not reading from correct file descriptor

## How to Fix

### Use -r Flag and Redirect

```bash
# Wrong - pipe creates subshell, -r missing
cat file.txt | while read line; do
    count=$((count + 1))
done
echo "$count"  # Always 0

# Correct
count=0
while IFS= read -r line; do
    ((count++))
done < file.txt
echo "$count"
```

### Handle Windows Line Endings

```bash
# Convert CRLF to LF first
while IFS= read -r line; do
    line="${line%$'\r'}"
    echo "$line"
done < windows_file.txt
```

### Read Fields Correctly

```bash
# Parse CSV
while IFS=',' read -r name email role; do
    echo "Name: $name, Email: $email, Role: $role"
done < users.csv
```

### Read with Timeout

```bash
# Read from stdin with timeout
if read -t 5 -r input; then
    echo "Got: $input"
else
    echo "No input within 5 seconds"
fi
```

### Read Multiple Lines at Once

```bash
# Read pairs of lines
while IFS= read -r key && IFS= read -r value; do
    echo "$key = $value"
done < config.txt
```

## Examples

```bash
#!/bin/bash
# Process file safely
if [[ ! -f "$1" ]]; then
    echo "File not found: $1" >&2
    exit 1
fi

line_num=0
while IFS= read -r line; do
    ((line_num++))
    # Skip empty lines and comments
    [[ -z "$line" || "$line" == \#* ]] && continue
    echo "Line $line_num: $line"
done < "$1"
```
