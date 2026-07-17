---
title: "[Solution] Linux 'Too many open files' — EMFILE Fix"
description: "Fix Linux 'Too many open files' (EMFILE) errors. Increase file descriptor limits, fix file leaks, and tune system-wide settings."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Linux: Too many open files (EMFILE)

The `Too many open files` error (EMFILE) means a process has reached the maximum number of file descriptors it's allowed to have open simultaneously. In Linux, file descriptors represent open files, sockets, pipes, and other I/O resources. When the limit is reached, the system refuses to open any new files or connections until existing ones are closed.

## Common Causes

- Application has a file descriptor leak (opens files but never closes them)
- File descriptor limits are set too low for the workload
- High-traffic web server or proxy with many concurrent connections
- Database with too many concurrent queries
- System-wide file descriptor limit reached

## How to Fix

### 1. Check Current Limits

```bash
# Check the soft limit for the current session
ulimit -n

# Check the hard limit
ulimit -Hn

# Check limits for a specific process
cat /proc/$(pgrep -f "process-name")/limits | grep "open files"

# Check system-wide file descriptor usage
cat /proc/sys/fs/file-nr
```

Example output:

```
# file-nr: allocated  allocated_handles  max_handles
1024                512               65536
```

### 2. Increase Limits Temporarily

```bash
# Set soft limit to 65535 for the current session
ulimit -n 65535

# Increase hard limit (must be <= hard limit)
ulimit -n 65535 -H
```

### 3. Increase Limits Permanently

Edit `/etc/security/limits.conf`:

```bash
sudo nano /etc/security/limits.conf
```

Add these lines:

```
*    soft    nofile    65535
*    hard    nofile    65535
root soft    nofile    65535
root hard    nofile    65535
```

For systemd services, also set the limit in the service file:

```bash
sudo systemctl edit myservice.service
```

```ini
[Service]
LimitNOFILE=65535
```

### 4. Increase System-Wide Limits

```bash
# Check current system-wide maximum
cat /proc/sys/fs/file-max

# Increase to 2 million
sudo sysctl -w fs.file-max=2000000

# Make persistent
echo "fs.file-max=2000000" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

### 5. Find the Process with Most Open Files

```bash
# Find processes with many open files
for pid in $(ls /proc | grep -E '^[0-9]+$'); do
  count=$(ls /proc/$pid/fd 2>/dev/null | wc -l)
  if [ "$count" -gt 100 ]; then
    echo "$count $(cat /proc/$pid/comm 2>/dev/null) [PID $pid]"
  fi
done | sort -rn | head -20

# Or use lsof
sudo lsof | wc -l
sudo lsof -p $(pgrep -f "process-name") | wc -l
```

### 6. Fix File Descriptor Leaks

Check if the application has a leak by monitoring open file count over time:

```bash
# Monitor file descriptor count for a process
watch -n 1 "ls /proc/$(pgrep myapp)/fd | wc -l"
```

If the count keeps growing, the application is leaking file descriptors and needs to be fixed at the source code level.

### 7. Check for Zombie/Orphan Processes

Zombie processes hold onto file descriptors:

```bash
# Find zombie processes
ps aux | grep -w Z

# Kill parent of zombie process
sudo kill -9 $(ps -o ppid= -p $(pgrep -x Z))
```

## Examples

```bash
$ ulimit -n
1024

$ python3 -c "
import socket
for i in range(2000):
    s = socket.socket()
    s.connect(('localhost', 80))
"
OSError: [Errno 24] Too many open files

$ ulimit -n 65535
# Run again — works
```

## Related Errors

- [Out of memory / OOM killer]({{< relref "/os/linux/oom-killer" >}}) — Process killed by OOM
- [Cannot allocate memory]({{< relref "/os/linux/cannot-allocate-memory" >}}) — Memory allocation failure
- [Connection refused]({{< relref "/os/linux/connection-refused7" >}}) — Service not accepting connections
