---
title: "[Solution] Nginx Sub Filter Types Mismatch Error"
description: "The sub_filter_types directive does not include the MIME type of the response being filtered."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The sub_filter_types directive does not include the MIME type of the response being filtered.

## Common Causes

- **Default sub_filter_types** only includes text/html
- **API responses** with application/json not included
- **Custom MIME types** missing

## How to Fix

1. Add types: `sub_filter_types text/html text/plain application/json application/javascript;`
2. Use * for all (careful with binary)
3. Set sub_filter_once: `sub_filter_once off;`

## Examples

**Filter HTML and JSON:**
```nginx
sub_filter_types text/html application/json text/plain;
sub_filter 'example.com' 'newdomain.com';
sub_filter_once off;
```
**With proxy:**
```nginx
location / {
    sub_filter 'http://' 'https://';
    sub_filter_types text/html text/css application/javascript;
    proxy_pass http://backend;
}
```