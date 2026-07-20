---
title: "[Solution] Nginx Access Log File Open Error"
description: "Nginx cannot open the access log file for writing."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx cannot open the access log file for writing.

## Common Causes

- **Directory does not exist**
- **Permission denied**
- **Disk full**
- **Invalid path** in config

## How to Fix

1. Check directory: `ls -la /var/log/nginx/`
2. Permissions: `chown nginx:nginx /var/log/nginx/`
3. Disk space: `df -h /var/log/`
4. Fix path in config

## Examples

**Check:**
```bash
ls -la /var/log/nginx/
df -h /var/log/
```
**Fix:**
```bash
sudo mkdir -p /var/log/nginx
sudo chown nginx:nginx /var/log/nginx/
```