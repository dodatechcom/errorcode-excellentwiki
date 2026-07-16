---
title: "[Solution] Bash Command Not Found Error Fix"
description: "Fix 'bash: X: command not found' when a command or program is not installed or not in your PATH."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["command-not-found", "path", "installation"]
weight: 5
---

# Bash Command Not Found Error Fix

This error occurs when Bash cannot locate the command you typed. The shell searches the directories listed in your `PATH` environment variable and fails to find an executable matching the name.

## Description

Bash searches `PATH` directories in order and runs the first match it finds. If no match exists, it prints `bash: X: command not found`. This can happen even if the program is installed, if it's not in a directory covered by `PATH`.

## Common Causes

- **Program not installed** — the command simply doesn't exist on the system.
- **Not in PATH** — the program is installed but its directory isn't in `PATH`.
- **Typo in command name** — misspelling of a valid command.
- **Using Windows-style path** — running `.\script.sh` instead of `./script.sh`.

## How to Fix

### Fix 1: Check if the program is installed

```bash
which command-name
# or
type command-name
```

If neither returns a path, install the program using your package manager (e.g., `apt`, `yum`, `brew`).

### Fix 2: Add the directory to PATH

```bash
# Temporarily add to PATH for the current session
export PATH=$PATH:/path/to/program/directory

# Permanently add to ~/.bashrc or ~/.profile
echo 'export PATH=$PATH:/path/to/program/directory' >> ~/.bashrc
source ~/.bashrc
```

### Fix 3: Use the full path to the command

```bash
# Instead of
myscript.sh

# Use the full path
/home/user/scripts/myscript.sh
# Or relative path with ./
./myscript.sh
```

### Fix 4: Fix a typo

```bash
# Wrong
git stauts

# Correct
git status
```

## Examples

```bash
$ docker ps
bash: docker: command not found

$ kubectl get pods
bash: kubectl: command not found

$ ./deploy.sh
bash: ./deploy.sh: No such file or directory
```

## Related Errors

- [Permission Denied](permission-denied) — command exists but lacks execute permission.
