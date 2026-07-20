---
title: "[Solution] npm install EINTEGRITY Integrity Check Failed"
description: "Resolve EINTEGRITY integrity check failures in npm install by clearing cache, verifying checksums, and ensuring registry trust."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install EINTEGRITY Integrity Check Failed

This guide helps you diagnose and resolve npm install EINTEGRITY Integrity Check Failed errors encountered when running npm commands.

## Common Causes

- Cached package tarball is corrupted or tampered with
- Registry returned a different package hash than expected
- Network issue caused partial download during previous install

## How to Fix

### Clear npm Cache for the Package

```bash
npm cache clean --force
```

### Delete Package-lock and Reinstall

```bash
rm package-lock.json && npm install
```

### Verify Registry Integrity

```bash
npm config get registry
```

## Examples

```bash
# Corrupted cached tarball
npm install moment
# Fix: Clear cache and reinstall
npm cache clean --force
rm package-lock.json
npm install moment

# Registry mismatch
npm install lodash
# Fix: Verify and switch registry
npm config get registry
npm config set registry https://registry.npmjs.org

```

## Related Errors

- [Corrupt Cache Entry]({{< relref "/tools/npm/corrupt-cache-entry" >}}) -- corrupted cache
- [Module Not Found]({{< relref "/tools/npm/module-not-found" >}}) -- missing module
