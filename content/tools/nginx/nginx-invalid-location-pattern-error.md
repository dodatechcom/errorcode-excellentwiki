---
title: "[Solution] Nginx Invalid Location Pattern Error"
description: "A location block contains an invalid regex pattern or malformed URI prefix."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

A location block contains an invalid regex pattern or malformed URI prefix.

## Common Causes

- **Malformed regex** - unescaped special characters
- **Missing URI prefix**
- **Conflicting location modifiers**
- **Unclosed brackets** in regex

## How to Fix

1. Test regex: `echo test-string | pcregrep '/pattern/'`
2. Escape special characters properly
3. Use `location ^~` for prefix matches
4. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
location ~ /path/(.+)+/file { }  # error: nothing to repeat
```
**Valid:**
```nginx
location ~ /path/([^/]+)/file$ { }
location ^~ /static/ { alias /var/www/static/; }
```