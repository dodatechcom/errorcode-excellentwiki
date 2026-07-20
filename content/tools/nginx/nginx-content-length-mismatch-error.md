---
title: "[Solution] Nginx Content Length Mismatch Error"
description: "The actual request body size does not match the Content-Length header value."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The actual request body size does not match the Content-Length header value.

## Common Causes

- **Client miscalculating** Content-Length
- **Chunked encoding** mixed with Content-Length
- **Compression** changing body size
- **Client sending after declaring close**

## How to Fix

1. Verify client sends correct Content-Length
2. Enable strict parsing: `client_body_in_single_buffer on;`
3. Check client HTTP library

## Examples

**Test:**
```bash
curl -X POST -d '{"key":"value"}' -H 'Content-Type: application/json' http://localhost:8080/api
```
**Buffer:**
```nginx
client_body_buffer_size 128k; client_max_body_size 100M;
```