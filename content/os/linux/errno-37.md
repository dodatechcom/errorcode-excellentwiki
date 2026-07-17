---
title: "[Solution] Linux ENAMETOOLONG (errno 37) — File Name Too Long Fix"
description: "Fix Linux ENAMETOOLONG (errno 37) File name too long error. Solutions for path length limit issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux ENAMETOOLONG (errno 37) — File Name Too Long

ENAMETOOLONG (errno 37) means a file name or path component exceeds the maximum allowed length. This error occurs when a single path component (directory or file name) exceeds `NAME_MAX` (typically 255 bytes) or the total path length exceeds `PATH_MAX` (typically 4096 bytes). It is distinct from ELOOP (errno 40) because ENAMETOOLONG refers to length, not link depth.

## Common Causes

- File name exceeds 255 bytes
- Total path length exceeds 4096 bytes
- Deeply nested directory structures
- Generated file names from applications are too long

## How to Fix ENAMETOOLONG

### 1. Check Path Length

Verify the length of the problematic path:

```bash
echo -n "/path/to/file" | wc -c
```

### 2. Shorten the File Name

Rename the file to a shorter name:

```bash
mv /very/long/path/that/exceeds/the/limit/longfilename.txt /shorter/path/short.txt
```

### 3. Find Long File Names in a Directory

Locate files with long names:

```bash
find /path -maxdepth 1 -exec bash -c 'for f; do echo ${#f} "$f"; done' _ {} + | sort -rn | head
```

### 4. Move Files to a Shallower Directory

Reduce directory nesting:

```bash
mv /a/b/c/d/e/file.txt /a/b/file.txt
```

### 5. Increase Path Limits (Temporarily)

Set a longer PATH_MAX for specific applications:

```bash
# Check current limits
getconf PATH_MAX /
```

## Verification

After shortening the path, confirm access works:

```bash
ls -la /new/short/path/file.txt
```

## Related Error Codes

- [ELOOP (errno 40)](/os/linux/errno-40/) — Too many levels of symbolic links
- [ENOENT (errno 2)](/os/linux/errno-2/) — No such file or directory
- [ENOTDIR (errno 20)](/os/linux/errno-20/) — Not a directory
