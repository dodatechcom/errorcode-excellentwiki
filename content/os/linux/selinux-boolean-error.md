---
title: "[Solution] Linux: selinux-boolean-error -- SELinux boolean error"
description: "Fix Linux SELinux boolean errors. SELinux boolean configuration or persistence error."
os: ["linux"]
error-types: ["selinux-error"]
severities: ["error"]
---

# Linux: SELinux Boolean Error

SELinux boolean errors occur when security policy booleans are misconfigured.

## Common Causes

- Boolean name does not exist in policy
- SELinux in permissive mode masking errors
- Persistent boolean not surviving reboot
- Boolean requires specific module version
- setsebool fails due to policy lock

## How to Fix

### 1. Check Boolean Status

```bash
getsebool -a | grep <boolean_name>
semanage boolean -l | grep <boolean_name>
```

### 2. Set Boolean

```bash
sudo setsebool -P <boolean_name> on
sudo setsebool -P <boolean_name> off
```

### 3. Debug Boolean Issues

```bash
ausearch -m AVC -ts recent
sealert -a /var/log/audit/audit.log
sudo semanage boolean -l | head -20
```

## Examples

```bash
$ getsebool -a | grep httpd_can_network_connect
httpd_can_network_connect --> off
$ sudo setsebool -P httpd_can_network_connect on
$ getsebool -a | grep httpd_can_network_connect
httpd_can_network_connect --> on
```
