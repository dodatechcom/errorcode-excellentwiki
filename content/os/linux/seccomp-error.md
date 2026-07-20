---
title: "[Solution] Linux: seccomp-error — seccomp error"
description: "Fix Linux seccomp-error errors. seccomp error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["process-error"]
weight: 8
---
# Linux: Seccomp Error

Seccomp (secure computing mode) errors occur when a process tries to make a system call that has been blocked by a seccomp filter.

## Common Causes

- Docker/containerd seccomp profile blocking a syscall the application needs
- Application running with --security-opt seccomp=unconfined needed
- Custom seccomp profile too restrictive
- Chrome/Firefox sandbox seccomp filters blocking legitimate operations
- System call number change between kernel versions

## How to Fix

### 1. Check for Seccomp Errors

```bash
dmesg | grep -i seccomp
journalctl -k | grep -i seccomp
```

### 2. Check Seccomp Status of Process

```bash
cat /proc/<pid>/status | grep Seccomp
# 0 = disabled, 1 = strict, 2 = filter
```

### 3. Run Docker Container Without Seccomp

```bash
docker run --security-opt seccomp=unconfined myimage
```

### 4. Use a Custom Seccomp Profile

```bash
docker run --security-opt seccomp=/path/to/profile.json myimage
```

## Examples

```bash
$ cat /proc/1234/status | grep Seccomp
Seccomp:	2

$ dmesg | grep seccomp
[12345.678] audit: type=1326 audit(1623456789.012:345): auid=1000 uid=1000 gid=1000 ses=2 subj=unconfined pid=1234 comm="chrome" exe="/opt/google/chrome/chrome" sig=31 syscall=123 compat=0 ip=0x7f1234567890 code=0x0
```
