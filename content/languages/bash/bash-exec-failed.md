---
title: "[Solution] Bash Exec: Not Found Error Fix"
description: "Fix bash exec command not found errors when trying to replace the current process."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["exec", "process", "replace", "command-not-found", "bash"]
weight: 5
---

# Bash Exec: Not Found Error Fix

A bash exec error occurs when `exec` tries to replace the current process with a command that doesn't exist or can't be found in PATH.

## What This Error Means

The `exec` command replaces the current shell process with the specified command. If the command isn't found, exec fails and the shell may terminate (since it was supposed to be replaced).

## Common Causes

- Command not in PATH
- Typo in command name
- Program not installed
- Using exec in a function (replaces the shell)

## How to Fix

### 1. Verify command exists

```bash
# WRONG: Exec with unknown command
exec nonexistent-command

# CORRECT: Check first
if command -v python3 &>/dev/null; then
    exec python3 "$@"
else
    echo "python3 not found"
    exit 1
fi
```

### 2. Use full path for exec

```bash
# CORRECT: Use absolute path
exec /usr/bin/python3 script.py
```

### 3. Don't use exec in functions

```bash
# WRONG: exec in function replaces the shell
my_func() {
    exec bash  # Replaces current shell!
}

# CORRECT: Use subshell if needed
my_func() {
    ( exec bash )  # Runs in subshell
}
```

### 4. Use exec for redirection (common use)

```bash
# CORRECT: exec for file descriptor manipulation
exec 3> output.txt
echo "This goes to file" >&3
exec 3>&-
```

## Related Errors

- [Command Not Found](command-not-found) — missing commands
- [No Such File](no-such-file) — missing files
- [Permission Denied](permission-denied) — access errors
