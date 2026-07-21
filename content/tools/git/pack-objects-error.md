---
title: "[Solution] Git Pack Objects Error"
description: "Fix Git pack-objects errors when packing repository objects fails during push or clone."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
---

# Git Pack Objects Error

Git pack-objects fails to create or read pack files.

```
error: pack-objects died of signal 13
fatal: index-pack failed
```

## Common Causes

- Insufficient disk space for packing
- Memory limit exceeded
- Corrupted pack file
- Large repository with many objects
- Pack file permissions wrong

## How to Fix

### Repack Repository

```bash
# Repack all objects
git repack -a -d

# Aggressive repack
git repack -a -d -f --depth=250 --window=250
```

### Fix Corrupted Pack

```bash
# Verify pack integrity
git verify-pack -v .git/objects/pack/*.idx

# Remove corrupted packs and re-fetch
rm .git/objects/pack/*.pack
rm .git/objects/pack/*.idx
git fetch origin
```

### Increase Memory for Packing

```bash
# Increase Git memory limit
git config pack.windowMemory 256m
git config pack.packSizeLimit 256m
git config pack.deltaCacheSize 256m
```

### Check Disk Space

```bash
# Check available space
df -h .git

# Clean up unnecessary files
git gc --prune=now
```

## Examples

```bash
# Full repack with garbage collection
git reflog expire --expire=now --all
git gc --prune=now
git repack -a -d

# Check pack file health
ls -lh .git/objects/pack/
git verify-pack -v .git/objects/pack/*.idx | tail -5
```
