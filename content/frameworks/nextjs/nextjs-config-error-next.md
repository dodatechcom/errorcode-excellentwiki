---
title: "[Solution] Next.js next.config.js Misconfiguration Error -- How to Fix"
description: "Fix Next.js configuration errors. Resolve next.config.js misconfiguration, build options, and plugin issues."
frameworks: ["nextjs"]
error-types: ["configuration-error"]
severities: ["error"]
weight: 5
comments: true
---

A Next.js next.config.js misconfiguration error occurs when the configuration file contains invalid options, deprecated settings, or incompatible combinations. The config file controls build, server, and rendering behavior.

## Why It Happens

`next.config.js` (or `next.config.mjs`) controls many aspects of Next.js. Errors occur when using deprecated options, when options have wrong data types, when `experimental` features are misconfigured, when `webpack` configuration conflicts with built-in features, or when the config uses CommonJS `require` in an ESM project.

## Common Error Messages

```
Error: Option "rewrites" is not allowed to be empty
```

```
Error: Invalid configuration object: "images" has unknown property 'domains'
```

```
Error: Cannot use the "env" key in next.config.js
```

```
Error: The "appDir" option is no longer needed as it is the default
```

## How to Fix It

### 1. Use Valid Configuration Options

Reference the latest Next.js configuration:

```javascript
// next.config.js (CommonJS)
/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    images: {
        remotePatterns: [
            {
                protocol: 'https',
                hostname: 'example.com',
            },
        ],
        formats: ['image/avif', 'image/webp'],
    },
    headers: async () => [
        {
            source: '/api/:path*',
            headers: [
                { key: 'Access-Control-Allow-Origin', value: '*' },
            ],
        },
    ],
    redirects: async () => [
        {
            source: '/old-path',
            destination: '/new-path',
            permanent: true,
        },
    ],
    rewrites: async () => [
        {
            source: '/api/:path*',
            destination: 'https://backend.example.com/:path*',
        },
    ],
};

module.exports = nextConfig;
```

### 2. Configure TypeScript and ESLint

Set up tooling options:

```javascript
// next.config.js
const nextConfig = {
    typescript: {
        ignoreBuildErrors: false,  // Set to true only if absolutely necessary
    },
    eslint: {
        ignoreDuringBuilds: false,
    },
    // Output standalone for Docker
    output: 'standalone',
};

module.exports = nextConfig;
```

### 3. Configure Headers and Redirects

Add custom headers and redirects:

```javascript
// next.config.js
const nextConfig = {
    async headers() {
        return [
            {
                source: '/(.*)',
                headers: [
                    { key: 'X-Frame-Options', value: 'DENY' },
                    { key: 'X-Content-Type-Options', value: 'nosniff' },
                    { key: 'Referrer-Policy', value: 'origin-when-cross-origin' },
                ],
            },
        ];
    },
    async redirects() {
        return [
            {
                source: '/blog/:slug',
                destination: '/posts/:slug',
                permanent: true,
            },
        ];
    },
};

module.exports = nextConfig;
```

### 4. Migrate to ESM Config

Use `next.config.mjs` for ES module syntax:

```javascript
// next.config.mjs
const nextConfig = {
    reactStrictMode: true,
    images: {
        remotePatterns: [
            {
                protocol: 'https',
                hostname: 'example.com',
            },
        ],
    },
};

export default nextConfig;
```

## Common Scenarios

**Scenario 1: Build fails with "unknown property" error.**
Check that you're using the correct property name and that it's not nested incorrectly. Some options have been renamed between versions.

**Scenario 2: Headers don't apply to API routes.**
Ensure the `source` pattern matches the API route. Use `/api/:path*` for all API routes.

**Scenario 3: Config changes don't take effect.**
Restart the development server after modifying `next.config.js`. Changes are not hot-reloaded.

## Prevent It

1. **Validate config with TypeScript** using `@types/node` for better IDE support.

2. **Check the Next.js docs** for your specific version before adding new options.

3. **Use `next.config.mjs`** for ESM syntax support.
