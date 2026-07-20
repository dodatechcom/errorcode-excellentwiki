---
title: "[Solution] Nginx Unsupported Media Type Error"
description: "The client sent a Content-Type that the server or backend does not accept (HTTP 415)."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The client sent a Content-Type that the server or backend does not accept (HTTP 415).

## Common Causes

- **Wrong Content-Type** (text/plain instead of application/json)
- **Backend rejecting** types
- **Missing Content-Type header**
- **Multipart boundary issues**

## How to Fix

1. Check client: `curl -X POST -H 'Content-Type: application/json' ...`
2. Validate at Nginx level
3. Ensure backend accepts the type

## Examples

**Validate:**
```nginx
location /api/ {
    set $valid 0;
    if ($content_type ~* '^(application/json|application/x-www-form-urlencoded)$') { set $valid 1; }
    if ($valid = 0) { return 415; }
    proxy_pass http://backend;
}
```