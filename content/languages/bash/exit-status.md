---
title: "[Solution] Bash Exit Status Code Reference"
description: "Understand and handle Bash exit status codes for command success, failure, and custom error handling."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Bash Exit Status Code Reference

Every command in Bash returns an exit status code that indicates success, failure, or a specific error condition.

## Description

Exit status codes are integers between 0 and 255. A status of 0 means success; anything else indicates failure. Bash stores the exit status of the most recent command in `$?`. Understanding these codes is essential for error handling in scripts.

## Common Exit Status Codes

- **0** — success
- **1** — general error or catchall
- **2** — misuse of shell builtins (per Bash documentation)
- **126** — command cannot execute (permission denied or not a binary)
- **127** — command not found
- **128+N** — fatal error signal N (e.g., 130 = SIGINT/Ctrl+C)
- **130** — script terminated by Ctrl+C
- **255** — exit status out of range

## How to Fix

### Fix 1: Check exit status after commands

```bash
if command -v mycommand &>/dev/null; then
    mycommand
    exit_code=$?
    if [[ $exit_code -ne 0 ]]; then
        echo "Command failed with exit code $exit_code"
    fi
else
    echo "Command not found"
    exit 1
fi
```

### Fix 2: Use `set -e` to exit on error

```bash
#!/bin/bash
set -e

# Script exits on first failure
risky_command
another_command
```

### Fix 3: Use `trap` for cleanup on failure

```bash
cleanup() {
    echo "Cleaning up on exit with status $1"
    rm -f /tmp/lockfile
}
trap cleanup EXIT
```

### Fix 4: Return meaningful exit codes in functions

```bash
validate_input() {
    if [[ -z "$1" ]]; then
        echo "Error: empty input" >&2
        return 1
    fi
    return 0
}
```

## Examples

```bash
$ ls /nonexistent
ls: cannot access '/nonexistent': No such file or directory
$ echo $?
2

$ false
$ echo $?
1

$ bash -c 'exit 42'
$ echo $?
42
```

## Related Errors

- [Return Code](return-code) — handling return values from functions.
- [Pipe Failure](pipe-failure) — exit status with piped commands.
