---
title: "[Solution] C errno EDEADLK — Resource deadlock avoided Fix"
description: "Fix C EDEADLK (Resource deadlock avoided) by using consistent lock ordering, trylock, and deadlock detection."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["edeadlk", "resource-deadlock", "deadlock-avoidance", "lock-ordering", "fcntl"]
weight: 5
---

# [Solution] C errno EDEADLK — Resource deadlock avoided Fix

When the kernel detects that granting a blocking lock would result in a deadlock (e.g., two processes each holding a lock the other needs), the `fcntl()` lock request fails and sets `errno` to `EDEADLK`. The kernel proactively prevents the deadlock by denying the lock.

## Common Causes

- Two or more processes acquire locks in inconsistent order (lock ordering violation).
- A process tries to lock a region it already holds with `F_SETLKW`.
- `fcntl()` file locks on the same file from different processes create a circular wait.
- Using `F_SETLKW` (blocking) instead of `F_SETLK` (non-blocking) for locks.

## How to Fix

Use consistent lock ordering, use `F_SETLK` with retry logic, or use `SIGALRM`-based timeouts.

```c
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>

int acquire_lock_no_deadlock(int fd) {
    struct flock fl;
    fl.l_type = F_WRLCK;
    fl.l_whence = SEEK_SET;
    fl.l_start = 0;
    fl.l_len = 0;

    if (fcntl(fd, F_SETLK, &fl) == -1) {
        if (errno == EDEADLK) {
            fprintf(stderr, "Deadlock avoided — retrying with backoff\n");
            usleep(10000);  // 10ms backoff
            return fcntl(fd, F_SETLKW, &fl) == 0 ? 0 : -1;
        }
        fprintf(stderr, "fcntl failed: %s\n", strerror(errno));
        return -1;
    }
    return 0;
}

int main(void) {
    int fd = open("data.txt", O_RDWR);
    if (fd == -1) { perror("open"); return 1; }
    if (acquire_lock_no_deadlock(fd) == 0) {
        // Critical section
        write(fd, "data", 4);
    }
    close(fd);
    return 0;
}
```

## Examples

Two processes causing a potential deadlock:

```c
// Process 1: locks region A, then tries B
// Process 2: locks region B, then tries A
// Kernel returns EDEADLK to one process

#include <fcntl.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct flock fl = { .l_type = F_WRLCK, .l_whence = SEEK_SET, .l_start = 0, .l_len = 100 };
    if (fcntl(fd, F_SETLKW, &fl) == -1) {
        if (errno == EDEADLK) {
            fprintf(stderr, "Deadlock avoided by kernel (errno %d)\n", errno);
        }
    }
    return 0;
}
```

## Related Errors

- [errno-35 EDEADLK](/languages/c/errno-eDEADLOCK/) — resource deadlock avoided (numeric).
- [errno-37 ENOLCK]({{< relref "/languages/c/errno-enolck" >}}) — no record locks available.
- [errno-11 EAGAIN](/languages/c/errno-eDEADLOCK/) — resource unavailable, try again.
