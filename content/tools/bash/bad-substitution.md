---
title: "[Solution] Bad Substitution Error"
description: "Resolve 'bad substitution' error in Bash variable expansion."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Bad Substitution Error

The shell cannot parse the variable substitution syntax used.

### Common Causes
- Using `${var/pattern/replacement}` in `sh` instead of `bash`.
- Incorrect brace placement or unbalanced braces.
- Using Bash-specific syntax in a POSIX shell.

### How to Fix
```bash
# Ensure script uses bash shebang
#!/bin/bash

# Use ${var%pattern} not ${var(pattern)}
echo "${filename%.log}"

# Validate syntax
bash -n script.sh
```

### Example
```bash
# Broken (sh mode)
#!/bin/sh
echo "${PATH//:/:\n}"

# Fixed (bash mode)
#!/bin/bash
echo "${PATH//:/$'\n'}"
```
