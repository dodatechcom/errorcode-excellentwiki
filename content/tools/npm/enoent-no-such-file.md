---
title: "[Solution] npm install ENOENT No Such File"
description: "Handle ENOENT no such file errors during npm install caused by missing dependencies, corrupted cache, or broken symlinks."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install ENOENT No Such File

This guide helps you diagnose and resolve npm install ENOENT No Such File errors encountered when running npm commands.

## Common Causes

- Referenced file or directory does not exist in the package
- Broken symlinks in node_modules pointing to deleted packages
- Corrupted npm cache contains stale or incomplete entries

## How to Fix

### Clear npm Cache and Reinstall

```bash
npm cache clean --force && rm -rf node_modules && npm install
```

### Verify package.json Integrity

```bash
cat package.json | python3 -m json.tool
```

### Reinstall from Scratch

```bash
rm -rf node_modules package-lock.json && npm install
```

## Examples

```bash
# ENOENT during postinstall
npm install sharp
# Fix: Clear cache and retry
npm cache clean --force
npm install sharp

# Missing file in dependency
npm install webpack
# Fix: Full clean reinstall
rm -rf node_modules package-lock.json
npm cache clean --force
npm install

```

## Related Errors

- [Module Not Found]({{< relref "/tools/npm/module-not-found" >}}) -- missing module
- [Corrupt Cache Entry]({{< relref "/tools/npm/corrupt-cache-entry" >}}) -- corrupted cache
