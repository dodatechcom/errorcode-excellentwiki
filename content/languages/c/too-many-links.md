---
title: "[Solution] C Too many links: EMLINK"
description: "Fix C too many links (EMLINK). Reduce hard links or increase filesystem limits."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Too many links: EMLINK

EMLINK occurs when creating a hard link would exceed the maximum number of links for a file, or the directory would have too many entries.

## Common Causes

```c
// Cause 1: Too many hard links
for (int i = 0; i < 100000; i++) {
    char name[64];
    snprintf(name, sizeof(name), "link_%d", i);
    link("original.txt", name); // EMLINK when limit reached
}

// Cause 2: Directory too full
// ext4 limits directory entries

// Cause 3: Filesystem link limit
```

## How to Fix

### Fix 1: Use symbolic links instead

```c
symlink("original.txt", "mylink"); // no link count limit
```

### Fix 2: Organize into subdirectories

```bash
mkdir -p subdir1/subdir2
mv files into subdirectories
```

### Fix 3: Check current link count

```bash
stat file.txt  # shows link count
ls -li file.txt
```

## Related Errors

- [No space left]({{< relref "/languages/c/no-space-left" >}}) — ENOSPC.
- [Too many open files]({{< relref "/languages/c/too-many-open-files" >}}) — EMFILE.
- [No such file]({{< relref "/languages/c/no-such-file" >}}) — ENOENT.
