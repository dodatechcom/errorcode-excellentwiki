---
title: "[Solution] Linux ESRCH (errno 3) — No Such Process Fix"
description: "Fix Linux ESRCH (errno 3) No Such Process error. Resolve missing PID issues, process lookup failures, and kill/signal errors."
platforms: ["linux"]
severities: ["error"]
error_types: ["runtime"]
tags: ["esrch", "no-such-process", "errno-3", "pid", "process"]
weight: 30
---

# Linux ESRCH (errno 3) — No Such Process

ESRCH (errno 3) means the system could not find a process matching the specified process ID (PID) or thread ID (TID). This error occurs when you try to send a signal, query process information, or manipulate a process that no longer exists or was never running. It is common in scripts that track process lifecycles or when using tools like `kill`, `killall`, or `waitpid`.

## Common Causes

- The target process already exited or was terminated
- Using an outdated or incorrect PID
- Race condition where the process dies between lookup and action
- Typo or incorrect PID value in a script
- Process was never started on the system
- Attempting to signal a thread that has already completed

## How to Fix ESRCH

### 1. Verify the Process Exists

Check if the PID is actually running before acting on it:

```bash
# Check a specific PID
ps -p 12345

# List all running processes
ps aux | grep <process_name>

# Alternative: use pgrep to find PIDs by name
pgrep -f "process_name"
```

### 2. Use ps and top to Monitor Processes

If you are tracking a process dynamically, confirm it is alive before sending signals:

```bash
# Top shows live process data with PIDs
top -bn1 | grep "process_name"

# ps with format options for scripting
ps -eo pid,comm | grep "process_name"
```

### 3. Handle ESRCH in Scripts

When writing scripts that send signals, always check if the process exists first:

```bash
PID=12345

if kill -0 "$PID" 2>/dev/null; then
    kill "$PID"
else
    echo "Process $PID is not running"
fi
```

The `kill -0` trick sends signal 0 (no signal) to verify the process exists without actually killing it.

### 4. Check for PID File Staleness

Many daemons write PID files. If the process crashed, the PID file may be stale:

```bash
# View the PID file
cat /var/run/myapp.pid

# Verify the PID is still alive
kill -0 $(cat /var/run/myapp.pid) 2>/dev/null && echo "Running" || echo "Stale PID"

# Remove stale PID file
sudo rm /var/run/myapp.pid
```

### 5. Use waitpid Correctly in Scripts

If you are waiting on a child process that may have already exited:

```bash
# Capture PID of background process
my_command &
PID=$!

# Wait and handle the case where the process is gone
if kill -0 "$PID" 2>/dev/null; then
    wait "$PID"
    echo "Exit code: $?"
else
    echo "Process $PID already exited"
fi
```

### 6. Use /proc to Investigate

The `/proc` filesystem provides detailed process info on Linux:

```bash
# Check if /proc/<pid> exists
ls /proc/12345

# Read process status
cat /proc/12345/status 2>/dev/null || echo "Process not found"

# Check process command
cat /proc/12345/cmdline 2>/dev/null | tr '\0' ' '
```

### 7. Avoid Race Conditions in Scripts

If multiple scripts interact with the same process, use file locking:

```bash
(
    flock -n 9 || { echo "Another instance is running"; exit 1; }
    # Your critical section here
    PID=$(cat /var/run/myapp.pid)
    kill "$PID" 2>/dev/null || echo "Process already gone"
) 9>/tmp/myapp.lock
```

## When to Investigate Further

ESRCH is usually harmless and expected when a process has already exited. However, if you see it repeatedly for a process that should be running, check system logs for crash information:

```bash
journalctl -u my_service --since "1 hour ago"
dmesg | tail -50
```

## Related Error Codes

- [EPERM (errno 1)](/os/linux/errno-1/) — Operation not permitted
- [ECHILD (errno 10)](/os/linux/errno-10/) — No child processes
- [ESRCH (errno 3)](/os/linux/errno-3/) — No such process
