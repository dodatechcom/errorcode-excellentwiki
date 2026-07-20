---
title: "[Solution] Nginx Return Directive Error"
description: "The return directive has an invalid status code or malformed redirect URL."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The return directive has an invalid status code or malformed redirect URL.

## Common Causes

- **Non-numeric status code**
- **Status code outside valid range**
- **Missing URL for redirect codes** (301, 302)

## How to Fix

1. Use valid codes: 200, 204, 301, 302, 303, 304, 307, 308, 400-599
2. Ensure redirects have URL
3. Use body for non-redirect codes

## Examples

**Valid:**
```nginx
return 200 'Welcome!';
return 301 https://www.example.com$request_uri;
return 403;
return 503 'Service Unavailable';
```
**Invalid:**
```nginx
return 999;    # invalid code
return 301;    # missing URL
```