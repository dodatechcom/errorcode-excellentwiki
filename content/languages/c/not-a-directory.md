---
title: "[Solution] C Not a directory: ENOTDIR"
description: "Fix C not a directory (ENOTDIR). Verify path components are directories."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["enotdir", "not-a-directory", "path", "errno", "filesystem"]
weight: 5
---

# Not a directory: ENOTDIR

ENOTDIR occurs when a path component that should be a directory is actually a regular file, or when trying to access a file as if it were in a directory path.

## Common Causes

```c
// Cause 1: Path component is a file, not directory
// /home/user/file.txt is a regular file
// Trying to access /home/user/file.txt/subdir
open("/home/user/file.txt/subdir/file.txt", O_RDONLY); // ENOTDIR

// Cause 2: Wrong path separator
open("file.txt/subdir", O_RDONLY); // ENOTDIR

// Cause 3: Symlink points to file, not directory
// symlink("file.txt", "mylink")
// Trying to access mylink/subdir
```

## How to Fix

### Fix 1: Verify path components

```c
struct stat st;
stat("/home/user", &st);
if (!S_ISDIR(st.st_mode)) {
    fprintf(stderr, "Not a directory: /home/user\n");
}
```

### Fix 2: Check path before using

```c
char *path = "/home/user/file.txt/subdir";
// Split and check each component
```

### Fix 3: Use correct paths

```c
int fd = open("/home/user/subdir/file.txt", O_RDONLY);
```

## Related Errors

- [Is a directory]({{< relref "/languages/c/is-a-directory" >}}) — EISDIR.
- [No such file]({{< relref "/languages/c/no-such-file" >}}) — ENOENT.
- [Too many symbolic links]({{< relref "/languages/c/symbolic-link-loop" >}}) — ELOOP.
