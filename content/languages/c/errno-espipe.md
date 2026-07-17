---
title: "[Solution] C errno ESPIPE — Illegal seek Fix"
description: "Fix C ESPIPE (Illegal seek) by avoiding lseek on pipes, sockets, and devices that don't support seeking."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ESPIPE — Illegal seek Fix

When `lseek()` is called on a file descriptor that does not support seeking — such as a pipe, socket, FIFO, or certain device files — the call fails and sets `errno` to `ESPIPE`. These file descriptors are sequential streams and have no concept of a file offset.

## Common Causes

- Calling `lseek()` on a pipe created with `pipe()`.
- Calling `lseek()` on a socket file descriptor.
- Calling `lseek()` on a FIFO (named pipe).
- Calling `lseek()` on `/dev/null`, `/dev/zero`, or other special devices.

## How to Fix

Check the file type before calling `lseek()`. Use `fstat()` or `isatty()` to determine if seeking is supported.

```c
#include <sys/stat.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>

int safe_lseek(int fd, off_t *offset) {
    struct stat st;
    if (fstat(fd, &st) == -1) {
        return -1;
    }
    if (S_ISFIFO(st.st_mode) || S_ISSOCK(st.st_mode)) {
        fprintf(stderr, "Cannot seek on pipe or socket\n");
        errno = ESPIPE;
        return -1;
    }
    *offset = lseek(fd, *offset, SEEK_SET);
    return (*offset == (off_t)-1) ? -1 : 0;
}
```

## Examples

Seeking on a pipe:

```c
#include <unistd.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int fds[2];
    pipe(fds);
    off_t pos = lseek(fds[0], 0, SEEK_SET);
    if (pos == -1) {
        perror("lseek");  // "lseek: Illegal seek"
        fprintf(stderr, "errno: %d (ESPIPE)\n", errno);
    }
    close(fds[0]);
    close(fds[1]);
    return 0;
}
```

## Related Errors

- [errno-29 ESPIPE](/languages/c/errno-espipe/) — illegal seek (numeric).
- [errno-1 ESPIPE](/languages/c/errno-espipe/) — inappropriate ioctl for device.
- [errno-22 EINVAL](/languages/c/errno-espipe/) — invalid argument.
