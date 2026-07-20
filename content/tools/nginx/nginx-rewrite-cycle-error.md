---
title: "[Solution] Nginx Rewrite or Internal Redirect Cycle Error"
description: "Nginx detected an infinite loop of rewrites or internal redirects."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx detected an infinite loop of rewrites or internal redirects.

## Common Causes

- **Rewrite rules redirecting to themselves**
- **try_files pointing to looping location**
- **Recursive rewrites** without terminal condition
- **Broken alias/root**

## How to Fix

1. Trace: `curl -vL http://example.com/page 2>&1 | grep -i location`
2. Check self-referencing rules
3. Add break or condition
4. Use return instead of rewrite

## Examples

**Broken:**
```nginx
location / { try_files $uri $uri/ @fallback; }
location @fallback { rewrite ^ /index.php last; }  # loops
```
**Fixed:**
```nginx
location / { try_files $uri $uri/ /index.php?$args; }
```