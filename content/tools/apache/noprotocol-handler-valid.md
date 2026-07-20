---
title: "[Solution] Apache No Protocol Handler Was Valid"
description: "No proxy protocol handler is available for the requested URL scheme."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

No proxy protocol handler is available for the requested URL scheme.

## Common Causes

- mod_proxy_http not loaded for HTTP backends
- mod_proxy_fcgi not loaded for FastCGI
- mod_proxy_ajp not loaded for AJP
- Wrong URL scheme in ProxyPass

## How to Fix

- Load the appropriate proxy protocol module
- Verify module matches the backend protocol
- Check ProxyPass URL scheme

## Examples

```
['LoadModule proxy_http_module modules/mod_proxy_http.so\nLoadModule proxy_fcgi_module modules/mod_proxy_fcgi.so\nLoadModule proxy_ajp_module modules/mod_proxy_ajp.so']
```
