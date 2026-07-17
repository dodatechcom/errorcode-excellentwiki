---
title: "[Solution] C Too many open files: EMFILE"
description: "Fix C too many open files (EMFILE). Manage file descriptor limits and close unused descriptors."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Too many open files: EMFILE

EMFILE occurs when a process has opened the maximum number of file descriptors allowed. Each `open()`, `socket()`, or `pipe()` call consumes a descriptor.

## Common Causes

```c
// Cause 1: Leaking file descriptors
for (int i = 0; i < 10000; i++) {
    int fd = open("file.txt", O_RDONLY);
    // forgot to close fd
}

// Cause 2: Not closing descriptors in error paths
int fd = open("file.txt", O_RDONLY);
if (error) {
    return -1; // fd leaked
}
close(fd);

// Cause 3: Too many sockets open
for (int i = 0; i < 10000; i++) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    // forgot to close
}
```

## How to Fix

### Fix 1: Close all descriptors

```c
for (int i = 0; i < 10000; i++) {
    int fd = open("file.txt", O_RDONLY);
    // ... use fd ...
    close(fd);
}
```

### Fix 2: Use RAII-like pattern

```c
int fd = open("file.txt", O_RDONLY);
if (fd == -1) return -1;

int result = do_work(fd);
close(fd); // always close
return result;
```

### Fix 3: Increase limit

```bash
ulimit -n 65535
```

## Related Errors

- [Bad file descriptor]({{< relref "/languages/c/bad-file-descriptor" >}}) — EBADF.
- [Too many links]({{< relref "/languages/c/too-many-links" >}}) — EMLINK.
- [No space left]({{< relref "/languages/c/no-space-left" >}}) — ENOSPC.
