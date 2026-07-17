---
title: "[Solution] Bash Builtin: Command Not Found Error Fix"
description: "Fix bash builtin command not found errors when built-in commands are missing or disabled."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Bash Builtin: Command Not Found Error Fix

A bash builtin error occurs when a shell built-in command is disabled or unavailable, or when the name conflicts with an external command.

## What This Error Means

Bash built-in commands (like `cd`, `echo`, `type`, `enable`) are part of the shell itself. They can be disabled with `enable -n`, and if disabled, bash may look for an external command instead. Some builtins may also be missing in minimal shells.

## Common Causes

- Built-in command disabled with `enable -n`
- Running in a minimal shell (like dash) that lacks some builtins
- PATH overwritten and builtins shadowed
- Custom function shadows a builtin name

## How to Fix

### 1. Re-enable disabled builtins

```bash
# WRONG: Builtin disabled
enable -n echo
echo "Hello"  # May not work as expected

# CORRECT: Re-enable
enable echo
echo "Hello"
```

### 2. Check if a command is builtin

```bash
# CORRECT: Verify builtin status
type cd
# cd is a shell builtin

type -a echo
# echo is /usr/bin/echo
# echo is a shell builtin
```

### 3. Use builtin explicitly

```bash
# CORRECT: Force builtin usage
builtin echo "Using builtin"
builtin cd /tmp
```

### 4. List all builtins

```bash
# CORRECT: See all available builtins
enable

# Check if specific builtin exists
enable | grep -w "echo"
```

## Related Errors

- [Command Not Found](command-not-found) — missing commands
- [No Such File](no-such-file) — missing files
- [Permission Denied](permission-denied) — access errors
