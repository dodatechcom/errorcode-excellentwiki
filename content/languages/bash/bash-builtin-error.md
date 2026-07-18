---
title: "[Solution] Bash Builtin Not A Shell Builtin Error Fix"
description: "Fix 'builtin: not a shell builtin' in Bash. Resolve builtin command errors when calling shell built-in functions incorrectly."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Bash Builtin Not A Shell Builtin Error Fix

The `builtin: not a shell builtin` error occurs when you try to call `builtin` with a command that is not a shell built-in function.

## What This Error Means

The `builtin` command explicitly calls a shell built-in, bypassing any external command with the same name. When the specified command is not a built-in, Bash reports this error.

A typical error:

```
bash: builtin: ls: not a shell builtin
```

## Why It Happens

Common causes include:

- **Calling builtin with external commands** — `builtin ls`, `builtin grep`, etc.
- **Wrong command name** — Typo or incorrect built-in name.
- **Using builtin in non-Bash shells** — `sh` and `dash` may not support `builtin`.
- **Function overriding a built-in** — A function shadows a built-in name.

## How to Fix It

### Fix 1: Only use builtin with actual built-ins

```bash
# WRONG: ls is not a builtin
builtin ls -la

# RIGHT: Use builtin only with built-in commands
builtin echo "This is a builtin"
builtin cd /tmp
builtin source script.sh
builtin read -p "Enter: " input
```

### Fix 2: List available builtins

```bash
# RIGHT: Check what builtins exist
compgen -b

# Common bash builtins
# echo, printf, read, cd, pwd, export, unset, type, which,
# alias, unalias, history, fc, eval, exec, builtin, enable
```

### Fix 3: Use command -p to find external commands

```bash
# RIGHT: Use 'command' for external commands
command ls -la
command grep "pattern" file.txt

# Use 'builtin' only when you need to bypass a function
my_echo() {
    builtin echo "$@"
}
```

### Fix 4: Override functions safely

```bash
# RIGHT: Override cd with custom behavior
cd() {
    builtin cd "$@" || return
    echo "Now in: $(pwd)"
}

# RIGHT: Override echo using builtin
echo() {
    builtin echo "[$(date +%H:%M:%S)] $*"
}
```

### Fix 5: Use enable to manage builtins

```bash
# Disable an external override
enable -n echo  # Use /bin/echo instead of builtin

# Re-enable builtin
enable echo

# List enabled builtins
enable
```

## Common Mistakes

- **Using `builtin` with external commands** — It is exclusively for shell built-ins.
- **Assuming all commands are builtins** — Most useful commands (ls, grep, find) are external.
- **Using builtin for performance** — Builtin is for semantic correctness, not speed.

## Related Pages

- [Bash Exec Error](bash-exec-error) — Command execution issues
- [Bash Source Error](bash-source-error) — Script loading issues
- [Bash Recursive Descent](bash-recursive-descent) — Stack overflow issues
