---
title: "[Solution] Nginx Sticky Cookie Error"
description: "The sticky cookie directive (commercial or third-party module) is misconfigured."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The sticky cookie directive (commercial or third-party module) is misconfigured.

## Common Causes

- **Module not loaded** (Nginx Plus required)
- **Invalid cookie parameters**
- **Duplicate sticky directives**

## How to Fix

1. Check module: `nginx -V 2>&1 | grep sticky`
2. Use correct syntax
3. Use open-source alternative with map/cookies

## Examples

**Nginx Plus:**
```nginx
upstream backend {
    sticky cookie srv_id expires=1h domain=.example.com path=/;
    server 10.0.0.1:8080; server 10.0.0.2:8080;
}
```