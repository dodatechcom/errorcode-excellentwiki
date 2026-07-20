---
title: "[Solution] npm install EBADENGINE Engine Mismatch"
description: "Fix EBADENGINE engine mismatch errors in npm install by updating Node.js, configuring engine strictness, or using nvm for version management."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install EBADENGINE Engine Mismatch

This guide helps you diagnose and resolve npm install EBADENGINE Engine Mismatch errors encountered when running npm commands.

## Common Causes

- Package requires a different Node.js or npm version than installed
- engines field in package.json is too restrictive for your environment
- System Node.js version is outdated for the requested package

## How to Fix

### Check Current Node Version

```bash
node --version && npm --version
```

### Update Node.js to Required Version

```bash
nvm install <required-version> && nvm use <required-version>
```

### Bypass Engine Check

```bash
npm install --engine-strict=false
```

## Examples

```bash
# Package requires Node 18+
npm install package-needing-node18
# Fix: Update Node.js
nvm install 18
nvm use 18

# Strict engine check failing
npm install modern-pkg
# Fix: Bypass engine check
npm config set engine-strict false

```

## Related Errors

- [Lifecycle Error]({{< relref "/tools/npm/lifecycle-error" >}}) -- script failure
- [ESM Require Error]({{< relref "/tools/npm/err-require-esm-esm-require-error" >}}) -- ESM compatibility
