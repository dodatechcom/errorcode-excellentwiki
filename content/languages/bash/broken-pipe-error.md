---
title: "[Solution] Bash Broken Pipe Error"
description: "Fix 'bash: broken pipe' when a process in a pipeline closes its input before the writer finishes."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "command", "pipeline", "signal", "pipe", "sigpipe"]
severity: "error"
---

# Broken Pipe

## Error Message

```
bash: echo: write error: Broken pipe
```

## Common Causes

- The receiving end of a pipe closes early (e.g., `head` closes after reading N lines)
- A process terminates before the sender finishes writing
- The `SIGPIPE` signal is delivered to the writing process
- Network pipes or FIFOs have a reader that disconnects

## Solutions

### Solution 1: Handle or Suppress SIGPIPE

The broken pipe error occurs when a reader closes its end of a pipe. You can suppress it with `set -o pipefail` handling or trap the signal.

```bash
#!/bin/bash

# The common case: head closes early
echo -e "line1\nline2\nline3\nline4\nline5" | head -n 2
# line3, line4, line5 cause SIGPIPE to echo — that's expected

# Suppress broken pipe warnings
set +o pipefail

# Or trap SIGPIPE
trap '' PIPE
echo -e "line1\nline2\nline3" | head -n 1 
```

### Solution 2: Use Process Substitution to Avoid Pipes

Replace pipes with process substitution `<(...)` or `>(...)` to avoid the broken pipe scenario entirely.

```bash
#!/bin/bash

# Instead of piping to head, use a while loop
echo -e "line1\nline2\nline3" | while read -r line; do
    echo "$line"
    break  # Process only first line
done

# Use process substitution
diff <(sort file1.txt) <(sort file2.txt)

# For large outputs, write to a temp file instead of piping
large_command > /tmp/output.txt
head -n 10 /tmp/output.txt 
```

## Prevention Tips

- Broken pipes from `head`/`tail` in pipelines are usually harmless
- Use `set +o pipefail` to ignore pipe failures in non-critical scripts
- Use `trap '' PIPE` to suppress SIGPIPE for specific commands

## Related Errors

- [Missing Pipe]({< relref "/languages/bash/missing-pipe" >})
- [Signal Error]({< relref "/languages/bash/signal-error" >})
