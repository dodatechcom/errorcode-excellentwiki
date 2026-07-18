---
title: "[Solution] Vercel Headers Error — Fix Invalid Headers Configuration"
description: "Fix Vercel headers errors when custom headers are incorrectly configured. Validate header syntax and resolve conflicts between header rules in vercel.json."
tools: ["vercel"]
error-types: ["configuration-error"]
severities: ["warning"]
weight: 5
---

A Vercel headers error occurs when custom HTTP headers defined in vercel.json are invalid. Headers may not be applied, or the configuration may cause deployment failures.

## What This Error Means

Vercel allows setting custom headers through vercel.json. When the header configuration is malformed:

```
Error: Invalid headers configuration
"headers" expects an array of objects with "source" and "headers" properties
```

## Why It Happens

- The headers configuration has invalid JSON syntax
- The source pattern is incorrectly formatted
- Header names or values contain invalid characters
- Multiple header rules conflict with each other
- The header rule does not match any route
- The `Access-Control-Allow-Origin` header value is improperly set
- The `Content-Security-Policy` header contains invalid directives

## How to Fix It

### Use Correct Headers Syntax

```json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "X-Frame-Options",
          "value": "DENY"
        },
        {
          "key": "X-Content-Type-Options",
          "value": "nosniff"
        }
      ]
    },
    {
      "source": "/api/(.*)",
      "headers": [
        {
          "key": "Access-Control-Allow-Origin",
          "value": "*"
        }
      ]
    }
  ]
}
```

### Use Correct Source Patterns

```json
{
  "headers": [
    {
      "source": "/images/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=31536000, immutable"
        }
      ]
    }
  ]
}
```

### Validate Header Syntax

```bash
vercel build 2>&1 | grep "headers"
```

### Check for Header Conflicts

Headers are applied in order. Later rules override earlier ones for overlapping source patterns.

### Escape Special Characters in Source

```json
{
  "headers": [
    {
      "source": "/path\\.html",
      "headers": [
        {
          "key": "X-Custom",
          "value": "value"
        }
      ]
    }
  ]
}
```

## Common Mistakes

- Using `Content-Type` as a custom header (Vercel sets this automatically)
- Defining headers for paths that do not exist in the deployment
- Forgetting to escape dots in source patterns (use `\\.` for literal dots)
- Setting `Access-Control-Allow-Origin: *` with credentials, which browsers reject

## Related Pages

- [Vercel Rewrites Loop]({{< relref "/tools/vercel/vercel-rewrites-loop" >}}) -- Rewrite loop detection
- [Vercel Build Error]({{< relref "/tools/vercel/vercel-build-error" >}}) -- Build failures
- [Vercel Regional Config]({{< relref "/tools/vercel/vercel-regional-config" >}}) -- Region configuration
