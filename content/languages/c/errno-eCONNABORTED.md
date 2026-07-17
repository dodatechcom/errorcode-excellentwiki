---
title: "[Solution] C errno ECONNABORTED — Connection aborted Fix"
description: "Fix C ECONNABORTED (Connection aborted) by handling peer aborts, implementing reconnection, and using keepalive."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ECONNABORTED — Connection aborted Fix

When a connection is aborted by the peer or by an intermediate network device before the application can complete the operation, the system call fails and sets `errno` to `ECONNABORTED`. The peer sent a TCP RST segment, forcibly closing the connection.

## Common Causes

- The remote peer application crashed or closed the socket improperly.
- A firewall or security device sent a TCP RST to terminate the connection.
- The peer's TCP stack rejected the connection after it was established.
- Load balancers or proxies aborted idle connections.

## How to Fix

Implement reconnection logic when `ECONNABORTED` occurs. Use TCP keepalive to detect dead connections early.

```c
#include <sys/socket.h>
#include <netinet/tcp.h>
#include <stdio.h>
#include <errno.h>
#include <unistd.h>

int send_with_reconnect(int sock, const void *buf, size_t len) {
    ssize_t n = send(sock, buf, len, 0);
    if (n == -1) {
        if (errno == ECONNABORTED) {
            fprintf(stderr, "Connection aborted — reconnecting\n");
            // Close old socket, create new one, reconnect
            close(sock);
            return -1;  // Caller should reconnect
        }
        perror("send");
        return -1;
    }
    return n;
}

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    // ... connect() ...

    if (send_with_reconnect(sock, "data", 4) == -1) {
        fprintf(stderr, "Need to reconnect\n");
    }
    close(sock);
    return 0;
}
```

## Examples

Accept on a listening socket when connection is aborted:

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int client = accept(listen_fd, NULL, NULL);
    if (client == -1) {
        if (errno == ECONNABORTED) {
            fprintf(stderr, "Connection aborted before accept completed (errno %d)\n", errno);
        }
    }
    return 0;
}
```

## Related Errors

- [errno-103 ECONNABORTED]({{< relref "/languages/c/errno-eCONNABORTED" >}}) — connection aborted (numeric).
- [errno-104 ECONNRESET]({{< relref "/languages/c/errno-eCONNRESET" >}}) — connection reset by peer.
- [errno-110 ETIMEDOUT]({{< relref "/languages/c/errno-eTIMEDOUT" >}}) — connection timed out.
