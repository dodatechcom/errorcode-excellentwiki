---
title: "[Solution] Linux: audit-error — audit system error"
description: "Fix Linux audit-error errors. audit system error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["process-error"]
weight: 8
---

# Linux: Audit Error

Audit errors occur when the Linux Audit framework fails to log events or the audit daemon encounters issues.

## Common Causes

- Audit daemon (auditd) not running
- Disk full on audit log partition
- Audit rules syntax error
- Kernel audit buffer overflow
- SELinux/AppArmor blocking audit events

## How to Fix

### 1. Check Audit Status

```bash
sudo systemctl status auditd
sudo auditctl -s
```

### 2. Check Audit Logs

```bash
sudo ausearch -ts today | tail -30
sudo tail /var/log/audit/audit.log
```

### 3. Check Disk Space

```bash
df -h /var/log/audit/
sudo auditctl -b 8192
```

### 4. Reload Rules

```bash
sudo auditctl -R /etc/audit/rules.d/audit.rules
sudo systemctl restart auditd
```

## Examples

```bash
$ sudo auditctl -s
enabled 1
failure 1
pid 12345
rate_limit 0
backlog_limit 64
lost 5
backlog 0

$ sudo ausearch -m AVC -ts today
<no matches>
```
