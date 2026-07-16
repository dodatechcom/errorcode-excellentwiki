---
title: "[Solution] C errno ENETRESET — Network connection reset Fix"
description: "Fix C ENETRESET (Network connection reset) by handling TCP resets, implementing retry logic, and checking connection health."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enetreset", "network-connection-reset", "tcp-reset", "connection-loss"]
weight: 5
---

# [Solution] C errno ENETRESET — Network connection reset Fix

When a TCP connection is reset by the network (due to a router reboot, intermediate device failure, or network change), the system call fails and sets `errno` to `ENETRESET`. This error indicates the connection was dropped by an intermediate network device.

## Common Causes

- A router or firewall along the path sent a TCP RST segment.
- The network path changed and the old connection is no longer valid.
- A NAT device dropped the mapping and sent a reset.
- The remote host's network was reset.

## How to Fix

Implement connection retry and reconnection logic. Use keepalive to detect dead connections early.

```c
#include <sys/socket.h>
#include <netinet/tcp.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);

    // Enable TCP keepalive to detect dead connections
    int keepalive = 1;
    setsockopt(sock, SOL_SOCKET, SO_KEEPALIVE, &keepalive, sizeof(keepalive));

    ssize_t n = send(sock, "data", 4, 0);
    if (n == -1) {
        if (errno == ENETRESET) {
            fprintf(stderr, "Network connection reset by intermediate device\n");
            // Reconnect
        } else {
            perror("send");
        }
    }
    close(sock);
    return 0;
}
```

## Examples

Receiving a connection reset during data transfer:

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    char buf[1024];
    ssize_t n = recv(sock, buf, sizeof(buf), 0);
    if (n == -1) {
        if (errno == ENETRESET) {
            fprintf(stderr, "Connection reset by network (errno %d)\n", errno);
        }
    }
    return 0;
}
```

## Related Errors

- [errno-102 ENETRESET]({{< relref "/languages/c/errno-eNETRESET" >}}) — network connection reset (numeric).
- [errno-104 ECONNRESET]({{< relref "/languages/c/errno-eCONNRESET" >}}) — connection reset by peer.
- [errno-103 ECONNABORTED]({{< relref "/languages/c/errno-eCONNABORTED" >}}) — connection aborted.
