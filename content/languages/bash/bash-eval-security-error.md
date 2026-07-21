---
title: "[Solution] Bash Eval Security Error -- Unsafe Command Evaluation"
description: "Fix bash eval security errors when using eval with untrusted input."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Eval Security Error

This error occurs when `eval` is used with untrusted or unsanitized input, leading to code injection vulnerabilities.

## Common Causes

- Using `eval` with user-provided input
- Variable expansion inside eval creating command injection
- Eval executing unintended commands
- Indirect variable references where eval is overkill

## How to Fix

### Avoid eval when possible

```bash
# WRONG: eval with user input
varname="user_input"
eval "value=\$$varname"  # potential injection

# CORRECT: use indirect reference
value="${!varname}"
```

### Sanitize input if eval is necessary

```bash
# If you must use eval
sanitize_input() {
    echo "$1" | tr -cd '[:alnum:]_-'
}

eval "$(sanitize_input "$user_input")"
```

## Examples

```bash
# Safe indirect variable access
declare -A config
config[debug]="true"

key="debug"
echo "${!key}"  # "true" -- no eval needed
```
