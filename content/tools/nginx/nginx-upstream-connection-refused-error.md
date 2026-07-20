---
title: "[Solution] Nginx Upstream Connection Refused Error"
description: "Nginx cannot establish a TCP connection to the upstream server because it refused the connection."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx cannot establish a TCP connection to the upstream server because it refused the connection.

## Common Causes

- **Backend service not running**
- **Backend listening on wrong port/IP**
- **Firewall blocking**
- **Backend backlog full**

## How to Fix

1. Check backend: `systemctl status app-backend; ss -tlnp | grep 8080`
2. Verify upstream address matches
3. Check firewall: `sudo iptables -L -n | grep 8080`
4. Increase backlog: `listen 8080 backlog=65535;`

## Examples

**Verify:**
```bash
ss -tlnp | grep 8080
# LISTEN 0 128 0.0.0.0:8080 users:("node",pid=1234)
```
**Check process:**
```bash
ps aux | grep 'node|gunicorn|java' | grep -v grep
```