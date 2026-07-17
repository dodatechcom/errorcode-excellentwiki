---
title: "[Solution] C errno ECONNRESET — Connection reset by peer Fix"
description: "Fix C ECONNRESET (Connection reset by peer) by handling TCP RST, implementing retry logic, and using keepalive probes."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ECONNRESET — Connection reset by peer Fix

When the remote peer sends a TCP RST segment to forcibly close the connection, subsequent operations on the socket fail and set `errno` to `ECONNRESET`. This error indicates the peer abruptly terminated the connection.

## Common Causes

- The peer application crashed or was killed unexpectedly.
- The peer called `close()` with unread data in the receive buffer.
- A firewall or NAT device sent a RST to terminate the connection.
- The peer's operating system rejected the connection state.

## How to Fix

Handle `ECONNRESET` by closing and reconnecting. Use `SO_KEEPALIVE` and `TCP_USER_TIMEOUT` to detect dead peers.

```c
#include <sys/socket.h>
#include <netinet/tcp.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);

    // Set TCP keepalive
    int keepalive = 1;
    setsockopt(sock, SOL_SOCKET, SO_KEEPALIVE, &keepalive, sizeof(keepalive));

    // Set user timeout (ms) — how long to wait before declaring dead
    int timeout = 10000;
    setsockopt(sock, IPPROTO_TCP, TCP_USER_TIMEOUT, &timeout, sizeof(timeout));

    ssize_t n = recv(sock, buf, sizeof(buf), 0);
    if (n == -1) {
        if (errno == ECONNRESET) {
            fprintf(stderr, "Connection reset by peer — reconnecting\n");
        } else {
            perror("recv");
        }
    }
    close(sock);
    return 0;
}
```

## Examples

Detecting peer reset during recv:

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    char buf[1024];
    ssize_t n = recv(sock, buf, sizeof(buf), 0);
    if (n == 0) {
        printf("Peer closed connection normally\n");
    } else if (n == -1) {
        if (errno == ECONNRESET) {
            fprintf(stderr, "Connection reset by peer (errno %d)\n", errno);
        } else {
            perror("recv");
        }
    }
    return 0;
}
```

## Related Errors

- [errno-104 ECONNRESET]({{< relref "/languages/c/errno-eCONNRESET" >}}) — connection reset by peer (numeric).
- [errno-103 ECONNABORTED]({{< relref "/languages/c/errno-eCONNABORTED" >}}) — connection aborted.
- [errno-32 EPIPE]({{< relref "/languages/c/errno-epipe" >}}) — broken pipe.
