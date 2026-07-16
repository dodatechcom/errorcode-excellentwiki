---
title: "[Solution] C errno EMFILE — Too many open files Fix"
description: "Fix C EMFILE (Too many open files) by closing unused descriptors, increasing limits, and using file descriptor pools."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["emfile", "too-many-open-files", "file-descriptor-limit", "ulimit"]
weight: 5
---

# [Solution] C errno EMFILE — Too many open files Fix

When a process has reached its limit on the number of file descriptors it can have open simultaneously, a new `open()`, `socket()`, or `pipe()` call fails and sets `errno` to `EMFILE`. This is a per-process limit enforced by the kernel.

## Common Causes

- The process has opened too many files, sockets, or pipes without closing them (file descriptor leak).
- The per-process file descriptor limit (`ulimit -n` or `RLIMIT_NOFILE`) is too low.
- A long-running server accumulates descriptors from client connections.
- Shared libraries or third-party code open files without closing them.

## How to Fix

Close unused file descriptors promptly and increase the per-process limit if needed. Use `getrlimit()` and `setrlimit()` to adjust limits programmatically.

```c
#include <sys/resource.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    struct rlimit rl;
    if (getrlimit(RLIMIT_NOFILE, &rl) == -1) {
        fprintf(stderr, "getrlimit failed: %s\n", strerror(errno));
        return 1;
    }
    printf("Current limit: %lu\n", rl.rlim_cur);
    printf("Max limit: %lu\n", rl.rlim_max);

    rl.rlim_cur = 4096;
    if (setrlimit(RLIMIT_NOFILE, &rl) == -1) {
        fprintf(stderr, "setrlimit failed: %s\n", strerror(errno));
        return 1;
    }
    printf("New limit: %lu\n", rl.rlim_cur);
    return 0;
}
```

## Examples

Exhausting file descriptors in a loop:

```c
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int fds[1024];
    int count = 0;
    for (int i = 0; i < 1024; i++) {
        fds[i] = open("/dev/null", O_RDONLY);
        if (fds[i] == -1) {
            perror("open");  // "open: Too many open files"
            fprintf(stderr, "errno: %d (EMFILE)\n", errno);
            break;
        }
        count++;
    }
    for (int i = 0; i < count; i++) close(fds[i]);
    return 0;
}
```

## Related Errors

- [errno-24 ENFILE](/languages/c/errno-emfile/) — too many open files in system.
- [errno-11 EAGAIN](/languages/c/errno-emfile/) — resource unavailable, try again.
- [errno-23 EMFILE](/languages/c/errno-emfile/) — too many open files.
