---
title: "[Solution] Nginx Open File Limit Reached Error"
description: "Nginx has reached the system limit for open file descriptors."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx has reached the system limit for open file descriptors.

## Common Causes

- **Too many open connections**
- **Cache files** consuming FDs
- **Keepalive connections** not releasing
- **FD limit too low**

## How to Fix

1. Check: `cat /proc/$(cat /run/nginx.pid)/limits | grep 'Max open files'`
2. Increase: `worker_rlimit_nofile 65535;` in nginx.conf
3. System limits: `ulimit -n 65535`
4. Monitor: `ls /proc/$(cat /run/nginx.pid)/fd | wc -l`

## Examples

**Config:**
```nginx
worker_rlimit_nofile 65535;
events { worker_connections 16384; }
```
**System:**
```bash
# /etc/security/limits.conf
* soft nofile 65535
* hard nofile 65535
```