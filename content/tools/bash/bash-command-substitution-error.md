---
title: "[Solution] Bash Command Substitution Error"
description: "Fix Bash command substitution errors when backticks or $() syntax produce unexpected results."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Nested backticks not escaped properly
- Unquoted command substitution splits on whitespace
- Command inside substitution fails silently
- Newlines or special characters not handled
- Using backticks instead of modern $() syntax

## How to Fix

- Use $() syntax instead of backticks for clarity and nesting
- Quote the substitution to preserve word splitting
- Check exit status of commands inside substitution

## Examples

```bash
#!/bin/bash

# Unquoted - word splitting occurs
files=$(ls)
echo "$files"

# Nested substitution (old style - hard to read)
# output=`cat \`find . -name "*.log"\``

# Modern style with $()
output=$(cat "$(find . -name '*.log')")

# Capture exit status
if result=$(grep -r "error" /var/log); then
    echo "Found: $result"
else
    echo "No matches or grep failed"
fi
```
