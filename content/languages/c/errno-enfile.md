---
title: "[Solution] C errno ENFILE — Too many open files in system Fix"
description: "Fix C ENFILE (Too many open files in system) by reducing system-wide file usage and tuning kernel limits."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ENFILE — Too many open files in system Fix

When the entire system has reached its maximum number of open file descriptors, a new `open()`, `socket()`, or `pipe()` call fails and sets `errno` to `ENFILE`. Unlike `EMFILE` (per-process limit), `ENFILE` is a system-wide limit affecting all processes.

## Common Causes

- Too many processes on the system collectively have too many open files.
- The system-wide file descriptor limit (`/proc/sys/fs/file-max`) is exhausted.
- A runaway process has leaked thousands of file descriptors.
- The kernel's file descriptor pool is exhausted due to high server loads.

## How to Fix

Check and increase the system-wide file descriptor limit. Reduce the number of open files across processes.

```bash
# Check current system-wide limit
cat /proc/sys/fs/file-max

# Increase the limit temporarily
echo 65536 > /proc/sys/fs/file-max

# Make it persistent via sysctl
sysctl -w fs.file-max=65536
```

```c
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <fcntl.h>

int main(void) {
    FILE *fp = fopen("/proc/sys/fs/file-max", "r");
    if (fp == NULL) {
        fprintf(stderr, "fopen failed: %s\n", strerror(errno));
        return 1;
    }
    long max_files;
    fscanf(fp, "%ld", &max_files);
    fclose(fp);
    printf("System file-max: %ld\n", max_files);
    return 0;
}
```

## Examples

When the system limit is reached:

```c
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    // Simulated — would fail with ENFILE when system limit reached
    int fd = open("/dev/null", O_RDONLY);
    if (fd == -1) {
        if (errno == ENFILE) {
            fprintf(stderr, "System-wide file limit reached\n");
            fprintf(stderr, "errno: %d (ENFILE)\n", errno);
        } else {
            perror("open");
        }
    }
    return 0;
}
```

## Related Errors

- [errno-24 EMFILE]({{< relref "/languages/c/errno-emfile" >}}) — too many open files (per-process).
- [errno-23 ENFILE](/languages/c/errno-enfile/) — too many open files in system (numeric).
- [errno-11 EAGAIN](/languages/c/errno-enfile/) — resource unavailable, try again.
