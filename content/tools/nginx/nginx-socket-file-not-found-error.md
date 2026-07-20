---
title: "[Solution] Nginx Socket File Not Found Error"
description: "The Unix socket file referenced in the configuration does not exist."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The Unix socket file referenced in the configuration does not exist.

## Common Causes

- **Socket file deleted**
- **Backend not creating socket**
- **Wrong path** in config
- **Permission issues**

## How to Fix

1. Check: `ls -la /run/nginx.sock`
2. Verify backend creates socket
3. Fix path in config
4. Check permissions

## Examples

**Check:**
```bash
ls -la /run/nginx.sock
# If missing, backend may need restart
```
**Fix:**
```bash
sudo systemctl restart app-backend
ls -la /run/nginx.sock
```