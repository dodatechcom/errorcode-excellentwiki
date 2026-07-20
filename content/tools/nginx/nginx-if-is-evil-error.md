---
title: "[Solution] Nginx If Is Evil Error"
description: "Using the if directive inside a location block causes unexpected behavior with other directives."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Using the if directive inside a location block causes unexpected behavior with other directives.

## Common Causes

- **if with proxy_pass** applies both location and if directives
- **if with add_header** causes duplicate headers
- **if with try_files** causes unexpected routing
- **if does NOT create a separate scope**

## How to Fix

1. Use separate location blocks instead of if
2. Only use if safely with: return, rewrite...last, set
3. Use map for complex conditions

## Examples

**Safe:**
```nginx
location / {
    set $backend default;
    if ($host = admin.example.com) { set $backend admin; }
    proxy_pass http://$backend;
}
```
**Unsafe:**
```nginx
location / {
    if ($request_uri ~ '^/api') {
        add_header X-API true;  # duplicated!
        proxy_pass http://api;
    }
    proxy_pass http://default;
}
```