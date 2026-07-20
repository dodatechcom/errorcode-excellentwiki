---
title: "[Solution] Nginx Auth Request Error"
description: "The auth_request subrequest to the authentication service failed or returned an error."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The auth_request subrequest to the authentication service failed or returned an error.

## Common Causes

- **Auth service down**
- **Auth returning 500**
- **Timeout connecting**
- **Wrong URI**

## How to Fix

1. Verify: `curl -I http://auth-service:8080/verify`
2. Set timeout: `proxy_connect_timeout 5s; proxy_read_timeout 5s;`
3. Handle failures gracefully

## Examples

**Setup:**
```nginx
location /api/ { auth_request /auth; proxy_pass http://backend; }
location = /auth {
    internal;
    proxy_pass http://auth:8080/validate;
    proxy_pass_request_body off;
    proxy_set_header Content-Length "";
    proxy_set_header X-Original-URI $request_uri;
}
```