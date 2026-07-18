---
title: "[Solution] Conda Hash Error - Fix Hash Mismatch for Package"
description: "Fix conda hash mismatch errors when downloaded packages do not match expected checksums. Verify integrity and clear corrupted caches."
tools: ["conda"]
error-types: ["hash-error"]
severities: ["error"]
weight: 5
---

This error means the downloaded package file does not match the expected cryptographic hash. conda refuses to install corrupted or tampered packages to protect your environment.

## What This Error Means

conda verifies package integrity using MD5 or SHA-256 hashes stored in channel metadata. When a downloaded package has a different hash than expected, installation stops:

```
HashMismatchError: Hash mismatch for package <name>
Expected: sha256:abc123...
Got: sha256:def456...
```

This prevents you from installing a corrupted download. It can also happen if the channel metadata itself is out of sync with the actual files on the mirror.

## Why It Happens

- A partial or interrupted download left a truncated file in the cache
- A network proxy or CDN modified the package during transit
- The channel mirror is out of sync and serves a different version than its metadata describes
- Disk corruption altered the cached package file
- A man-in-the-middle attack modified the package (rare but possible)
- The package was rebuilt on the channel after your metadata was cached

## How to Fix It

### Clear the package cache and retry

```bash
conda clean --packages
conda install <package>
```

This removes the corrupted download and fetches a fresh copy.

### Clean everything and retry

```bash
conda clean --all
conda install <package>
```

If a metadata mismatch is the issue, clearing the index cache forces a re-download of channel data.

### Verify the download manually

```bash
wget <package_url>
sha256sum <downloaded_file>
```

Compare the output hash to what the channel metadata lists.

### Switch to a different channel mirror

```bash
conda config --remove channels <current_mirror>
conda config --add channels <different_mirror>
conda install <package>
```

A mirror that is out of sync can cause persistent hash mismatches.

### Check disk integrity

```bash
dmesg | grep -i error
smartctl -a /dev/sda
```

Failing storage can silently corrupt files. Rule out hardware issues if hash mismatches recur across different packages.

### Force reinstall from a clean state

```bash
conda remove <package> --force
conda clean --all
conda install <package>
```

## Common Mistakes

- Retrying the same install without clearing the cache, getting the same corrupted file
- Ignoring hash mismatches as transient errors when they indicate disk problems
- Using unreliable mirrors that frequently serve outdated metadata
- Not running `conda clean` after interrupted installs
- Assuming hash mismatches are always network issues without checking disk health

## Related Pages

- [Conda Fetch Error]({{< relref "/tools/conda/conda-fetch-error" >}}) -- network download failures
- [Conda SSL Error]({{< relref "/tools/conda/conda-ssl-error" >}}) -- SSL certificate issues
- [Conda Disk Space]({{< relref "/tools/conda/conda-disk-space" >}}) -- disk space problems
