---
title: "[Solution] Apache CORS Misconfiguration Error"
description: "Fix Apache Cross-Origin Resource Sharing errors when CORS headers are not properly configured."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache CORS Misconfiguration Error

Apache returns CORS errors because the required headers are missing or incorrectly set.

```
Access to XMLHttpRequest has been blocked by CORS policy
```

## Common Causes

- Access-Control-Allow-Origin not set
- Missing Access-Control-Allow-Methods header
- Access-Control-Allow-Credentials conflicts with wildcard origin
- Preflight OPTIONS request not handled
- Headers not included in error responses

## How to Fix

### Enable CORS Headers

```apache
# Enable headers module
a2enmod headers

<IfModule mod_headers.c>
    Header set Access-Control-Allow-Origin "*"
    Header set Access-Control-Allow-Methods "GET, POST, PUT, DELETE, OPTIONS"
    Header set Access-Control-Allow-Headers "Content-Type, Authorization, X-Requested-With"
    Header set Access-Control-Max-Age "3600"
</IfModule>
```

### Handle Preflight Requests

```apache
# Respond to OPTIONS preflight
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{REQUEST_METHOD} OPTIONS
    RewriteRule ^(.*)$ $1 [R=200,L]
</IfModule>
```

### Restrict Origin for Security

```apache
<IfModule mod_headers.c>
    SetEnvIf Origin "^(https?://.*\.example\.com)$" CORS_ORIGIN=$0
    Header set Access-Control-Allow-Origin "%{CORS_ORIGIN}e" env=CORS_ORIGIN
    Header set Access-Control-Allow-Credentials "true" env=CORS_ORIGIN
</IfModule>
```

### Add CORS to Proxy Responses

```apache
<Proxy "http://backend:3000">
    Header set Access-Control-Allow-Origin "*"
    Header set Access-Control-Allow-Methods "GET, POST, OPTIONS"
</Proxy>
```

## Examples

```apache
# CORS for specific directory only
<Location /api>
    <IfModule mod_headers.c>
        Header set Access-Control-Allow-Origin "https://app.example.com"
        Header set Access-Control-Allow-Methods "GET, POST, PUT, DELETE"
        Header set Access-Control-Allow-Headers "Content-Type, Authorization"
    </IfModule>
</Location>
```
