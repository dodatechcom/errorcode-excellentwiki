---
title: "[Solution] Linux: selinux-port-label-error -- SELinux port label missing"
description: "Fix Linux SELinux port label errors. SELinux port type definition missing for service."
os: ["linux"]
error-types: ["selinux-error"]
severities: ["error"]
---

# Linux: SELinux Port Label Error

SELinux port label errors occur when a service binds to a port without proper type.

## Common Causes

- Service using non-standard port not in policy
- semanage port add failed due to label conflict
- Service restarted before port label applied
- Container runtime using ephemeral ports
- Policy missing port type for application

## How to Fix

### 1. Check Port Labels

```bash
sudo semanage port -l | grep <port_number>
sudo semanage port -l | grep http_port
```

### 2. Add Port Label

```bash
sudo semanage port -a -t http_port_t -p tcp 8080
sudo semanage port -m -t http_port_t -p tcp 8080
```

### 3. Verify and Restart

```bash
sudo semanage port -l | grep 8080
sudo systemctl restart <service>
```

## Examples

```bash
$ sudo semanage port -l | grep 8080
$ sudo semanage port -a -t http_port_t -p tcp 8080
$ sudo semanage port -l | grep 8080
http_port_t    tcp    8080, 8008, 8443
```
