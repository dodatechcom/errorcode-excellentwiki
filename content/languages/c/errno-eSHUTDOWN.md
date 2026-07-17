---
title: "[Solution] C errno ESHUTDOWN — Cannot send after shutdown Fix"
description: "Fix C ESHUTDOWN (Cannot send after shutdown) by handling socket shutdown states and checking connection status before sending."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ESHUTDOWN — Cannot send after shutdown Fix

When a process attempts to send data on a socket that has been shut down for writing (via `shutdown()` or the peer's close), the system call fails and sets `errno` to `ESHUTDOWN`. This error indicates the send half of the connection is closed.

## Common Causes

- `shutdown(fd, SHUT_WR)` was called on the socket, disabling further sends.
- The peer has closed its end of the connection.
- The socket was shut down before the send operation completed.
- A half-closed TCP connection is in the FIN-WAIT-2 state.

## How to Fix

Check the socket state before sending. Handle `ESHUTDOWN` to detect closed connections gracefully.

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int safe_send(int sock, const void *buf, size_t len) {
    ssize_t n = send(sock, buf, len, 0);
    if (n == -1) {
        if (errno == ESHUTDOWN) {
            fprintf(stderr, "Socket shutdown — cannot send\n");
            return -1;
        }
        fprintf(stderr, "send failed: %s\n", strerror(errno));
        return -1;
    }
    return n;
}
```

## Examples

Sending after `shutdown()`:

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    // ... connect() ...

    shutdown(sock, SHUT_WR);

    ssize_t n = send(sock, "data", 4, 0);
    if (n == -1 && errno == ESHUTDOWN) {
        fprintf(stderr, "Cannot send after shutdown (errno %d)\n", errno);
    }
    close(sock);
    return 0;
}
```

## Related Errors

- [errno-108 ESHUTDOWN]({{< relref "/languages/c/errno-eSHUTDOWN" >}}) — cannot send after shutdown (numeric).
- [errno-32 EPIPE]({{< relref "/languages/c/errno-epipe" >}}) — broken pipe.
- [errno-107 ENOTCONN]({{< relref "/languages/c/errno-eNOTCONN" >}}) — not connected.
