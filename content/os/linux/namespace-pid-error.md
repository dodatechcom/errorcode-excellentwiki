---
title: "[Solution] Linux: namespace-pid-error -- PID namespace failure"
description: "Fix Linux PID namespace errors. PID namespace creation or entry failure."
os: ["linux"]
error-types: ["namespace-error"]
severities: ["error"]
---

# Linux: PID Namespace Error

PID namespace errors occur when creating or entering PID namespaces fails.

## Common Causes

- Insufficient privileges for PID namespace
- Kernel parameter restricting namespace creation
- /proc mount not visible in namespace
- Nested PID namespace depth limit reached
- init process not running in PID namespace

## How to Fix

### 1. Check Namespace Support

```bash
cat /proc/sys/kernel/unprivileged_userns_clone
unshare --pid --fork echo test
ls /proc/1/ns/pid
```

### 2. Enable User Namespaces

```bash
echo 1 | sudo tee /proc/sys/kernel/unprivileged_userns_clone
sudo sysctl kernel.unprivileged_userns_clone=1
```

### 3. Enter PID Namespace

```bash
sudo nsenter --pid=/proc/<pid>/ns/pid -- ps aux
unshare -fp --mount-proc bash
```

## Examples

```bash
$ unshare --pid --fork echo test
unshare: Operation not permitted
$ cat /proc/sys/kernel/unprivileged_userns_clone
0
$ echo 1 | sudo tee /proc/sys/kernel/unprivileged_userns_clone
1
$ unshare --pid --fork echo test
test
```
