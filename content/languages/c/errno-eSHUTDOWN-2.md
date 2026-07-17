---
title: "[Solution] C errno ESHUTDOWN — Cannot send after shutdown (variant) Fix"
description: "Fix C ESHUTDOWN (Cannot send after shutdown variant) by checking socket shutdown state and handling half-close connections."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ESHUTDOWN — Cannot send after shutdown (variant) Fix

This is an alternate manifestation of `ESHUTDOWN` occurring when `send()`, `sendto()`, or `sendmsg()` is called on a socket whose send half has been closed via `shutdown(SHUT_WR)` or the peer's close was detected. The kernel rejects the send operation.

## Common Causes

- `shutdown(fd, SHUT_WR)` was called, disabling the send half.
- The peer closed its receiving end, causing our sends to fail.
- The socket entered a half-closed state after FIN was sent.
- A `close()` on the read end of a Unix domain socket triggers this on the write end.

## How to Fix

Check the socket state before sending. Handle `ESHUTDOWN` by transitioning to a read-only state or closing the socket.

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    // ... connect() ...

    shutdown(sock, SHUT_WR);

    ssize_t n = send(sock, "final_data", 10, 0);
    if (n == -1) {
        if (errno == ESHUTDOWN) {
            fprintf(stderr, "Cannot send after shutdown — transitioning to recv-only\n");
            // Continue receiving remaining data
            char buf[1024];
            recv(sock, buf, sizeof(buf), 0);
        }
    }
    close(sock);
    return 0;
}
```

## Examples

Sending after peer closed their end:

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    ssize_t n = send(sock, "data", 4, 0);
    if (n == -1 && errno == ESHUTDOWN) {
        fprintf(stderr, "Socket send half is shut down (errno %d)\n", ESHUTDOWN);
    }
    return 0;
}
```

## Related Errors

- [errno-108 ESHUTDOWN]({{< relref "/languages/c/errno-eSHUTDOWN" >}}) — cannot send after shutdown (numeric).
- [errno-32 EPIPE]({{< relref "/languages/c/errno-epipe" >}}) — broken pipe.
- [errno-107 ENOTCONN]({{< relref "/languages/c/errno-eNOTCONN" >}}) — not connected.
