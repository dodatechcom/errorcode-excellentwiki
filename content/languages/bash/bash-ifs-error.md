---
title: "[Solution] Bash IFS Error -- Incorrect Field Splitting"
description: "Fix bash IFS errors when the Internal Field Separator is modified and causes unexpected word splitting."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash IFS Error

This error occurs when the Internal Field Separator (IFS) is modified and causes unexpected word splitting behavior.

## Common Causes

- Changing IFS without restoring it
- IFS not set to expected delimiter for read
- Empty IFS causing entire line to be one field
- Forgetting that IFS affects word splitting globally

## How to Fix

### Save and restore IFS

```bash
# WRONG: IFS changed permanently
IFS=','
read -r name age <<< "Alice,30"
# IFS still set to comma

# CORRECT: save and restore
OLD_IFS="$IFS"
IFS=','
read -r name age <<< "Alice,30"
IFS="$OLD_IFS"
```

### Use local IFS in functions

```bash
parse_csv() {
    local IFS=','
    read -r field1 field2 field3 <<< "$1"
}
```

## Examples

```bash
#!/bin/bash
# Parse CSV safely
while IFS=, read -r name age email; do
    echo "Name: $name, Age: $age, Email: $email"
done < data.csv
```
