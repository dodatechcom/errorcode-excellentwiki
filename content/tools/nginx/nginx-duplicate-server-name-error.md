---
title: "[Solution] Nginx Duplicate Server Name Error"
description: "Two server blocks share the same server_name on the same port, causing a conflict."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Two server blocks share the same server_name on the same port, causing a conflict.

## Common Causes

- **Multiple config files** defining the same server_name
- **Copy-paste errors** duplicating server blocks
- **Include glob** pulling in files with overlapping names
- **Default server** conflicts

## How to Fix

1. Find duplicates: `grep -rn 'server_name' /etc/nginx/conf.d/ | sort`
2. Remove duplicates or make names unique
3. Use `default_server` for catch-all: `listen 80 default_server; server_name _;`
4. Validate: `sudo nginx -t && sudo nginx -s reload`

## Examples

**Broken:**
```nginx
# a.conf: server { listen 80; server_name example.com; }
# b.conf: server { listen 80; server_name example.com; }  # conflict
```
**Fixed:**
```nginx
server { listen 80; server_name example.com; }
server { listen 80; server_name www.example.com; }
```