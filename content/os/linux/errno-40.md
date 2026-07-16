---
title: "[Solution] Linux ELOOP (errno 40) — Too Many Levels of Symbolic Links Fix"
description: "Fix Linux ELOOP (errno 40) Too many levels of symbolic links error. Solutions for symlink loop issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enLOOP", "symlink", "errno-40", "link"]
weight: 5
---

# Linux ELOOP (errno 40) — Too Many Levels of Symbolic Links

ELOOP (errno 40) means too many symbolic links were encountered while resolving a path. This error occurs when symbolic links form a cycle or the chain of links exceeds the kernel's maximum depth (typically 40). It is distinct from ENAMETOOLONG (errno 36) because ELOOP specifically refers to link indirection, not path length.

## Common Causes

- A symbolic link points to itself (self-referencing link)
- A chain of symbolic links creates a cycle (e.g., A -> B -> A)
- Too many nested symbolic links in a path
- A symlink points to a directory that contains a symlink back to the parent

## How to Fix ELOOP

### 1. Detect Symlink Cycles

Use `readlink` or `ls -la` to trace the chain:

```bash
ls -la /path/to/link
readlink -f /path/to/link
```

### 2. Find Circular Links

Use `find` to locate self-referencing or circular links:

```bash
find /path -maxdepth 5 -type l -exec sh -c 'readlink -f "$1"' _ {} \;
```

### 3. Remove Problematic Symlinks

Delete the circular or excessive symlinks:

```bash
rm /path/to/circular_link
```

### 4. Check for Symlink Bait

Some malware creates circular symlinks to cause denial of service:

```bash
find /tmp -maxdepth 3 -type l
```

## Verification

After removing circular links, confirm path resolution works:

```bash
readlink -f /path/to/link
ls /path/to/link/
```

## Related Error Codes

- [ENAMETOOLONG (errno 36)](/os/linux/errno-36/) — File name too long
- [ENOENT (errno 2)](/os/linux/errno-2/) — No such file or directory
- [ENOTDIR (errno 20)](/os/linux/errno-20/) — Not a directory
