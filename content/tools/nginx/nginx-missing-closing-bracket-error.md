---
title: "[Solution] Nginx Missing Closing Bracket Error"
description: "A block in the Nginx configuration is missing a closing curly bracket."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

A block in the Nginx configuration is missing a closing curly bracket.

## Common Causes

- **Accidentally deleted** closing bracket
- **Nested blocks** where one bracket was forgotten
- **Include files** breaking bracket nesting
- **Copy-paste errors**

## How to Fix

1. Count brackets: `grep -c '{' /etc/nginx/nginx.conf` vs `grep -c '}'`
2. Use bracket-matching editor
3. Check include files too
4. Validate: `sudo nginx -t`

## Examples

**Missing:**
```nginx
server {
    listen 80;
    location / {
        proxy_pass http://backend;
    # missing }
}
```
**Fixed:**
```nginx
server {
    listen 80;
    location / { proxy_pass http://backend; }
}
```