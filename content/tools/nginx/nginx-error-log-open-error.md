---
title: "[Solution] Nginx Error Log File Open Error"
description: "Nginx cannot open the error log file for writing."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx cannot open the error log file for writing.

## Common Causes

- **Directory does not exist**
- **Permission denied**
- **Disk full**
- **Invalid path**

## How to Fix

1. Check: `ls -la /var/log/nginx/`
2. Permissions: `sudo chown nginx:nginx /var/log/nginx/`
3. Disk: `df -h`
4. Validate: `sudo nginx -t`

## Examples

**Fix:**
```bash
sudo mkdir -p /var/log/nginx
sudo chown nginx:nginx /var/log/nginx/
sudo nginx -t
```