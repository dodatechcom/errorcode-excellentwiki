---
title: "[Solution] npm ci Error — package-lock out of sync"
description: "Fix npm ci errors. Resolve package-lock.json synchronization issues."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

npm ci fails when the `package-lock.json` is out of sync with `package.json`. This command requires an exact match between the two files.

## Common Causes

- `package.json` was modified without updating `package-lock.json`
- Lock file was manually edited or corrupted
- Different npm versions generated incompatible lock files
- Lock file was not committed to version control

## How to Fix

### Regenerate Lock File

```bash
rm package-lock.json
npm install
```

### Use npm Install Instead

```bash
npm install
```

### Verify Lock File Integrity

```bash
npm ci --ignore-scripts
```

### Check npm Version

```bash
npm --version
```

### Force npm ci

```bash
npm ci --legacy-peer-deps
```

## Examples

```bash
# Example 1: npm ci fails in CI/CD
npm ci
# npm ERR! code EUSAGE
# npm ERR! The package-lock.json is out of date
# Fix: run npm install locally and commit lock file

# Example 2: Regenerate lock file
rm package-lock.json node_modules
npm install
git add package-lock.json
```

## Related Errors

- [npm Integrity Error]({{< relref "/tools/npm/npm-integrity-error" >}}) — integrity check failed
- [npm Cache Error]({{< relref "/tools/npm/npm-cache-error" >}}) — npm cache error
