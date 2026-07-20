---
title: "[Solution] Bash Bad Substitution Error"
description: "Fix 'bash: bad substitution' when using invalid variable expansion or parameter expansion syntax."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "variables", "substitution", "parameter-expansion", "syntax"]
severity: "error"
---

# Variable Substitution Error

## Error Message

```
bash: bad substitution
```

## Common Causes

- Using `${var/pattern/replacement}` with invalid pattern syntax
- Mixing `$` and `${}` syntax incorrectly
- Using Bash-specific parameter expansion in a POSIX sh script
- Missing closing `}` in variable expansion (e.g., `${var` instead of `${var}`)

## Solutions

### Solution 1: Use Correct Parameter Expansion Syntax

Ensure all variable expansions are properly closed with `}` and use the correct operator for the intended operation.

```bash
# Wrong — missing closing brace
echo "${MY_VAR"

# Right
echo "${MY_VAR}"

# Wrong — mixing $ and ${} incorrectly
echo "$MY_VAR/word}"  # stray } in output

# Right — use ${} consistently
echo "${MY_VAR}/word"

# Substring extraction
str="Hello, World!"
echo "${str:0:5}"    # Output: Hello
echo "${str:7}"      # Output: World! 
```

### Solution 2: Check That You're Using Bash (Not sh) for Advanced Expansions

Advanced parameter expansion like `${var//pattern/replacement}` requires Bash. If your script starts with `#!/bin/sh`, Bash-specific features won't work.

```bash
#!/bin/bash
# This script must use Bash for advanced parameter expansion

str="Hello, World"

# Pattern substitution
echo "${str/World/Bash}"   # Output: Hello, Bash

# Global substitution
path="/usr/local/bin"
echo "${path//\//_}"       # Output: _usr_local_bin

# Check which shell is running
echo "Shell: $SHELL"
echo "BASH_VERSION: ${BASH_VERSION:-not bash}" 
```

## Prevention Tips

- Always close `${}` expansions — count your braces
- Use `#!/bin/bash` for scripts using Bash-specific parameter expansion
- Run `bash -n script.sh` to check for substitution syntax errors

## Related Errors

- [Parameter Expansion Error]({< relref "/languages/bash/parameter-expansion" >})
- [Default Value Error]({< relref "/languages/bash/default-value-error" >})
