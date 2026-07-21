---
title: "Ubuntu Seccomp Filter Error"
description: "Seccomp sandbox blocking system calls required by application"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Seccomp Filter Error

Seccomp sandbox blocking system calls required by application

## Common Causes

- Seccomp filter contains blacklist rule for required syscall
- Docker default seccomp profile blocking operation
- Application uses syscalls not in seccomp whitelist
- Seccomp mode not compatible with application

## How to Fix

1. Check seccomp: `grep Seccomp /proc/<pid>/status`
2. Run without seccomp: `docker run --security-opt seccomp=unconfined`
3. Check blocked syscall: `strace -c <command>`
4. Custom profile: `docker run --security-opt seccomp=custom.json`

## Examples

```bash
# Check if process uses seccomp
grep Seccomp /proc/self/status

# Run Docker container without seccomp
docker run --security-opt seccomp=unconfined myimage

# Trace system calls
strace -c ls
```
