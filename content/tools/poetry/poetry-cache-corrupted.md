---
title: "[Solution] Poetry Cache Corrupted -- Fix Broken Package Cache"
description: "Fix Poetry cache corrupted errors when the local package cache contains damaged or incomplete files. Clear and rebuild the cache."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry's local package cache contains corrupted, incomplete, or mismatched files. Operations like install or update fail with hash or extraction errors.

## Common Causes

- An interrupted download left partial files in the cache
- Disk write was not flushed before system shutdown
- Another process modified cache files
- Cache directory permissions changed

## How to Fix

### 1. Clear the Entire Cache

```bash
poetry cache clear --all pypi
```

### 2. Clear All Cache Directories

```bash
rm -rf $(poetry config cache-dir)/pypoetry/cache
rm -rf $(poetry config cache-dir)/pypoetry/artifacts
poetry install
```

### 3. Rebuild from Scratch

```bash
poetry cache clear --all .
poetry cache clear --all pypi
poetry install -vvv
```

### 4. Check Cache Directory Permissions

```bash
ls -la $(poetry config cache-dir)
chmod -R u+w $(poetry config cache-dir)
```

## Examples

```bash
$ poetry install
HashMismatchError: Hashes did not match for wheel download

$ poetry cache clear --all pypi
Cleared poetry cache (245 MB)

$ poetry install
Installing dependencies from lock file...
```
