---
title: "[Solution] C errno EALREADY — Operation already in progress Fix"
description: "Fix C EALREADY (Operation already in progress) by handling non-blocking connect states and checking socket readiness."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EALREADY — Operation already in progress Fix

When `connect()` is called on a non-blocking socket that already has a connection attempt in progress, the call fails and sets `errno` to `EALREADY`. This error indicates a previous `connect()` has not yet completed.

## Common Causes

- Calling `connect()` again on a non-blocking socket while the first attempt is still pending.
- The socket is in the middle of a TCP three-way handshake.
- A previous `connect()` returned `EINPROGRESS` and has not yet completed.
- Programming error: not tracking the connection state of non-blocking sockets.

## How to Fix

Use `poll()` or `select()` to wait for the socket to become writable, then check for errors with `getsockopt(SO_ERROR)`.

```c
#include <sys/socket.h>
#include <sys/poll.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);

    // Set non-blocking
    int flags = fcntl(sock, F_GETFL, 0);
    fcntl(sock, F_SETFL, flags | O_NONBLOCK);

    struct sockaddr_in addr = {0};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(8080);
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    int ret = connect(sock, (struct sockaddr *)&addr, sizeof(addr));
    if (ret == -1) {
        if (errno == EINPROGRESS) {
            // Wait for connection to complete
            struct pollfd pfd = { .fd = sock, .events = POLLOUT };
            poll(&pfd, 1, 5000);

            int err;
            socklen_t len = sizeof(err);
            getsockopt(sock, SOL_SOCKET, SO_ERROR, &err, &len);
            if (err != 0) {
                fprintf(stderr, "Connection failed: %s\n", strerror(err));
            }
        } else if (errno == EALREADY) {
            fprintf(stderr, "Connection attempt already in progress\n");
        }
    }
    close(sock);
    return 0;
}
```

## Examples

Non-blocking connect race condition:

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
    addr.sin_port = htons(8080);
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    connect(sock, (struct sockaddr *)&addr, sizeof(addr));  // Returns EINPROGRESS

    // Calling connect again before it completes
    if (connect(sock, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        if (errno == EALREADY) {
            fprintf(stderr, "Connect already in progress (errno %d)\n", errno);
        }
    }
    close(sock);
    return 0;
}
```

## Related Errors

- [errno-114 EALREADY]({{< relref "/languages/c/errno-eALREADY" >}}) — operation already in progress (numeric).
- [errno-115 EINPROGRESS]({{< relref "/languages/c/errno-eINPROGRESS" >}}) — operation now in progress.
- [errno-36 EISCONN]({{< relref "/languages/c/errno-eISCONN" >}}) — already connected.
