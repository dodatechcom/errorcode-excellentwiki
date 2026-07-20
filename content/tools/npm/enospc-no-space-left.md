---
title: "[Solution] npm install ENOSPC No Space Left on Device"
description: "Fix ENOSPC no space left on device errors during npm install by freeing disk space and cleaning npm cache and temp files."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install ENOSPC No Space Left on Device

This guide helps you diagnose and resolve npm install ENOSPC No Space Left on Device errors encountered when running npm commands.

## Common Causes

- Disk partition hosting node_modules is full
- npm cache has accumulated excessive storage
- System temp directory is full of stale files

## How to Fix

### Clean npm Cache

```bash
npm cache clean --force
```

### Remove node_modules and Reinstall

```bash
rm -rf node_modules && npm install
```

### Check Disk Usage

```bash
df -h && du -sh node_modules
```

## Examples

```bash
# Disk full during install
npm install @angular/cli
# Fix: Free space
npm cache clean --force
du -sh ~/.npm

# Temp directory full
npm install
# Fix: Clean temp directory
rm -rf /tmp/npm-*
npm cache clean --force

```

## Related Errors

- [Corrupt Cache Entry]({{< relref "/tools/npm/corrupt-cache-entry" >}}) -- corrupted cache
- [Clean Cache Failed]({{< relref "/tools/npm/clean-cache-failed" >}}) -- cache clean error
