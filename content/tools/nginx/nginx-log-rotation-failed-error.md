---
title: "[Solution] Nginx Log Rotation Failed Error"
description: "The log rotation process failed to properly rotate Nginx log files."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The log rotation process failed to properly rotate Nginx log files.

## Common Causes

- **Logrotate script error**
- **Nginx not receiving USR1 signal**
- **Permission issues** on log directory
- **Disk space** during rotation

## How to Fix

1. Check logrotate: `cat /etc/logrotate.d/nginx`
2. Send USR1: `sudo kill -USR1 $(cat /run/nginx.pid)`
3. Check permissions
4. Verify: `ls -la /var/log/nginx/`

## Examples

**Manual rotation:**
```bash
mv /var/log/nginx/access.log /var/log/nginx/access.log.1
sudo kill -USR1 $(cat /run/nginx.pid)
```
**Logrotate config:**
```
/var/log/nginx/*.log {
    daily
    missingok
    rotate 52
    compress
    delaycompress
    notifempty
    create 0640 nginx adm
    sharedscripts
    postrotate
        [ -f /run/nginx.pid ] && kill -USR1 $(cat /run/nginx.pid)
    endscript
}
```