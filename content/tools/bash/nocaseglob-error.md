---
title: "[Solution] Nocaseglob Pattern Error"
description: "Fix nocaseglob case-insensitive globbing errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Nocaseglob Pattern Error

With `nocaseglob`, pattern matching in globs is case-insensitive.

### Common Causes
- `shopt -s nocaseglob` makes `*.TXT` match `file.txt`.
- Unexpected file matches due to case-insensitive behavior.

### How to Fix
```bash
# Enable case-insensitive globbing
shopt -s nocaseglob
echo *.txt    # matches .TXT, .Txt, .txt

# Disable for case-sensitive matching
shopt -u nocaseglob
echo *.txt    # only matches .txt

# Check status
shopt nocaseglob
```

### Example
```bash
# Broken (nocaseglob on, matches unexpected files)
shopt -s nocaseglob
rm *.txt    # removes .TXT files too

# Fixed
shopt -u nocaseglob
rm *.txt    # only removes .txt
```
