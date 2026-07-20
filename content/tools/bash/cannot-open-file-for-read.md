---
title: "[Solution] Cannot Open File for Reading"
description: "Resolve 'cannot open file for reading' errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Cannot Open File for Reading

The file specified for input redirection or command argument cannot be opened.

### Common Causes
- File does not exist.
- Insufficient read permissions.
- File is actually a directory.
- Too many open files.

### How to Fix
```bash
# Check file existence and type
[[ -f "$file" ]] && [[ -r "$file" ]] && cat "$file"

# Check if it's a directory
[[ -d "$file" ]] && echo "It's a directory"

# Use descriptive error messages
if [[ ! -r "$file" ]]; then
    echo "Cannot read: $file" >&2
    exit 1
fi
```

### Example
```bash
# Broken
while IFS= read -r line; do
    echo "$line"
done < "$missing_file"

# Fixed
if [[ -r "$file" ]]; then
    while IFS= read -r line; do
        echo "$line"
    done < "$file"
fi
```
