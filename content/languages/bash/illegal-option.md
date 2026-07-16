---
title: "[Solution] Bash Illegal Option Error"
description: "Fix 'illegal option' in Bash when an unknown flag or option is passed to a command or script."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["illegal-option", "unknown-flag", "getopts"]
weight: 5
---

# Bash Illegal Option Error Fix

This error occurs when a command or Bash builtin receives an option flag it doesn't recognize.

## Description

Commands and builtins accept specific option flags. When you pass an unsupported option — due to a typo, wrong command, or version mismatch — the command rejects it with "illegal option."

## Common Causes

- **Typo in option flag** — `ls -lal` is fine, but `ls -llal` is not.
- **GNU vs BSD differences** — macOS `grep` doesn't support `-P` (Perl regex).
- **Missing colon in getopts** — `getopts "abc"` vs `getopts "a:bc"`.
- **Using a flag not supported by the command version** — older versions lack newer flags.

## How to Fix

### Fix 1: Check the command's help

```bash
command --help
# or
man command
```

### Fix 2: Verify option syntax

```bash
# Wrong — -r is recursive, but -R is not a valid combo on all systems
ls -Rr /path

# Right
ls -R /path
```

### Fix 3: Handle platform differences in scripts

```bash
# Detect OS for different flag syntax
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS (BSD)
    sed -i '' 's/old/new/g' file
else
    # Linux (GNU)
    sed -i 's/old/new/g' file
fi
```

### Fix 4: Use getopts with proper syntax

```bash
# Wrong — missing colon means 'a' doesn't take an argument
while getopts "abc" opt; do

# Right — 'a:' means 'a' takes an argument
while getopts "a:bc" opt; do
```

## Examples

```bash
$ grep -P "pattern" file
grep: illegal option -- P

$ ls -Z
ls: invalid option -- 'Z'

$ bash -xv script.sh
# If script.sh doesn't have executable permission and you didn't use bash
```

## Related Errors

- [Command Not Found](command-not-found) — the command itself doesn't exist.
- [Permission Denied](permission-denied) — no execute permission on the script.
