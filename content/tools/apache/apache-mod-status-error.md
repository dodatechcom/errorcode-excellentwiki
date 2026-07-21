---
title: "[Solution] Apache mod_status Error"
description: "Fix Apache mod_status errors when server-status page returns 403 or 500 errors."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache mod_status Error

Apache mod_status returns forbidden or internal errors when accessing the server-status page.

```
AH01630: client denied by server configuration (server-status)
```

## Common Causes

- mod_status not enabled
- Access restrictions block localhost
- ExtendedStatus not configured
- Proxy interfering with status path
- Location directive missing or wrong

## How to Fix

### Enable mod_status

```bash
a2enmod status
systemctl restart apache2
```

### Configure Status Access

```apache
# Allow status from localhost
<Location "/server-status">
    SetHandler server-status
    Require ip 127.0.0.1
    Require ip ::1
</Location>
```

### Enable Extended Status

```apache
ExtendedStatus On
```

### Allow Access from Monitoring Tools

```apache
<Location "/server-status">
    SetHandler server-status
    Require ip 127.0.0.1
    Require ip 10.0.0.0/8
    Require ip 192.168.0.0/16
</Location>
```

### Access Status via CLI

```bash
# Quick status check
curl http://localhost/server-status

# Full status with details
curl http://localhost/server-status?auto
curl http://localhost/server-status?refresh=5
```

## Examples

```apache
# Complete status configuration
<IfModule mod_status.c>
    ExtendedStatus On
    <Location "/server-status">
        SetHandler server-status
        Require ip 127.0.0.1
        Require ip 10.0.0.0/8
    </Location>
    <Location "/server-info">
        SetHandler server-info
        Require ip 127.0.0.1
    </Location>
</IfModule>
```
