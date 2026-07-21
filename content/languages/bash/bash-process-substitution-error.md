---
title: "[Solution] Bash Process Substitution Error -- Incorrect <() Usage"
description: "Fix bash process substitution errors when using <() or >() syntax incorrectly."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Bash Process Substitution Error

This error occurs when process substitution `<()` or `>()` is used incorrectly or with incompatible commands.

## Common Causes

- Using process substitution with commands expecting file arguments
- Process substitution not available in POSIX sh
- File descriptor leaks from process substitution
- Missing closing parenthesis

## How to Fix

### Use correct syntax

```bash
# WRONG: process substitution in non-bash
#!/bin/sh
diff <(ls dir1) <(ls dir2)  # not POSIX

# CORRECT: use in bash
#!/bin/bash
diff <(ls dir1) <(ls dir2)
```

### Use for command comparison

```bash
# Compare command outputs
diff <(sort file1) <(sort file2)

# Feed multiple commands
cat <(echo "Header") <(grep pattern file)
```

## Examples

```bash
#!/bin/bash
# Sort by second column
awk '{print $2, $0}' data.txt | sort | awk '{print $2}'

# Or with process substitution
sort -k2 <(awk '{print $2, $0}' data.txt) | cut -d' ' -f2-
```
