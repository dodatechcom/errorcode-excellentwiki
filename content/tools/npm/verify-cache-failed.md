---
title: "[Solution] npm cache Verify Failed"
description: "Fix npm cache verify failures by cleaning corrupted entries, checking disk space, and rebuilding the cache metadata from scratch."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm cache Verify Failed

This guide helps you diagnose and resolve npm cache Verify Failed errors encountered when running npm commands.

## Common Causes

- Cache metadata is corrupted or has integrity mismatches
- Disk I/O errors during previous cache write operations
- Cache format is incompatible with current npm version

## How to Fix

### Clean Cache Completely

```bash
rm -rf ~/.npm/_cacache
```

### Check Disk Space

```bash
df -h ~/.npm
```

### Rebuild Cache from Scratch

```bash
npm cache verify && npm install <package>
```

## Examples

```bash
# Corrupted cache metadata
npm cache verify
# Fix: Delete and rebuild cache
rm -rf ~/.npm/_cacache
npm cache verify

# Disk I/O errors
npm cache verify
# Fix: Check disk health and clean
df -h
npm cache clean --force
npm cache verify

```

## Related Errors

- [Clean Cache Failed]({{< relref "/tools/npm/clean-cache-failed" >}}) -- cache clean error
- [Corrupt Cache Entry]({{< relref "/tools/npm/corrupt-cache-entry" >}}) -- corrupted cache
