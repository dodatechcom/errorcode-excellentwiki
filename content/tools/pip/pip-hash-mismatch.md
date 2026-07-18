---
title: "[Solution] pip Hash Mismatch Error — Fix Wheel Hash Verification Failure"
description: "Fix pip hash mismatch errors when the downloaded wheel does not match the expected checksum. Clear cache, verify URLs, and update requirements hashes."
tools: ["pip"]
error-types: ["hash-error"]
severities: ["error"]
weight: 5
---

This error means the downloaded package does not match the cryptographic hash specified in your requirements file. pip refuses to install to protect against corrupted or tampered packages.

## What This Error Means

When you pin packages with hashes in `requirements.txt`, pip verifies every download against the expected SHA-256 digest:

```
ERROR: Hash mismatch for package==1.0.0 (from https://files.pythonhosted.org/...)
Expected sha256=abc123...
Got      sha256=def456...
```

## Why It Happens

- The package maintainer uploaded a new version of the same release (a re-cut)
- The download was corrupted mid-transfer by a proxy or network issue
- A stale wheel in pip's local cache has a different hash than expected
- A mirror or custom index serves a different build of the package
- The requirement file has outdated hashes from an older version

## How to Fix It

### Clear the Cache and Re-download

```bash
pip cache purge
pip install -r requirements.txt
```

### Regenerate Hashes with pip-tools

```bash
pip install pip-tools
pip-compile --generate-hashes requirements.in -o requirements.txt
```

### Manually Update Hashes for a Single Package

```bash
pip install --no-deps --require-hashes --only-binary :all: <package>==1.0.0
hash=$(pip hash <package>.whl)
# Update the hash in requirements.txt
```

### Skip Hash Verification Temporarily (Debug Only)

```bash
pip install --no-hashes -r requirements.txt
```

### Check PyPI for the Correct Hashes

Visit the package page on PyPI and compare the file digests listed there.

## Common Mistakes

- Regenerating hashes without verifying the package comes from a trusted source
- Using `--no-hashes` permanently instead of updating the hash values
- Not clearing the local cache before re-verifying hashes
- Pinning hashes from a mirror that serves different builds than PyPI

## Related Pages

- [pip Cache Error]({{< relref "/tools/pip/pip-cache-error" >}}) -- cache corruption
- [pip Install Error]({{< relref "/tools/pip/pip-install-error" >}}) -- install failures
- [pip Dependency Conflict]({{< relref "/tools/pip/pip-dependency-conflict" >}}) -- dependency issues
