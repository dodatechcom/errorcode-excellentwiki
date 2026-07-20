---
title: "[Solution] Nginx Request Line Too Long Error"
description: "The HTTP request line exceeds the configured buffer size."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The HTTP request line exceeds the configured buffer size.

## Common Causes

- **Very long URL** with many params
- **Session tokens** in URL
- **Malicious oversized URIs**
- **Default buffer too small** (8k)

## How to Fix

1. Increase: `large_client_header_buffers 4 16k;`
2. Limit URI length at app level
3. Use POST for large data
4. Set client_header_buffer_size

## Examples

**Default (may be too small):**
```nginx
# large_client_header_buffers 4 8k
```
**Increased:**
```nginx
large_client_header_buffers 4 32k;
```
**Check:**
```bash
awk '{print length($6), $7}' /var/log/nginx/access.log | sort -rn | head
```