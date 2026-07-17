---
title: "[Solution] C errno EINPROGRESS — Operation now in progress Fix"
description: "Fix C EINPROGRESS (Operation now in progress) by handling non-blocking I/O, using poll/select, and checking socket state."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EINPROGRESS — Operation now in progress Fix

When `connect()` is called on a non-blocking socket and the connection cannot be completed immediately, the call returns `EINPROGRESS`. This is not an error — it indicates the connection is being established asynchronously. The socket becomes writable when the connection completes.

## Common Causes

- A non-blocking `connect()` is initiated and the TCP handshake is in progress.
- The socket is configured as non-blocking and the operation would block.
- DNS resolution is happening asynchronously.
- The TCP stack is waiting for SYN-ACK from the server.

## How to Fix

Use `poll()` or `select()` to detect when the socket becomes writable, then check the connection result with `getsockopt(SO_ERROR)`.

```c
#include <sys/socket.h>
#include <sys/poll.h>
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    int flags = fcntl(sock, F_GETFL, 0);
    fcntl(sock, F_SETFL, flags | O_NONBLOCK);

    struct sockaddr_in addr = {0};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(8080);
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    int ret = connect(sock, (struct sockaddr *)&addr, sizeof(addr));
    if (ret == -1 && errno == EINPROGRESS) {
        struct pollfd pfd = { .fd = sock, .events = POLLOUT };
        ret = poll(&pfd, 1, 5000);  // 5s timeout

        if (ret > 0 && (pfd.revents & POLLOUT)) {
            int err;
            socklen_t len = sizeof(err);
            getsockopt(sock, SOL_SOCKET, SO_ERROR, &err, &len);
            if (err == 0) {
                printf("Connected successfully\n");
            } else {
                fprintf(stderr, "Connection failed: %s\n", strerror(err));
            }
        } else if (ret == 0) {
            fprintf(stderr, "Connection timed out\n");
        }
    }
    close(sock);
    return 0;
}
```

## Examples

Non-blocking connect pattern:

```c
#include <sys/socket.h>
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    fcntl(sock, F_SETFL, O_NONBLOCK);

    struct sockaddr_in addr = {0};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(80);
    addr.sin_addr.s_addr = inet_addr("93.184.216.34");

    if (connect(sock, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        if (errno == EINPROGRESS) {
            fprintf(stderr, "Connection in progress (errno %d)\n", errno);
            fprintf(stderr, "Use poll/select to wait for completion\n");
        }
    }
    close(sock);
    return 0;
}
```

## Related Errors

- [errno-115 EINPROGRESS]({{< relref "/languages/c/errno-eINPROGRESS" >}}) — operation now in progress (numeric).
- [errno-114 EALREADY]({{< relref "/languages/c/errno-eALREADY" >}}) — operation already in progress.
- [errno-36 EISCONN]({{< relref "/languages/c/errno-eISCONN" >}}) — already connected.
