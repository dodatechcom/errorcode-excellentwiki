---
title: "[Solution] Invalid Alias Syntax"
description: "Fix invalid alias syntax errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Invalid Alias Syntax

The alias definition has incorrect syntax.

### Common Causes
- Missing `=` or spaces around it.
- Quoting issues in the replacement string.
- Using aliases in non-interactive shells.

### How to Fix
```bash
# Correct syntax: alias name='command'
alias ll='ls -la'

# For complex commands, use a function instead
mycommand() {
    echo "complex command"
}

# Disable alias expansion in scripts
unalias mycommand 2>/dev/null
set +o alias
```

### Example
```bash
# Broken
alias ll = 'ls -la'

# Fixed
alias ll='ls -la'
```
