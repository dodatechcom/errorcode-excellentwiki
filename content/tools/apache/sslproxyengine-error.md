---
title: "[Solution] Apache SSLProxyEngine Error"
description: "SSL proxy directives are used but SSLProxyEngine is not enabled."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

SSL proxy directives are used but SSLProxyEngine is not enabled.

## Common Causes

- SSLProxyEngine Off or missing
- SSLProxy* directives used without SSLProxyEngine On
- Module mod_proxy_http not loaded

## How to Fix

- Add SSLProxyEngine On in the relevant VirtualHost
- Ensure mod_proxy and mod_proxy_http are loaded
- Configure SSLProxyCACertificateFile for backend verification

## Examples

```
['SSLProxyEngine On\nSSLProxyCACertificateFile /etc/ssl/ca.crt\nProxyPass / https://backend:443/']
```
