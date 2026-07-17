---
title: "[Solution] Vercel Rewrites Not Working Error — Fix URL Rewrites"
description: "Fix Vercel rewrite errors. Resolve URL rewrite configuration issues, path matching, and proxy rewrite failures."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["warning"]
weight: 7
---

A Vercel rewrites not working error occurs when your configured URL rewrites are not being applied. Requests go to the original path instead of being rewritten to the target destination.

## What This Error Means

Rewrites in Vercel transparently redirect requests from one path to another without changing the URL in the browser. When they do not work, visitors see 404 errors or the wrong content is served.

## Why It Happens

- The rewrite configuration in vercel.json has incorrect syntax
- The source path pattern does not match the incoming request
- The destination URL is unreachable
- Conflicting rewrite rules override each other
- The rewrite is placed after a more specific route handler
- Framework-level routing conflicts with Vercel rewrites

## How to Fix It

### Configure Rewrites in vercel.json

```json
{
  "rewrites": [
    {
      "source": "/old-page",
      "destination": "/new-page"
    },
    {
      "source": "/blog/:slug",
      "destination": "/articles/:slug"
    },
    {
      "source": "/api/:path*",
      "destination": "https://external-api.com/:path*"
    }
  ]
}
```

### Use Path Match Patterns

```json
{
  "rewrites": [
    {
      "source": "/products/:id(\\d+)",
      "destination": "/product-detail?id=:id"
    },
    {
      "source": "/docs/:slug*",
      "destination": "/documentation/:slug*"
    },
    {
      "source": "/:path((?!api|admin).*)",
      "destination": "/catch-all/:path"
    }
  ]
}
```

### Next.js Rewrites (next.config.js)

```javascript
// next.config.js
module.exports = {
  async rewrites() {
    return [
      {
        source: '/old-path/:path*',
        destination: '/new-path/:path*',
      },
      {
        source: '/external/:path*',
        destination: 'https://api.example.com/:path*',
      },
    ];
  },
};
```

### Test Rewrites

```bash
# Test a rewrite
curl -I https://your-domain.com/old-page

# Check response headers for the rewritten path
curl -v https://your-domain.com/blog/hello-post 2>&1 | grep "< location"

# Use Vercel CLI to test locally
vercel dev
```

### Debug Rewrite Issues

```javascript
// Add debug logging in your route handler
export default function handler(req, res) {
  console.log('Original URL:', req.url);
  console.log('Rewrite source:', req.headers['x-matched-path']);
  res.json({ url: req.url });
}
```

### Check Rewrite Order

```json
{
  "rewrites": [
    {
      "source": "/admin/:path*",
      "destination": "/admin-panel/:path*"
    },
    {
      "source": "/:path*",
      "destination": "/catch-all/:path*"
    }
  ]
}
```

Rewrites are processed in order. More specific patterns should come first.

## Common Mistakes

- Putting catch-all rewrites before specific ones
- Using `*` instead of `:path*` for path matching
- Not testing rewrites locally with `vercel dev`
- Confusing rewrites with redirects (rewrites preserve the URL)
- Forgetting that rewrites do not change the browser URL bar

## Related Pages

- [Vercel Domain Error]({{< relref "/tools/vercel/vercel-domain-error" >}}) — Domain configuration failed
- [Vercel Deploy Error]({{< relref "/tools/vercel/vercel-deploy-error" >}}) — Deployment failed
