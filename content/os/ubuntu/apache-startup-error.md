---
title: "[Solution] Ubuntu Server: apache-startup-error"
description: "Fix Ubuntu apache-startup-error. Apache httpd fails to start."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Apache Startup Error

Apache httpd service fails to start.

## Common Causes
- Port 80 or 443 already in use
- Configuration syntax error
- Missing module or wrong load order
- DocumentRoot does not exist

## How to Fix
1. Check Apache status
```bash
sudo systemctl status apache2
```
2. Test configuration
```bash
sudo apache2ctl configtest
```
3. Check for port conflicts
```bash
sudo ss -tlnp | grep :80
sudo ss -tlnp | grep :443
```

## Examples
```bash
$ sudo systemctl status apache2
● apache2.service - The Apache HTTP Server
   Active: failed (Result: exit-code)

$ sudo apache2ctl configtest
AH00558: apache2: Could not reliably determine the servers
