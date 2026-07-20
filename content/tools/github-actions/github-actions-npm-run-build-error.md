---
title: "[Solution] GitHub Actions NPM Run Build Error"
description: "Fix GitHub Actions npm run build failures in CI workflow."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Build errors occur when `npm run build` fails in the workflow:

```
Error: Build failed with 2 errors
src/index.ts(1,20): error TS2307: Cannot find module 'lodash'
```

## Common Causes

- Dependencies not installed before build.
- TypeScript compilation errors.
- Missing environment variables needed at build time.

## How to Fix

**Set build environment variables:**

```yaml
env:
  NODE_OPTIONS: "--max-old-space-size=4096"
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
  - run: npm ci
  - run: npm run build
```

## Examples

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
  - run: npm ci
  - run: npm run build
    env:
      NODE_OPTIONS: "--max-old-space-size=4096"
```
