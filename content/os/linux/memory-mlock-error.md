---
title: "[Solution] Linux: memory-mlock-error -- mlock memory locking failure"
description: "Fix Linux mlock errors. Memory locking failure preventing processes from pinning pages."
os: ["linux"]
error-types: ["memory-error"]
severities: ["error"]
---

# Linux: Memory Mlock Error

Memory mlock errors occur when processes fail to lock pages in physical memory.

## Common Causes

- RLIMIT_MEMLOCK limit too low
- Insufficient locked memory for requested pages
- vm.overcommit_memory preventing mlock
- Application requesting mlock without CAP_IPC_LOCK
- ulimit settings conflicting with requirements

## How to Fix

### 1. Check Limits

```bash
ulimit -a | grep -i lock
cat /proc/self/limits | grep "Locked"
cat /proc/<pid>/status | grep -i locked
```

### 2. Increase mlock Limit

```bash
ulimit -l unlimited
# Persistent: /etc/security/limits.conf
* hard memlock unlimited
* soft memlock unlimited
```

### 3. Check Overcommit

```bash
cat /proc/sys/vm/overcommit_memory
sudo sysctl vm.overcommit_memory=0
```

## Examples

```bash
$ ulimit -l
64
$ cat /proc/<pid>/status | grep -i locked
VmLck:    0 kB
$ ulimit -l unlimited
$ ulimit -l
unlimited
```
