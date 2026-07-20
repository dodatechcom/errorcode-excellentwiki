---
title: "[Solution] npm Integrity Check Failed"
description: "Fix npm integrity check errors. Resolve package integrity verification failures."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

An npm integrity check failed error occurs when the downloaded package does not match the expected checksum. This indicates potential corruption or tampering.

## Common Causes

- Network interruption during download caused corrupted tarball
- npm registry returned incorrect package content
- Local cache contains corrupted package
- Package was modified after publication
- Mirror registry has stale or incorrect packages

## How to Fix

### Clear npm Cache

```bash
npm cache clean --force
```

### Verify Registry Configuration

```bash
npm config get registry
```

### Reinstall Dependencies

```bash
rm -rf node_modules package-lock.json
npm install
```

### Check Cache Integrity

```bash
npm cache verify
```

### Use Official Registry

```bash
npm config set registry https://registry.npmjs.org/
```

## Examples

```bash
# Example 1: Integrity check failed
npm install
# npm ERR! code EINTEGRITY
# npm ERR! sha512-... integrity checksum failed
# Fix: npm cache clean --force && npm install

# Example 2: Verify cache
npm cache verify
# verified 0 tarballs
```

## Related Errors

- [npm Cache Error]({{< relref "/tools/npm/npm-cache-error" >}}) -- npm cache error
- [npm Tarball Error]({{< relref "/tools/npm/npm-tarball-error" >}}) -- tarball extraction error
