---
title: "[Solution] Bash Pipe Error"
description: "Fix bash pipe errors when commands in a pipeline fail, return unexpected exit codes, or cause 'Broken pipe' errors."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["pipe", "pipeline", "broken-pipe", "exit-code", "signal"]
weight: 5
---

# Bash Pipe Error Fix

Pipe errors include "Broken pipe" (SIGPIPE), commands in a pipeline returning non-zero exit codes, or pipe output not reaching the next command.

## What This Error Means

A pipe connects stdout of one command to stdin of another. SIGPIPE occurs when a process writes to a pipe whose read end has closed (e.g., `head` closes early). Pipeline errors also occur when individual commands fail.

## Common Causes

- Downstream command exits before upstream finishes (SIGPIPE)
- `set -o pipefail` catching failures in pipeline stages
- Pipe buffer overflow with heavy output
- Command producing no output when next command expects input

## How to Fix

### 1. Handle SIGPIPE gracefully

```bash
# Suppress SIGPIPE errors
set +o pipefail

# Or handle SIGPIPE explicitly
trap '' PIPE
echo "data" | head -1  # No error even though head closes pipe
trap - PIPE
```

### 2. Use pipefail to find failing command

```bash
set -o pipefail
cmd1 | cmd2 | cmd3
echo "Pipeline exit code: $?"
# Shows which command in the pipeline failed
```

### 3. Use process substitution instead of pipes

```bash
# Pipe: may cause SIGPIPE
diff <(sort file1) <(sort file2)

# Safer than:
sort file1 | sort file2 | diff - file3
```

### 4. Check for empty pipe input

```bash
# Ensure upstream produces output
command_that_may_fail | next_command

# Safer:
command_that_may_fail | { read -r line; [ -n "$line" ] && process "$line"; }
```

## Related Errors

- [Process Substitution](bash-process-substitution) — `<()` and `>()` errors
- [Return Code](return-code) — exit status handling
