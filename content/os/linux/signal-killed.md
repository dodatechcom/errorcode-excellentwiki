---
title: "[Solution] Linux: signal-killed — process killed by signal"
description: "Fix Linux signal-killed errors. process killed by signal with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["process-error"]
weight: 8
---
# Linux: Process Killed by Signal

A process killed by signal means the kernel sent a signal (SIGKILL, SIGTERM, SIGHUP, etc.) to terminate a process.

## Common Causes

- OOM (Out-of-Memory) killer terminated the process (SIGKILL)
- System administrator or monitoring system sent SIGTERM/SIGKILL
- Process reached resource limits (cgroup memory limit)
- Shell job control (Ctrl+C sends SIGINT)
- Parent process termination sending SIGHUP to child

## How to Fix

### 1. Check Which Signal Killed the Process

```bash
# Check exit status
./myprogram
echo $?  # 137 = SIGKILL, 143 = SIGTERM, 130 = SIGINT
```

### 2. Check for OOM Killer

```bash
dmesg | grep -i "killed process\|oom"
journalctl -k | grep -i oom
```

### 3. Check System Logs

```bash
journalctl -xe -n 50
sudo tail -100 /var/log/syslog
```

### 4. Check Cgroup Memory Limits

```bash
# Check cgroup memory limit
cat /sys/fs/cgroup/memory/memory.limit_in_bytes
cat /sys/fs/cgroup/system.slice/<service>.service/memory.current
```

### 5. Increase Memory or Adjust Limits

```bash
# For systemd service
sudo systemctl edit <service>
# Add:
# [Service]
# MemoryMax=2G
```

## Examples

```bash
$ ./myapp
Killed

$ dmesg | grep -i "killed process"
[12345.678] Killed process 12345 (myapp) total-vm:1234567kB, anon-rss:987654kB, file-rss:0kB

$ echo $?
137  # Process was killed by SIGKILL (OOM)
```
