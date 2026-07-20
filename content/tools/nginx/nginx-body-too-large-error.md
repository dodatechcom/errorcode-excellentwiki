---
title: "[Solution] Nginx Request Body Too Large Error"
description: "The client request body exceeds the client_max_body_size limit (HTTP 413)."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The client request body exceeds the client_max_body_size limit (HTTP 413).

## Common Causes

- **File upload exceeds limit**
- **Large JSON payloads**
- **Default limit too small** (1MB)
- **Uncompressed uploads**

## How to Fix

1. Increase: `client_max_body_size 100M;`
2. Set per-location limits
3. Disable (caution): `client_max_body_size 0;`
4. Enable buffering: `client_body_buffer_size 128k;`

## Examples

**Default (1MB):**
```nginx
client_max_body_size 1M;
```
**Per-location:**
```nginx
location /upload/ { client_max_body_size 1G; client_body_buffer_size 128k; }
```