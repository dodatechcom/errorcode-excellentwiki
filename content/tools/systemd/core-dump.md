---
title: "[Solution] Systemd Process Crashed (Core Dump)"
description: "Fix systemd core dump errors. Diagnose and resolve process crashes that generate core dumps."
tools: ["systemd"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["core-dump", "crash", "segfault", "systemd", "coredump"]
weight: 5
---

# Systemd Process Crashed (Core Dump)

A core dump occurs when a process receives a fatal signal (SIGSEGV, SIGABRT, etc.) and the OS writes a memory snapshot to disk. Systemd logs the crash and marks the unit as failed.

## Common Causes

- A segmentation fault caused by invalid memory access
- An assertion failure or unhandled exception in the application
- A library mismatch or corrupted binary
- Insufficient memory causing the OOM killer to terminate the process

## How to Fix

### Inspect the Core Dump

```bash
coredumpctl list
coredumpctl info <PID>
coredumpctl gdb <PID>
```

### Check Systemd Logs for the Crash

```bash
journalctl -u <service-name> -n 100 --no-pager
```

### Review Core Dump Settings

```ini
# /etc/systemd/coredump.conf
[Manager]
CoreDumpUseReliableShellSplit=true
MaxUse=1G
```

### Analyze with GDB

```bash
coredumpctl gdb <PID>
(gdb) bt
(gdb) info registers
```

### Disable Core Dumps (Production)

```bash
# /etc/security/limits.conf
* hard core 0

# Or via sysctl
sudo sysctl -w fs.suid_dumpable=0
```

## Examples

```bash
# Process segfaulted
# my-app.service: Main process exited, code=killed, signal=SEGV
# core dumped
# Fix: use coredumpctl gdb to find the crash location in code

# Out of memory killed
# my-app.service: Main process exited, code=killed, signal=KILL
# Fix: increase MemoryLimit or fix memory leak
```

## Related Errors

- [Permission Error]({{< relref "/tools/systemd/permission-error7" >}}) — access denied during operation
- [Timeout Start]({{< relref "/tools/systemd/timeout-start" >}}) — service failed to start in time
