---
title: "[Solution] Ubuntu Server: kernel-ubuntu-oom-killer"
description: "Fix Ubuntu kernel-ubuntu-oom-killer. Out-of-memory killer terminates processes on Ubuntu."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Kernel Ubuntu OOM Killer

The OOM killer terminates processes when the system runs out of memory.

## Common Causes
- Application memory leak
- Too many services running for available RAM
- Swap space too small or missing
- cgroup memory limits too restrictive

## How to Fix
1. Check OOM events
```bash
dmesg | grep -i "oom\|out of memory"
journalctl -k | grep -i oom
```
2. Check memory usage
```bash
free -h
cat /proc/meminfo
```
3. Adjust OOM score for critical processes
```bash
echo -1000 | sudo tee /proc/<PID>/oom_score_adj
```

## Examples
```bash
$ dmesg | grep -i oom
[ 5678.901] Out of memory: Kill process 1234 (java) score 800 or sacrifice child
[ 5678.901] Killed process 1234 (java) total-vm:2048000kB, anon-rss:1500000kB
```
