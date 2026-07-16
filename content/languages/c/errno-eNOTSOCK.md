---
title: "[Solution] C errno ENOTSOCK — Socket operation on non-socket Fix"
description: "Fix C ENOTSOCK (Socket operation on non-socket) by verifying file descriptors are sockets before performing socket operations."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enotsock", "socket-operation-on-non-socket", "socket", "fd-check"]
weight: 5
---

# [Solution] C errno ENOTSOCK — Socket operation on non-socket Fix

When a socket-related operation (`send()`, `recv()`, `getsockopt()`, etc.) is called on a file descriptor that is not a socket, the call fails and sets `errno` to `ENOTSOCK`. This error occurs when passing a regular file descriptor to a socket function.

## Common Causes

- The file descriptor refers to a regular file, pipe, or device, not a socket.
- The socket was closed and the fd was reused for a non-socket file.
- A programming error passes the wrong fd to a socket function.
- `select()` or `poll()` is given a non-socket fd in the socket set.

## How to Fix

Verify file descriptors are sockets before performing socket operations. Use `fstat()` to check.

```c
#include <sys/stat.h>
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int is_socket(int fd) {
    struct stat st;
    if (fstat(fd, &st) == -1) return 0;
    return S_ISSOCK(st.st_mode);
}

int main(void) {
    int fd = 3;  // might be a file or a socket

    if (!is_socket(fd)) {
        fprintf(stderr, "File descriptor %d is not a socket\n", fd);
        return 1;
    }

    // Safe to use socket operations
    char buf[100];
    recv(fd, buf, sizeof(buf), 0);
    return 0;
}
```

## Examples

Calling send() on a regular file:

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    FILE *fp = fopen("test.txt", "w");
    int fd = fileno(fp);

    ssize_t n = send(fd, "data", 4, 0);
    if (n == -1 && errno == ENOTSOCK) {
        fprintf(stderr, "Not a socket (errno %d)\n", errno);
    }
    fclose(fp);
    return 0;
}
```

## Related Errors

- [errno-88 ENOTSOCK]({{< relref "/languages/c/errno-eNOTSOCK" >}}) — socket operation on non-socket (numeric).
- [errno-9 EBADF](/languages/c/errno-eNOTSOCK/) — bad file descriptor.
- [errno-22 EINVAL](/languages/c/errno-eNOTSOCK/) — invalid argument.
