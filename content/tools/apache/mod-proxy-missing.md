---
title: "[Solution] Apache mod_proxy Missing"
description: "Proxy directives are used but mod_proxy is not loaded."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Proxy directives are used but mod_proxy is not loaded.

## Common Causes

- LoadModule proxy_module missing
- ProxyPass directives without loaded module
- Related proxy modules not loaded

## How to Fix

- Load all required proxy modules:
LoadModule proxy_module modules/mod_proxy.so
LoadModule proxy_http_module modules/mod_proxy_http.so
- Install mod_proxy package if missing
- Restart Apache after changes

## Examples

```
['LoadModule proxy_module modules/mod_proxy.so\nLoadModule proxy_http_module modules/mod_proxy_http.so\nProxyPass / http://backend:8080/']
```
