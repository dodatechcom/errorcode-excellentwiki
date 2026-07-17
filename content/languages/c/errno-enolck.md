---
title: "[Solution] C errno ENOLCK — No record locks available Fix"
description: "Fix C ENOLCK (No record locks available) by reducing lock usage, checking system limits, and using advisory locking."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ENOLCK — No record locks available Fix

When a process attempts to acquire a file lock using `fcntl()` with `F_SETLKW` or `F_SETLK` and the system has exhausted its available lock resources, the call fails and sets `errno` to `ENOLCK`. This error is uncommon on modern Linux systems but can occur under heavy lock usage.

## Common Causes

- The system-wide limit for POSIX record locks (`/proc/sys/fs/locks/nr_locks` or internal kernel limits) has been reached.
- A process is creating too many locks across many files without releasing them.
- Lock leak — locks acquired but never released via `F_SETLK` with `F_UNLCK`.
- Heavy concurrent access patterns creating lock contention.

## How to Fix

Release locks when they are no longer needed. Consider using advisory locking or alternative synchronization mechanisms.

```c
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>

int acquire_lock(int fd) {
    struct flock fl;
    fl.l_type = F_WRLCK;
    fl.l_whence = SEEK_SET;
    fl.l_start = 0;
    fl.l_len = 0;

    if (fcntl(fd, F_SETLKW, &fl) == -1) {
        if (errno == ENOLCK) {
            fprintf(stderr, "No record locks available\n");
        } else {
            fprintf(stderr, "fcntl lock failed: %s\n", strerror(errno));
        }
        return -1;
    }
    return 0;
}

void release_lock(int fd) {
    struct flock fl;
    fl.l_type = F_UNLCK;
    fl.l_whence = SEEK_SET;
    fl.l_start = 0;
    fl.l_len = 0;
    fcntl(fd, F_SETLK, &fl);
}
```

## Examples

Acquiring and releasing file locks:

```c
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int fd = open("data.txt", O_RDWR);
    if (fd == -1) { perror("open"); return 1; }

    struct flock fl = { .l_type = F_WRLCK, .l_whence = SEEK_SET, .l_start = 0, .l_len = 0 };
    if (fcntl(fd, F_SETLKW, &fl) == -1) {
        if (errno == ENOLCK) {
            fprintf(stderr, "Cannot acquire lock — system limit reached\n");
        }
        close(fd);
        return 1;
    }

    // Critical section
    write(fd, "data", 4);

    // Release lock
    fl.l_type = F_UNLCK;
    fcntl(fd, F_SETLK, &fl);
    close(fd);
    return 0;
}
```

## Related Errors

- [errno-37 ENOLCK](/languages/c/errno-enolck/) — no record locks available (numeric).
- [errno-11 EAGAIN](/languages/c/errno-enolck/) — resource unavailable, try again.
- [errno-11 EDEADLK]({{< relref "/languages/c/errno-eDEADLOCK" >}}) — resource deadlock avoided.
