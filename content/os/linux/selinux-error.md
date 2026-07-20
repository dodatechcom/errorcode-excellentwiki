---
title: "[Solution] Linux: selinux-error — SELinux error"
description: "Fix Linux selinux-error errors. SELinux error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["process-error"]
weight: 8
---

# Linux: SELinux Error

SELinux errors occur when SELinux policies block access to files, ports, or processes.

## Common Causes

- File context label incorrect
- Policy missing for new application
- Boolean setting preventing access
- Port not defined in policy
- Application running in wrong domain

## How to Fix

### 1. Check SELinux Status

```bash
getenforce
sestatus
```

### 2. Check Denied Operations

```bash
sudo ausearch -m AVC -ts recent | tail -20
sudo sealert -a /var/log/audit/audit.log 2>/dev/null | head -30
```

### 3. Fix File Context

```bash
sudo restorecon -Rv /path
sudo semanage fcontext -a -t httpd_sys_content_t /web(/.*)?
sudo restorecon -Rv /web
```

### 4. Set Booleans

```bash
sudo setsebool -P httpd_can_network_connect on
```

## Examples

```bash
$ getenforce
Enforcing

$ sudo ausearch -m AVC -ts recent | tail -3
type=AVC msg=audit(123456.789): avc: denied { read } for pid=12345 comm="nginx" name="shadow"

$ sudo semanage boolean -l | grep httpd_can_network_connect
httpd_can_network_connect     (off, off) allow HTTPD scripts and modules to connect to the network
$ sudo setsebool -P httpd_can_network_connect on
```
