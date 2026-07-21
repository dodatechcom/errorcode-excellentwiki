---
title: "[Solution] Linux: audit-rate-error -- audit rate limiting error"
description: "Fix Linux audit rate limit errors. Audit daemon rate limiting dropping events."
os: ["linux"]
error-types: ["audit-error"]
severities: ["warning"]
---

# Linux: Audit Rate Limit Error

Audit rate limit errors occur when the kernel audit subsystem drops events.

## Common Causes

- Too many audit rules generating excessive events
- Audit backlog limit too low for workload
- Kernel audit buffer size insufficient
- High-frequency syscalls generating audit floods
- auditeventd rate limiting dropping messages

## How to Fix

### 1. Check Audit Status

```bash
sudo auditctl -s
sudo ausearch -m AVC --start recent 2>/dev/null | wc -l
cat /proc/sys/kernel/audit_backlog_limit
```

### 2. Increase Audit Limits

```bash
echo 8192 | sudo tee /proc/sys/kernel/audit_backlog_limit
sudo sysctl -w kernel.audit_backlog_limit=8192
```

### 3. Optimize Rules

```bash
sudo auditctl -l
sudo auditctl -D
sudo auditctl -w /etc/passwd -p wa -k passwd_changes
```

## Examples

```bash
$ sudo auditctl -s
enabled 1
backlog_limit 8192
lost 4523
# Lost events indicate rate limiting
$ echo 16384 | sudo tee /proc/sys/kernel/audit_backlog_limit
```
