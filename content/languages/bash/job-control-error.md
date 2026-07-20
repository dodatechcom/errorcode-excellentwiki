---
title: "[Solution] Bash Job Control Not Enabled Error"
description: "Fix 'bash: job control not enabled' when background jobs and job control don't work as expected."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "command", "job-control", "background", "signals", "interactive"]
severity: "error"
---

# Job Control Error

## Error Message

```
bash: job control not enabled
```

## Common Causes

- Running a non-interactive script that tries to use job control features
- Using `set -m` (monitor mode) in a non-interactive shell
- Background jobs (`&`) don't work properly in scripts without a terminal
- The shell is running in a non-terminal context (e.g., cron, systemd, Dockerfile RUN)

## Solutions

### Solution 1: Use Alternatives to Job Control in Scripts

Job control (`jobs`, `fg`, `bg`, `disown`) is designed for interactive shells. In scripts, use `&` with PID tracking and `wait` instead.

```bash
#!/bin/bash

# Wrong — job control not available in scripts
set -m
sleep 10 &
jobs  # Won't work in non-interactive shell

# Right — track PIDs manually
sleep 10 &
PID=$!
echo "Started background job: $PID"

# Wait for it to finish
wait $PID
echo "Job finished with status: $?" 
```

### Solution 2: Enable Job Control for Interactive Scripts

If you need job control in a script (e.g., an interactive shell script), enable it explicitly with `set -m`. This only works when the script has a controlling terminal.

```bash
#!/bin/bash

# Enable job control (requires a terminal)
set -m

# Now background jobs work
sleep 5 &
sleep 10 &

# List background jobs
jobs -l

# Bring a job to the foreground
# fg %1

# For scripts run from cron/systemd, use a different approach:
# Instead of job control, use screen/tmux or nohup
nohup long_running_task > output.log 2>&1 & 
```

## Prevention Tips

- Job control features only work in interactive shells with a controlling terminal
- Use `&` with `wait` and PID tracking for background tasks in scripts
- Use `nohup` or `screen`/`tmux` for long-running tasks outside interactive sessions

## Related Errors

- [Broken Pipe]({< relref "/languages/bash/broken-pipe-error" >})
- [Signal Error]({< relref "/languages/bash/signal-error" >})
