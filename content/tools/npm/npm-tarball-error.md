---
title: "[Solution] npm Tarball Extraction Error"
description: "Fix npm tarball extraction errors. Resolve package tarball extraction failures."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

An npm tarball extraction error occurs when npm cannot extract the downloaded package tarball. The tarball may be corrupted or incomplete.

## Common Causes

- Incomplete download due to network issues
- Corrupted npm cache
- Disk space full during extraction
- File system does not support required operations
- Antivirus software interfering with extraction

## How to Fix

### Clear npm Cache

```bash
npm cache clean --force
```

### Check Disk Space

```bash
df -h
```

### Retry Installation

```bash
rm -rf node_modules package-lock.json
npm install
```

### Check File System

```bash
mount | grep $(df . | tail -1 | awk '{print $1}')
```

### Disable Antivirus Temporarily

```bash
# Temporarily disable antivirus and retry
npm install
```

## Examples

```bash
# Example 1: Extraction failed
npm install
# npm ERR! code Z_EEXIST
# npm ERR! tarball extraction failed
# Fix: npm cache clean --force && npm install

# Example 2: Disk full
npm install
# npm ERR! code ENOSPC
# Fix: free disk space and retry
```

## Related Errors

- [npm Integrity Error]({{< relref "/tools/npm/npm-integrity-error" >}}) -- integrity check failed
- [npm Cache Error]({{< relref "/tools/npm/npm-cache-error" >}}) -- npm cache error
