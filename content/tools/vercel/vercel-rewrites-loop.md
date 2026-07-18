---
title: "[Solution] Vercel Rewrites Loop Error — Fix Infinite Rewrite Loop Detected"
description: "Fix Vercel infinite rewrite loop errors when rewrite rules create a redirect cycle. Debug rewrite patterns and fix conflicting source/destination rules."
tools: ["vercel"]
error-types: ["configuration-error"]
severities: ["error"]
weight: 5
---

A Vercel rewrite loop error occurs when rewrite rules create a cycle where a request is rewritten repeatedly to itself or in a chain that never terminates. The deployment fails or requests hang indefinitely.

## What This Error Means

Vercel detects that a rewrite rule directs a request to a path that triggers the same rewrite again:

```
Error: Infinite rewrite loop detected for path /api/users
```

## Why It Happens

- A rewrite source matches the destination path, creating a loop
- Multiple rewrite rules chain into each other without a terminal
- The source pattern is too broad and matches all paths including the destination
- A redirect points back to the same path without a condition to break the cycle
- The `has` or `missing` conditions do not prevent the loop
- A trailing slash rule causes the rewrite to match itself repeatedly

## How to Fix It

### Debug Rewrite Rules

```bash
vercel build --debug | grep "rewrite"
vercel inspect <deployment-url> --logs
```

### Add Conditions to Prevent Loops

```json
{
  "rewrites": [
    {
      "source": "/api/users",
      "destination": "/api/users-list",
      "has": [
        {
          "type": "header",
          "key": "x-original-path",
          "value": "^(?!.*api/users-list).*$"
        }
      ]
    }
  ]
}
```

### Use Specific Source Patterns

```json
{
  "rewrites": [
    // Avoid:
    { "source": "/(.*)", "destination": "/index.html" },
    // Instead, use:
    { "source": "/((?!api/).*)", "destination": "/index.html" }
  ]
}
```

### Break Circular Chains

```json
{
  "rewrites": [
    { "source": "/old-path", "destination": "/new-path" },
    // Do NOT add: { "source": "/new-path", "destination": "/old-path" }
  ]
}
```

### Use Redirect Instead of Rewrite

```json
{
  "redirects": [
    {
      "source": "/old-path",
      "destination": "/new-path",
      "permanent": true
    }
  ]
}
```

### Add Terminal Conditions

```json
{
  "rewrites": [
    {
      "source": "/app/(.*)",
      "destination": "/app-shell.html",
      "missing": [
        {
          "type": "file",
          "value": "/app/$1"
        }
      ]
    }
  ]
}
```

## Common Mistakes

- Creating rewrites where source and destination match the same pattern
- Using wildcard `(.*)` patterns that match all routes including destinations
- Chaining rewrites without a terminal condition or base case
- Not testing rewrite rules locally before deployment

## Related Pages

- [Vercel Rewrite Error]({{< relref "/tools/vercel/vercel-rewrite-error" >}}) -- Rewrite configuration
- [Vercel Headers Error]({{< relref "/tools/vercel/vercel-headers-error" >}}) -- Headers configuration
- [Vercel Build Error]({{< relref "/tools/vercel/vercel-build-error" >}}) -- Build failures
