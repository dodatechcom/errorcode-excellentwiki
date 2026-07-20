---
title: "[Solution] Bash Fork Cannot Allocate Memory Error"
description: "Fix 'bash: fork: Cannot allocate memory' when the system runs out of resources to create new processes."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "command", "memory", "fork", "resources", "limits"]
severity: "error"
---

# Fork Failed

## Error Message

```
bash: fork: Cannot allocate memory
```

## Common Causes

- System has exhausted available memory (RAM or swap)
- Process limit (ulimit) has been reached
- A fork bomb or runaway process loop consumed system resources
- System is under heavy load from other services or processes

## Solutions

### Solution 1: Free Up System Resources

Check system memory and process limits. Kill unnecessary processes and increase swap if possible.

```bash
# Check memory usage
free -h
top -bn1 | head -20

# Check process count
ps aux | wc -l

# Check ulimit
ulimit -a

# Kill resource-hungry processes
kill -9 <PID>

# Check for fork bombs
ps aux | awk '{print $1}' | sort | uniq -c | sort -rn | head -10 
```

### Solution 2: Increase Process and Memory Limits

If the limits are too restrictive, increase them. Check `/etc/security/limits.conf` or use `ulimit` to raise limits for your session.

```bash
# Check current limits
ulimit -u  # max user processes
ulimit -v  # max virtual memory

# Temporarily increase limits
ulimit -u 4096
ulimit -v unlimited

# Check system-wide limits
cat /proc/sys/kernel/pid-max
cat /proc/sys/fs/file-max

# Increase pid-max if needed (requires root)
sudo sysctl -w kernel.pid_max=65536 
```

## Prevention Tips

- Monitor system resources with `free -h` and `top` regularly
- Set reasonable `ulimit` values to prevent resource exhaustion
- Use `ulimit -v` and `ulimit -u` to control virtual memory and process limits

## Related Errors

- [Permission Denied]({< relref "/languages/bash/permission-denied-error" >})
- [Signal Error]({< relref "/languages/bash/signal-error" >})
