---
title: "[Solution] Nginx Break Directive Error"
description: "The break directive is used in the wrong context or causes unintended behavior."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The break directive is used in the wrong context or causes unintended behavior.

## Common Causes

- **break inside if** not stopping rewrites as expected
- **break in wrong nesting level**
- **Mixing break with rewrite** causing confusion

## How to Fix

1. Use break only in server/location context
2. break stops rewrite processing but does not change URI
3. Use last to restart location matching

## Examples

**break vs last:**
```nginx
rewrite ^/test$ /test.html break;    # stops rewrites, processes location
rewrite ^/old$ /new last;            # restarts location matching
```
**Valid:**
```nginx
location / {
    rewrite ^/(.*)$ /index.php?path=$1 break;
    fastcgi_pass unix:/run/php-fpm.sock;
}
```