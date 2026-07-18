---
title: "[Solution] Poetry Cache Error - Fix Cache Directory Error or Corrupted Cache"
description: "Fix Poetry cache errors and corrupted cache directories. Clear and rebuild Poetry caches to resolve download and resolution failures."
tools: ["poetry"]
error-types: ["cache-error"]
severities: ["error"]
weight: 5
---

This error means Poetry's local cache is corrupted, inaccessible, or full. The cache stores downloaded packages and metadata, and problems here cascade into installation and resolution failures.

## What This Error Means

When Poetry encounters cache problems, you see:

```
CacheError: Unable to create cache directory
# or
FileNotFoundError: [Errno 2] No such file or directory: '...cache...'
# or
JSONDecodeError: Expecting value: line 1 column 1
```

A corrupted cache can cause misleading errors in package resolution because Poetry reads stale or invalid metadata from cached files.

## Why It Happens

- A previous Poetry operation crashed mid-download, leaving partial files
- Disk space ran out while Poetry was writing to the cache
- File permissions changed after a system update or user switch
- Multiple Poetry processes wrote to the cache simultaneously in CI
- A Poetry upgrade changed the cache format and old files are incompatible
- Antivirus software quarantined files in the cache directory

## How to Fix It

### Clear the specific package cache

```bash
poetry cache clear pypi
```

This removes cached metadata and downloads from PyPI.

### Clear all caches

```bash
poetry cache clear --all pypi
rm -rf ~/.cache/pypoetry/
```

Nuclear option that removes everything. Poetry will re-download on next install.

### Check cache directory permissions

```bash
ls -la ~/.cache/pypoetry/
chmod -R u+rwx ~/.cache/pypoetry/
```

Ensure your user owns and can write to the cache directory.

### Rebuild the lock file after clearing cache

```bash
poetry cache clear --all pypi
poetry lock
poetry install
```

Clearing the cache without regenerating the lock can leave stale references.

### Set a different cache directory

```bash
export PYTHON_PACKAGES_CACHE=$HOME/.poetry-cache
poetry install
```

Useful on systems where the default cache path has permission issues.

### Check available disk space

```bash
df -h ~/.cache/pypoetry/
```

Ensure there is enough space for Poetry to write cache files.

### Remove corrupted JSON metadata files

```bash
find ~/.cache/pypoetry/ -name "*.json" -size 0 -delete
poetry install
```

Zero-byte JSON files indicate interrupted writes.

## Common Mistakes

- Running `poetry install` repeatedly when cache is corrupted instead of clearing it first
- Not clearing cache after a Poetry major version upgrade
- Assuming cache errors mean the package does not exist on PyPI
- Sharing cache directories across different users in CI without proper locking
- Forgetting that Poetry cache can grow large and consume significant disk space

## Related Pages

- [Poetry Install Error]({{< relref "/tools/poetry/poetry-install-error" >}}) -- installation failures
- [Poetry Plugin Error]({{< relref "/tools/poetry/poetry-plugin-error" >}}) -- plugin issues
- [Poetry Lock Error]({{< relref "/tools/poetry/poetry-lock-error" >}}) -- lock file problems
