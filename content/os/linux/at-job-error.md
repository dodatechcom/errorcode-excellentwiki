---
title: "[Solution] Linux: at-job-error -- at job scheduling failure"
description: "Fix Linux at job errors. At job scheduling or execution failure due to daemon issues."
os: ["linux"]
error-types: ["cron-error"]
severities: ["error"]
---

# Linux: At Job Error

At job errors occur when scheduled one-time jobs fail to execute.

## Common Causes

- atd daemon not running or crashed
- /var/spool/at not writable
- User not in /etc/at.allow or in at.deny
- Job output exceeding buffer causing crash
- System clock jump causing missed execution

## How to Fix

### 1. Check atd Status

```bash
systemctl status atd
atq
at -l
```

### 2. Fix Permissions

```bash
ls -la /var/spool/at/
cat /etc/at.allow 2>/dev/null
cat /etc/at.deny
```

### 3. Schedule and Verify

```bash
echo "echo test" | at now + 5 minutes
atq
at -c 1
```

## Examples

```bash
$ systemctl status atd
● atd.service - Deferred execution scheduler
     Active: failed (Result: exit-code)
$ sudo systemctl start atd
$ echo "echo hello" | at now + 5 minutes
warning: commands will be executed using /bin/sh
job 1 at Thu Jul 20 14:05:00 2026
```
