---
title: "[Solution] Linux EFBIG (errno 27) — File Too Large Fix"
description: "Fix Linux EFBIG (errno 27) File too large error. Solutions for file size limit issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enFBIG", "file", "errno-27", "size"]
weight: 5
---

# Linux EFBIG (errno 27) — File Too Large

EFBIG (errno 27) means the file size exceeds the maximum allowed for the filesystem or process. This error occurs when you try to create or extend a file beyond the filesystem's maximum file size limit. It is distinct from ENOSPC (errno 28) because EFBIG refers to the file size limit, not available disk space.

## Common Causes

- The file exceeds the maximum size supported by the filesystem (e.g., ext3's 2TB limit for single files)
- The file is being written to a filesystem with a file size quota
- A 32-bit process trying to handle files larger than 2GB
- Log files or data files growing beyond filesystem constraints

## How to Fix EFBIG

### 1. Check Filesystem Type and Limits

Identify the filesystem and its maximum file size:

```bash
df -Th /path/to/file
stat -f /path/to/file
```

### 2. Upgrade to a Larger Filesystem

Migrate to a filesystem that supports larger files:

```bash
# Convert ext3 to ext4 for larger file support
sudo tune2fs -O extents,uninit_bg,dir_index,has_journal /dev/sda1
sudo e2fsck -f /dev/sda1
```

### 3. Split Large Files

Divide the file into smaller chunks:

```bash
split -b 1G large_file.bin part_
```

### 4. Check Disk Space

Ensure there is enough space and no quotas are preventing the write:

```bash
df -h
quota -s
```

## Verification

After addressing the size limit, confirm the file can be written:

```bash
ls -lh /path/to/file
```

## Related Error Codes

- [ENOSPC (errno 28)](/os/linux/errno-28/) — No space left on device
- [EOVERFLOW (errno 75)](/os/linux/errno-75/) — Value too large for defined data type
- [EMFILE (errno 24)](/os/linux/errno-24/) — Too many open files
