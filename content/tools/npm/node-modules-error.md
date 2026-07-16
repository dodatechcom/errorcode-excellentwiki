---
title: "[Solution] npm node_modules Error — module resolution failed"
description: "Fix npm node_modules issues. Resolve module resolution and dependency installation problems."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["node-modules-error", "node-modules", "module", "resolution", "npm"]
weight: 5
---

# npm node_modules Error — module resolution failed

node_modules errors occur when packages are missing, corrupted, or incorrectly installed. This causes import/require failures at runtime.

## Common Causes

- node_modules directory is incomplete or corrupted
- Package was not installed properly
- Different package manager was used
- Node version incompatibility

## How to Fix

### Clean Install

```bash
rm -rf node_modules package-lock.json
npm install
```

### Use npm ci for Clean Install

```bash
npm ci
```

### Verify node_modules

```bash
ls node_modules | head -20
```

### Check Package Lock

```bash
npm ls
```

### Force Rebuild

```bash
npm rebuild
```

### Check Node Version

```bash
node -v
nvm use <version>
```

## Examples

```bash
# Example 1: Missing module
node app.js
# Error: Cannot find module 'express'
# Fix: rm -rf node_modules package-lock.json && npm install

# Example 2: Corrupted node_modules
npm install
# npm ERR! code EEXIST
# Fix: rm -rf node_modules && npm install

# Example 3: Version mismatch
npm ls
# UNMET DEPENDENCY express@^4.18.0
# Fix: npm install
```

## Related Errors

- [Workspace Error]({{< relref "/tools/npm/workspace-error" >}}) — workspace configuration issues
- [Cache Error]({{< relref "/tools/npm/cache-error" >}}) — npm cache corruption
