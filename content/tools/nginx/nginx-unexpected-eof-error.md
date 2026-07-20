---
title: "[Solution] Nginx Unexpected End of File Error"
description: "Nginx reached the end of a configuration file before all blocks or directives are properly closed."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx reached the end of a configuration file before all blocks or directives are properly closed.

## Common Causes

- **Truncated config file**
- **Missing semicolons** at end of directives
- **Unclosed blocks**
- **Empty config files**

## How to Fix

1. Check the line number from the error
2. Ensure file is not truncated: `wc -l file.conf; tail -5 file.conf`
3. Add missing semicolons or brackets
4. Validate: `sudo nginx -t`

## Examples

**Truncated:**
```nginx
server {
    listen 80;
    server_name example.com  # missing semicolon, file ends
```
**Fixed:**
```nginx
server { listen 80; server_name example.com; location / { root /var/www; } }
```