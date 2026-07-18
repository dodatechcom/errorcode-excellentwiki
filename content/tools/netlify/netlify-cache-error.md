---
title: "[Solution] Netlify Cache Error — Fix Build Cache Corrupted or Stale"
description: "Fix Netlify cache errors when the build cache is corrupted or contains stale data. Clear the cache, optimize caching strategies, and resolve incremental build issues."
tools: ["netlify"]
error-types: ["build-error"]
severities: ["warning"]
weight: 5
---

A Netlify cache error occurs when the build cache is corrupted, stale, or contains files that cause build failures. Cached node_modules or build artifacts may be incompatible with the current build environment.

## What This Error Means

Netlify caches dependencies between builds to speed up deployment. When the cache is problematic:

```
Error: Build failed due to corrupted cache
npm ERR! Integrity check failed for <package>
```

## Why It Happens

- The cached node_modules are incompatible with the current Node.js version
- A package in the cache has been updated or yanked from the registry
- The cache contains platform-specific binaries for the wrong architecture
- The cache was built with a different operating system or kernel version
- The cache contains stale build artifacts from a previous framework version
- The cache directory has permission issues
- The cache exceeds the storage limit

## How to Fix It

### Clear the Build Cache from Dashboard

Go to Site > Deploys > Deploy Settings > Build Cache and click Clear Cache.

### Clear Cache via CLI

```bash
netlify deploy --build --clear-cache
```

### Use Environment Variable to Clear Cache

```toml
[build]
  command = "npm run build"
  publish = "dist"

[build.environment]
  NETLIFY_CLEAR_CACHE = "true"
```

### Disable Cache for Specific Packages

```bash
# netlify.toml
[build]
  command = "npm ci --prefer-offline && npm run build"
```

### Configure Cache Manually

```bash
# netlify.toml
[build]
  ignore = "git diff --quiet HEAD^ HEAD .nvmrc .node-version package-lock.json"
```

### Use npm ci Instead of npm install

```toml
[build]
  command = "npm ci && npm run build"
```

## Common Mistakes

- Not clearing the cache after changing Node.js versions
- Ignoring build failures caused by stale cache
- Assuming npm ci always resolves cache issues
- Not using the clear cache option when switching between major dependency versions

## Related Pages

- [Netlify Build Error]({{< relref "/tools/netlify/netlify-build-error" >}}) -- Build failures
- [Netlify Deploy Error]({{< relref "/tools/netlify/netlify-deploy-error" >}}) -- Deploy failures
- [Netlify Plugin Error]({{< relref "/tools/netlify/netlify-plugin-error" >}}) -- Plugin issues
