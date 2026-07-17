---
title: "[Solution] C Bad file descriptor: EBADF"
description: "Fix C bad file descriptor (EBADF). Use valid file descriptors for I/O operations."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["bad-file-descriptor", "ebadf", "file-descriptor", "errno", "io"]
weight: 5
---

# Bad file descriptor: EBADF

EBADF occurs when you use a file descriptor that is not valid. This can happen when the descriptor was never opened, was already closed, or is not open for the requested operation.

## Common Causes

```c
// Cause 1: Using closed file descriptor
int fd = open("file.txt", O_RDONLY);
close(fd);
read(fd, buf, 100); // EBADF

// Cause 2: Wrong descriptor for operation
int fd = open("file.txt", O_RDONLY);
write(fd, "data", 4); // EBADF — fd is read-only

// Cause 3: Using uninitialized fd
int fd;
read(fd, buf, 100); // EBADF — fd is garbage
```

## How to Fix

### Fix 1: Check fd validity

```c
int fd = open("file.txt", O_RDONLY);
if (fd == -1) {
    perror("open");
    return 1;
}
```

### Fix 2: Don't use closed descriptors

```c
int fd = open("file.txt", O_RDONLY);
// ... use fd ...
close(fd);
// Don't use fd after this
```

### Fix 3: Use correct open flags

```c
// For writing
int fd = open("file.txt", O_WRONLY | O_CREAT, 0644);
```

## Related Errors

- [Too many open files]({{< relref "/languages/c/too-many-open-files" >}}) — EMFILE.
- [Permission denied]({{< relref "/languages/c/permission-denied-file" >}}) — EACCES.
- [No such file]({{< relref "/languages/c/no-such-file" >}}) — ENOENT.
