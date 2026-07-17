---
title: "[Solution] C errno EISCONN — Already connected Fix"
description: "Fix C EISCONN (Already connected) by checking connection state before connecting and handling duplicate connect calls."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EISCONN — Already connected Fix

When `connect()` is called on a socket that is already connected, the call fails and sets `errno` to `EISCONN`. This error indicates the socket has already been connected to a remote endpoint.

## Common Causes

- Calling `connect()` twice on the same socket without closing or disconnecting first.
- The socket was connected via `connect()` and then `connect()` is called again with a different address.
- A TCP socket that completed the three-way handshake is already in `ESTABLISHED` state.
- Programming error: failing to track connection state.

## How to Fix

Check the socket's connection state before calling `connect()`. Use `getpeername()` to verify existing connections.

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int safe_connect(int sock, struct sockaddr *addr, socklen_t addrlen) {
    struct sockaddr_in peer;
    socklen_t peerlen = sizeof(peer);

    // Check if already connected
    if (getpeername(sock, (struct sockaddr *)&peer, &peerlen) == 0) {
        fprintf(stderr, "Socket is already connected\n");
        return 0;  // Already connected
    }

    if (connect(sock, addr, addrlen) == -1) {
        if (errno == EISCONN) {
            fprintf(stderr, "Socket already connected\n");
            return 0;
        }
        perror("connect");
        return -1;
    }
    return 0;
}
```

## Examples

Calling connect twice on the same socket:

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr = {0};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(8080);
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    connect(sock, (struct sockaddr *)&addr, sizeof(addr));  // First connect

    // Second connect to different address
    if (connect(sock, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        if (errno == EISCONN) {
            fprintf(stderr, "Already connected (errno %d)\n", errno);
        }
    }
    close(sock);
    return 0;
}
```

## Related Errors

- [errno-106 EISCONN]({{< relref "/languages/c/errno-eISCONN" >}}) — already connected (numeric).
- [errno-107 ENOTCONN]({{< relref "/languages/c/errno-eNOTCONN" >}}) — not connected.
- [errno-106 EISCONN]({{< relref "/languages/c/errno-eISCONN" >}}) — transport endpoint already connected.
