---
title: "[Solution] Bash Pipe Failure Error"
description: "Fix pipe failures in Bash when commands in a pipeline don't succeed as expected."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["pipe-failure", "pipefail", "pipeline"]
weight: 5
---

# Bash Pipe Failure Error Fix

This error occurs when a command in a pipeline fails and the failure isn't properly detected or handled.

## Description

By default, Bash only returns the exit status of the **last** command in a pipeline. If an earlier command fails but the last succeeds, the pipeline reports success. The `set -o pipefail` option changes this so the pipeline returns the status of the last failing command.

## Common Causes

- **Missing `pipefail` option** — earlier pipeline failures are silently ignored.
- **Not checking pipeline status** — script continues after pipeline errors.
- **Mid-pipeline command failure** — e.g., `grep` finds nothing but `sort` succeeds.
- **SIGPIPE** — a process closes its end of a pipe early, causing writes to fail.

## How to Fix

### Fix 1: Enable pipefail globally

```bash
#!/bin/bash
set -o pipefail

# Now any failure in the pipeline causes the whole pipeline to fail
cat file.txt | grep "pattern" | sort
```

### Fix 2: Check pipeline status explicitly

```bash
result=$(cat file.txt | grep "pattern" | wc -l)
if [[ ${PIPESTATUS[@]} -ne 0 ]]; then
    echo "Pipeline failed"
fi
```

### Fix 3: Use PIPESTATUS to check individual commands

```bash
cat file.txt | grep "pattern" | sort
echo "grep exit: ${PIPESTATUS[1]}"
```

### Fix 4: Handle SIGPIPE gracefully

```bash
# Use true to ignore SIGPIPE (exit 141)
head -n 10 large_file || true
```

## Examples

```bash
$ set -o pipefail
$ false | true
$ echo $?
1
# With pipefail, the failure of `false` propagates

$ cat nonexistent | sort
cat: nonexistent: No such file or directory
# Without pipefail, sort succeeds and $? is 0

$ cmd1 | cmd2 | cmd3
echo "${PIPESTATUS[@]}"
# Shows exit status of each command in the pipeline
```

## Related Errors

- [Exit Status](exit-status) — general exit status code reference.
- [Return Code](return-code) — handling return values from functions.
- [Signal Trap](signal-trap) — handling SIGPIPE and other signals.
