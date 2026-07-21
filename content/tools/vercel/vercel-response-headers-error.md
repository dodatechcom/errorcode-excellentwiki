---
title: "[Solution] Vercel Response Headers Error"
description: "Fix Vercel response header errors when custom headers are not applied correctly."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Vercel Response Headers Error

Vercel custom response headers are not applied or cause errors.

```
Error: Invalid header value
```

## Common Causes

- Header name contains invalid characters
- Header value exceeds length limit
- Conflicting security headers
- Headers not applied to correct paths
- CSP headers blocking resources

## How to Fix

### Configure Headers

```json
// vercel.json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "X-Content-Type-Options", "value": "nosniff" }
      ]
    }
  ]
}
```

### Set Security Headers

```json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "Strict-Transport-Security", "value": "max-age=31536000; includeSubDomains" },
        { "key": "X-XSS-Protection", "value": "1; mode=block" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" }
      ]
    }
  ]
}
```

### Set Cache Headers

```json
{
  "headers": [
    {
      "source": "/static/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    }
  ]
}
```

### Fix CSP Headers

```json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "Content-Security-Policy",
          "value": "default-src 'self'; script-src 'self' 'unsafe-inline';"
        }
      ]
    }
  ]
}
```

### Headers in Next.js

```javascript
// next.config.js
module.exports = {
  async headers() {
    return [
      {
        source: '/(.*)',
        headers: [
          { key: 'X-Frame-Options', value: 'DENY' }
        ]
      }
    ];
  }
};
```

## Examples

```json
// API-specific headers
{
  "headers": [
    {
      "source": "/api/(.*)",
      "headers": [
        { "key": "Access-Control-Allow-Origin", "value": "*" },
        { "key": "Cache-Control", "value": "no-store" }
      ]
    }
  ]
}
```
