---
title: "[Solution] C errno 24 EMFILE — Too many open files"
description: "Fix C errno 24 EMFILE (Too many open files) by closing unused file descriptors, increasing limits with ulimit, or using file descriptor pools."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno 24 EMFILE — Too many open files

Too many open files occurs when a system call fails and sets `errno` to 24. This error indicates that the requested operation cannot be performed due to the specific condition described by EMFILE.

## Common Causes

- Opening more file descriptors than the process limit (ulimit -n).
- Leaking file descriptors by not closing them after use.
- Creating many threads or processes each with open files.
- Reaching the system-wide limit on open file descriptors.

## How to Fix

```c
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int fds[1024];
    int i;
    for (i = 0; i < 1024; i++) {
        fds[i] = open("/dev/null", O_RDONLY);
        if (fds[i] == -1) {
            fprintf(stderr, "open failed at %d: %s (errno %d)\n", i, strerror(errno), errno);
            break;
        }
    }
    // Close opened files
    for (int j = 0; j < i; j++) {
        close(fds[j]);
    }
    return 0;
}
```

## Examples

```c
#include <sys/resource.h>
#include <stdio.h>

int main(void) {
    struct rlimit rl;
    getrlimit(RLIMIT_NOFILE, &rl);
    printf("Soft limit: %ld\n", rl.rlim_cur);
    printf("Hard limit: %ld\n", rl.rlim_max);
    return 0;
}
```

## Related Errors

- [errno-11 EAGAIN]({{< relref "/languages/c/errno-11" >}}) — resource unavailable.
- [errno-24 EMFILE]({{< relref "/languages/c/errno-24" >}}) — too many open files (self).
- [errno-12 ENOMEM]({{< relref "/languages/c/errno-12" >}}) — cannot allocate memory.
