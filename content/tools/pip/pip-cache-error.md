---
title: "[Solution] pip Cache Error — Fix Cache Corruption and Cleanup Issues"
description: "Fix pip cache errors caused by corrupted download cache or stale wheel files. Clear and repair the pip cache to resolve broken installations with ease."
tools: ["pip"]
error-types: ["cache-error"]
severities: ["warning"]
weight: 5
---

This error means pip's local download cache contains corrupted, incomplete, or incompatible files. pip tries to reuse cached downloads but finds them unusable, causing install failures or unexpected behavior.

## What This Error Means

pip stores downloaded packages in `~/.cache/pip` (Linux), `~/Library/Caches/pip` (macOS), or `%LOCALAPPDATA%\pip\Cache` (Windows). When cache files become corrupted -- from interrupted downloads, disk errors, or partial writes -- pip either fails to unpack them or installs a broken package. Typical messages include:

```
ERROR: Could not install packages due to an OSError
ERROR: wheels cannot be installed since the directory is corrupt
WARNING: pip is configured with locations that require TLS/SSL, however the ssl module is not available
```

## Why It Happens

- A previous pip install was interrupted (Ctrl+C, power loss, OOM kill)
- Disk corruption damaged cached wheel files
- A proxy intercepted and modified the download mid-stream
- Two pip processes wrote to the cache simultaneously
- The cache directory permissions were changed by a `sudo` install

## How to Fix It

### Clear the Entire Cache

```bash
pip cache purge
```

If `pip cache` is not available (older pip):

```bash
rm -rf ~/.cache/pip
```

### Remove Only Broken Wheels

```bash
pip cache remove <package-name>
```

### Check Cache Location and Size

```bash
pip cache dir
pip cache info
```

This shows you where the cache lives and how much space it uses.

### Disable Caching Temporarily

When debugging, bypass the cache entirely:

```bash
pip install <package> --no-cache-dir
```

### Fix Cache Permissions After Sudo

If a root install corrupted the cache:

```bash
sudo chown -R $(whoami) $(pip cache dir)
```

### Verify Wheel Integrity After Re-download

After clearing the cache, reinstall and verify:

```bash
pip cache purge
pip install <package>
pip show <package>
```

## Common Mistakes

- Running `sudo pip install` which writes cache as root and breaks normal user access
- Not clearing cache after a disk-full error during install
- Using `--no-cache-dir` permanently instead of fixing the underlying corruption
- Ignoring repeated install failures that point to cache corruption

## Related Pages

- [pip Install Error]({{< relref "/tools/pip/pip-install-error" >}}) -- environment errors during install
- [pip Permission Denied]({{< relref "/tools/pip/pip-permission-denied" >}}) -- permission errors
- [pip Virtualenv Error]({{< relref "/tools/pip/pip-virtualenv-error" >}}) -- virtualenv issues
