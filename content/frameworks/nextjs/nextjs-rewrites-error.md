---
title: "[Solution] Next.js Rewrites or Redirects Error — How to Fix"
description: "Fix Next.js rewrites and redirects errors. Resolve URL rewriting, redirect loops, and path configuration issues."
frameworks: ["nextjs"]
error-types: ["configuration-error"]
severities: ["error"]
weight: 5
comments: true
---

A Next.js rewrites or redirects error occurs when URL rewriting or redirect rules fail, create loops, or don't match expected patterns. These are configured in `next.config.js`.

## Why It Happens

Rewrites and redirects are processed at the edge or server level. Errors occur when source and destination patterns are invalid, when permanent redirects loop back on themselves, when rewrite destinations are unreachable, when regex in source patterns is malformed, or when rewrites conflict with existing pages.

## Common Error Messages

```
Error: Invalid redirect: /old → /new has circular reference
```

```
Error: Invalid rewrite: source pattern is malformed
```

```
ERR_TOO_MANY_REDIRECTS
```

```
Error: Rewrites and redirects cannot be empty
```

## How to Fix It

### 1. Configure Redirects Properly

Define redirects in `next.config.js`:

```javascript
// next.config.js
const nextConfig = {
    async redirects() {
        return [
            {
                source: '/old-blog/:slug',
                destination: '/blog/:slug',
                permanent: true,  // 308 status code
            },
            {
                source: '/deprecated',
                destination: '/new-feature',
                permanent: false,  // 307 status code
            },
            {
                source: '/docs/:path*',
                destination: '/documentation/:path*',
                permanent: true,
                has: [
                    {
                        type: 'header',
                        key: 'x-legacy-docs',
                        value: 'true',
                    },
                ],
            },
        ];
    },
};

module.exports = nextConfig;
```

### 2. Configure Rewrites for APIs

Proxy requests to external services:

```javascript
// next.config.js
const nextConfig = {
    async rewrites() {
        return [
            {
                source: '/api/backend/:path*',
                destination: 'https://api.example.com/:path*',
            },
            {
                source: '/proxy/:path*',
                destination: 'https://external-service.com/:path*',
                has: [
                    {
                        type: 'query',
                        key: 'proxy',
                        value: 'true',
                    },
                ],
            },
            // Before page routes
            {
                source: '/blog/:slug',
                destination: '/blog-ssr/:slug',
            },
        ];
    },
};

module.exports = nextConfig;
```

### 3. Use Advanced Matching

Apply conditions to redirects and rewrites:

```javascript
const nextConfig = {
    async redirects() {
        return [
            {
                source: '/:path*',
                destination: '/en/:path*',
                permanent: false,
                has: [
                    {
                        type: 'header',
                        key: 'accept-language',
                        value: '(.*en.*)',  // Regex match
                    },
                ],
                missing: [
                    {
                        type: 'query',
                        key: 'locale',
                    },
                ],
            },
        ];
    },
};

module.exports = nextConfig;
```

### 4. Handle Redirect Loops

Check for circular references:

```javascript
// Wrong: creates a loop
const nextConfig = {
    async redirects() {
        return [
            { source: '/a', destination: '/b', permanent: true },
            { source: '/b', destination: '/a', permanent: true },  // Loop!
        ];
    },
};

// Correct: one-directional
const nextConfig = {
    async redirects() {
        return [
            { source: '/old', destination: '/new', permanent: true },
            // No redirect back from /new to /old
        ];
    },
};
```

## Common Scenarios

**Scenario 1: Redirect creates infinite loop.**
Verify that the destination doesn't match another redirect source. Use browser dev tools to trace redirect chains.

**Scenario 2: Rewrite doesn't match expected URL.**
Check the source pattern. Use `/:path*` for catch-all patterns and test with different URL formats.

**Scenario 3: Redirect loses query parameters.**
Use the destination with `:path*` to preserve query parameters, or configure them explicitly.

## Prevent It

1. **Test redirects with `curl -v -L`** to verify the redirect chain before deployment.

2. **Use `permanent: false` first** during development, then switch to `permanent: true` once verified.

3. **Document all redirect and rewrite rules** for team reference.
