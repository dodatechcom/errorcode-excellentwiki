---
title: "[Solution] C errno ENOTCONN — Not connected Fix"
description: "Fix C ENOTCONN (Not connected) by ensuring socket is connected before send/recv and checking connection state."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enotconn", "not-connected", "socket", "send", "recv"]
weight: 5
---

# [Solution] C errno ENOTCONN — Not connected Fix

When a socket operation (`send()`, `recv()`, `getpeername()`, etc.) is called on a socket that has not been connected, the call fails and sets `errno` to `ENOTCONN`. This error indicates the socket's transport endpoint is not connected.

## Common Causes

- Calling `send()` or `recv()` on a socket before calling `connect()`.
- The socket was created with `socket()` but never connected.
- The connection was closed and the socket was not reconnected.
- Calling `getpeername()` on an unconnected socket.

## How to Fix

Verify the socket is connected before performing data operations. Use `getpeername()` or `getsockopt(SO_ERROR)` to check.

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int is_connected(int sock) {
    struct sockaddr_in peer;
    socklen_t len = sizeof(peer);
    return getpeername(sock, (struct sockaddr *)&peer, &len) == 0;
}

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);

    if (!is_connected(sock)) {
        fprintf(stderr, "Socket not connected — call connect() first\n");
        close(sock);
        return 1;
    }

    send(sock, "data", 4, 0);
    close(sock);
    return 0;
}
```

## Examples

Sending on an unconnected socket:

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);

    ssize_t n = send(sock, "data", 4, 0);
    if (n == -1) {
        if (errno == ENOTCONN) {
            fprintf(stderr, "Socket not connected (errno %d)\n", errno);
        }
    }
    close(sock);
    return 0;
}
```

## Related Errors

- [errno-107 ENOTCONN]({{< relref "/languages/c/errno-eNOTCONN" >}}) — not connected (numeric).
- [errno-106 EISCONN]({{< relref "/languages/c/errno-eISCONN" >}}) — already connected.
- [errno-9 EBADF](/languages/c/errno-eNOTCONN/) — bad file descriptor.
