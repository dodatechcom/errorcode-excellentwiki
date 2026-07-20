---
title: "[Solution] Nginx Redirect Loop Error"
description: "The server creates an infinite redirect loop between HTTP and HTTPS or between URLs."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The server creates an infinite redirect loop between HTTP and HTTPS or between URLs.

## Common Causes

- **HTTP-to-HTTPS redirect** not accounting for LB
- **Missing X-Forwarded-Proto** from LB
- **Both HTTP and HTTPS** redirecting to each other
- **Proxy passing** to self-redirecting server

## How to Fix

1. Use X-Forwarded-Proto for LBs
2. Handle forwarded headers
3. Trace: `curl -vL http://example.com 2>&1 | grep -i location`

## Examples

**Broken:**
```nginx
server { listen 80; return 301 https://example.com; }
server { listen 443 ssl; return 301 http://example.com; }  # loop
```
**Fixed:**
```nginx
server { listen 80; return 301 https://example.com$request_uri; }
server { listen 443 ssl; server_name example.com; root /var/www/html; }
```