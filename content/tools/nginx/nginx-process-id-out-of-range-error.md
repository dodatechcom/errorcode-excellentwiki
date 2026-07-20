---
title: "[Solution] Nginx Process ID Out of Range Error"
description: "The Nginx master process PID file contains an invalid or out-of-range process ID."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The Nginx master process PID file contains an invalid or out-of-range process ID.

## Common Causes

- **Corrupted PID file**
- **Stale PID file** from old process
- **PID file from wrong Nginx instance**

## How to Fix

1. Check PID file: `cat /run/nginx.pid`
2. Verify process: `ps -p $(cat /run/nginx.pid)`
3. Remove stale: `rm /run/nginx.pid && sudo nginx`
4. Check for multiple instances

## Examples

**Check:**
```bash
cat /run/nginx.pid
ps -p $(cat /run/nginx.pid)
# If no process, PID file is stale
```
**Fix:**
```bash
sudo rm /run/nginx.pid
sudo nginx
```