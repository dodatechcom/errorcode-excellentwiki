---
title: "[Solution] Nginx Conflicting Server Name Error"
description: "Multiple server blocks have conflicting server_name entries on the same listen address."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Multiple server blocks have conflicting server_name entries on the same listen address.

## Common Causes

- **Wildcard conflicts** (`*.example.com` and `example.com`)
- **Same domain** in multiple config files
- **Symlinked configs** loaded twice

## How to Fix

1. List declarations: `grep -rn 'server_name' /etc/nginx/ --include='*.conf'`
2. Remove duplicates
3. Use `default_server` for catch-all
4. Validate: `sudo nginx -t && sudo nginx -s reload`

## Examples

**Fixed:**
```nginx
server { listen 443 ssl; server_name app.example.com; }
server { listen 443 ssl; server_name admin.example.com; }
```