---
title: "[Solution] Nginx Invalid Port Error"
description: "Nginx rejects a port number in a listen directive that is out of range or invalid."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx rejects a port number in a listen directive that is out of range or invalid.

## Common Causes

- Port number **exceeds 65535**
- Port number is **zero or negative**
- **Duplicate listen ports** across server blocks
- Using **privileged ports** (< 1024) without proper permissions

## How to Fix

1. Use valid port range (1-65535)
2. For privileged ports: `sudo setcap cap_net_bind_service=+ep /usr/sbin/nginx`
3. Check duplicates: `grep -rn 'listen ' /etc/nginx/`
4. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
server { listen 70000; }  # error: port > 65535
```
**Valid:**
```nginx
server { listen 80; listen 443 ssl; server_name example.com; }
server { listen 192.168.1.10:8080; server_name internal.example.com; }
```