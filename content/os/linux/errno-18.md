---
title: "[Solution] Linux EXDEV (errno 18) — Invalid Cross-Device Link Fix"
description: "Fix Linux EXDEV (errno 18) Invalid cross-device link error. Solutions for cross-device move and rename issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["exdev", "cross-device", "errno-18", "rename", "link"]
weight: 5
---

# Linux EXDEV (errno 18) — Invalid Cross-Device Link

EXDEV (errno 18) means you attempted to move or link a file across different filesystems or devices. This error occurs when `mv` or `link` is called on files that reside on separate mount points, as hard links cannot span devices. It is distinct from EMLINK (errno 31) because EXDEV specifically involves different devices, not too many links.

## Common Causes

- Attempting to `mv` a file across different mount points
- Trying to create a hard link between files on different filesystems
- Moving files between partitions without using copy-and-delete
- Renaming files across filesystem boundaries

## How to Fix EXDEV

### 1. Check Mount Points

Verify which filesystems the source and destination are on:

```bash
df /path/to/source
df /path/to/destination
```

### 2. Use Copy and Delete Instead of Move

Replace `mv` with a copy-then-delete approach:

```bash
cp -a /path/to/source/file /path/to/destination/file
rm /path/to/source/file
```

### 3. Use rsync for Large Transfers

For large files or directories, use rsync with remove-source-files:

```bash
rsync -av --remove-source-files /path/to/source/ /path/to/destination/
```

### 4. Use Symbolic Links Instead of Hard Links

If you need a link across devices, use a symbolic link:

```bash
ln -s /path/to/source/file /path/to/destination/file
```

## Verification

After copying, confirm the file exists at both locations:

```bash
ls -la /path/to/source/file
ls -la /path/to/destination/file
```

## Related Error Codes

- [EMLINK (errno 31)](/os/linux/errno-31/) — Too many links
- [ENOENT (errno 2)](/os/linux/errno-2/) — No such file or directory
- [EACCES (errno 13)](/os/linux/errno-13/) — Permission denied
