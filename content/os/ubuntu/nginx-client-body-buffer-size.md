---
title: "Nginx Client Body Buffer Size Error"
description: "Nginx returns 413 or 400 errors for large client requests"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Nginx Client Body Buffer Size Error

Nginx returns 413 or 400 errors for large client requests

## Common Causes

- client_body_buffer_size too small for request body
- client_max_body_size limiting uploads
- Buffer overflow causing request rejection
- Temporary directory for client body not writable

## How to Fix

1. Increase buffer: `client_body_buffer_size 128k;`
2. Increase max size: `client_max_body_size 10m;`
3. Check temp: `client_body_temp_path /var/lib/nginx/client_temp;`
4. Review error log: `grep 'client intended' /var/log/nginx/error.log`

## Examples

```nginx
# Increase client body settings
server {
    client_max_body_size 50m;
    client_body_buffer_size 256k;
    client_body_temp_path /var/lib/nginx/client_temp 1 2;
}
```
