---
title: "[Solution] Nginx Rewrite Directive Not Allowed Error"
description: "The rewrite directive is used in a context where it is not permitted."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The rewrite directive is used in a context where it is not permitted.

## Common Causes

- **rewrite inside if** in location block
- **rewrite inside limit_except**
- **Wrong nesting level**

## How to Fix

1. Move rewrite to correct context
2. Use return inside if blocks
3. Use named locations for complex rewrites

## Examples

**Invalid:**
```nginx
location / {
    if ($request_uri ~ '^/old') { rewrite ^ /new permanent; }  # not allowed
}
```
**Fixed:**
```nginx
location ~ ^/old/(.*) { return 301 /new/$1; }
```