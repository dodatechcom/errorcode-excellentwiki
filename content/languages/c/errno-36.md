---
title: "[Solution] C errno 36 ENOLCK — No record locks available"
description: "Fix C errno 36 ENOLCK (No record locks available) by reducing concurrent locking, increasing system limits, or using advisory locking."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enolck", "errno-36", "lock", "record-lock", "file-lock"]
weight: 5
---

# [Solution] C errno 36 ENOLCK — No record locks available

No record locks available occurs when a system call fails and sets `errno` to 36. This error indicates that the requested operation cannot be performed due to the specific condition described by ENOLCK.

## Common Causes

- Too many file locks held by the process.
- System limit on number of locks reached.
- Attempting to lock files across NFS with too many locks.
- Using fcntl() locks excessively.

## How to Fix

```c
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int fd = open("/tmp/test.txt", O_RDWR | O_CREAT, 0644);
    if (fd == -1) {
        perror("open");
        return 1;
    }
    struct flock fl;
    fl.l_type = F_WRLCK;
    fl.l_whence = SEEK_SET;
    fl.l_start = 0;
    fl.l_len = 10;
    if (fcntl(fd, F_SETLK, &fl) == -1) {
        fprintf(stderr, "fcntl failed: %s (errno %d)\n", strerror(errno), errno);
    }
    close(fd);
    return 0;
}
```

## Examples

```c
#include <sys/file.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    FILE *fp = fopen("/tmp/test.txt", "r+");
    if (fp == NULL) {
        perror("fopen");
        return 1;
    }
    if (flock(fileno(fp), LOCK_EX | LOCK_NB) == -1) {
        if (errno == EWOULDBLOCK) {
            printf("File is already locked\n");
        }
    }
    fclose(fp);
    return 0;
}
```

## Related Errors

- [errno-11 EAGAIN]({{< relref "/languages/c/errno-11" >}}) — resource unavailable.
- [errno-36 ENOLCK]({{< relref "/languages/c/errno-36" >}}) — no record locks available (self).
- [errno-13 EACCES]({{< relref "/languages/c/errno-13" >}}) — permission denied.
