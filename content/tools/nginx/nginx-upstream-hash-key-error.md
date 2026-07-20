---
title: "[Solution] Nginx Upstream Hash Key Error"
description: "The hash directive in the upstream block has an invalid key or configuration."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The hash directive in the upstream block has an invalid key or configuration.

## Common Causes

- **Missing hash key**
- **Undefined variable** as key
- **Hash with consistent placed incorrectly**

## How to Fix

1. Provide valid key: `hash $request_uri consistent;`
2. Use well-known vars ($request_uri, $remote_addr, $host)
3. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
upstream backend { hash; server 10.0.0.1:8080; }  # missing key
```
**Valid:**
```nginx
upstream backend { hash $request_uri consistent; server 10.0.0.1:8080; server 10.0.0.2:8080; }
```