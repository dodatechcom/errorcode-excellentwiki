---
title: "[Solution] Nginx URI Too Long Error"
description: "The requested URI is longer than the maximum allowed length (HTTP 414)."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The requested URI is longer than the maximum allowed length (HTTP 414).

## Common Causes

- **Excessive query parameters**
- **Session data in URL**
- **Malformed client** generating long URLs
- **API clients** constructing URLs wrong

## How to Fix

1. Increase buffer: `large_client_header_buffers 4 32k;`
2. Set header buffer: `client_header_buffer_size 4k;`
3. Return 414 for long URIs
4. Fix client app

## Examples

**Check lengths:**
```bash
awk '{print length($7), $7}' /var/log/nginx/access.log | sort -rn | head
```
**Buffer:**
```nginx
client_header_buffer_size 4k;
large_client_header_buffers 4 32k;
```