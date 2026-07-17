---
title: "[Solution] C errno 29 ESPIPE — Illegal seek"
description: "Fix C errno 29 ESPIPE (Illegal seek) by avoiding lseek on pipes, sockets, or other non-seekable file descriptors."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno 29 ESPIPE — Illegal seek

Illegal seek occurs when a system call fails and sets `errno` to 29. This error indicates that the requested operation cannot be performed due to the specific condition described by ESPIPE.

## Common Causes

- Calling lseek() on a pipe, socket, or FIFO.
- Trying to rewind a non-seekable file descriptor.
- Using fseek() on a stream connected to a pipe.
- Attempting to set file position on a device that doesn't support seeking.

## How to Fix

```c
#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int pipefd[2];
    pipe(pipefd);
    off_t pos = lseek(pipefd[0], 0, SEEK_SET);
    if (pos == -1) {
        fprintf(stderr, "lseek failed: %s (errno %d)\n", strerror(errno), errno);
    }
    close(pipefd[0]);
    close(pipefd[1]);
    return 0;
}
```

## Examples

```c
#include <sys/stat.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct stat st;
    if (fstat(STDIN_FILENO, &st) == 0) {
        if (S_ISFIFO(st.st_mode)) {
            printf("Standard input is a pipe/FIFO - lseek will fail\n");
        }
    }
    return 0;
}
```

## Related Errors

- [errno-29 ESPIPE]({{< relref "/languages/c/errno-29" >}}) — illegal seek (self).
- [errno-13 EACCES]({{< relref "/languages/c/errno-13" >}}) — permission denied.
- [errno-32 EPIPE]({{< relref "/languages/c/errno-32" >}}) — broken pipe.
