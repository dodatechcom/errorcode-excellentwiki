---
title: "[Solution] C errno EADDRINUSE — Address already in use Fix"
description: "Fix C EADDRINUSE (Address already in use) by using SO_REUSEADDR, checking for lingering sockets, and avoiding port conflicts."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EADDRINUSE — Address already in use Fix

When `bind()` is called with an address and port that is already in use by another socket, the call fails and sets `errno` to `EADDRINUSE`. This is one of the most common socket errors, especially when restarting servers.

## Common Causes

- Another process (or the same process from a previous run) is already bound to the address and port.
- The socket is in `TIME_WAIT` state after a connection was closed.
- Multiple sockets are trying to bind to the same port.
- The `SO_REUSEADDR` option is not set on the listening socket.

## How to Fix

Set `SO_REUSEADDR` before `bind()` to allow reuse of addresses in `TIME_WAIT` state.

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) { perror("socket"); return 1; }

    int optval = 1;
    if (setsockopt(sock, SOL_SOCKET, SO_REUSEADDR, &optval, sizeof(optval)) == -1) {
        perror("setsockopt");
        close(sock);
        return 1;
    }

    struct sockaddr_in addr = {0};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(8080);
    addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(sock, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        if (errno == EADDRINUSE) {
            fprintf(stderr, "Port 8080 already in use\n");
        } else {
            fprintf(stderr, "bind failed: %s\n", strerror(errno));
        }
        close(sock);
        return 1;
    }

    listen(sock, 10);
    printf("Server listening on port 8080\n");
    close(sock);
    return 0;
}
```

## Examples

Server restart without SO_REUSEADDR:

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
    addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(sock, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        if (errno == EADDRINUSE) {
            fprintf(stderr, "Address already in use — server may still be running\n");
            fprintf(stderr, "errno: %d (EADDRINUSE)\n", errno);
        }
    }
    close(sock);
    return 0;
}
```

## Related Errors

- [errno-98 EADDRINUSE]({{< relref "/languages/c/errno-eADDRINUSE" >}}) — address already in use (numeric).
- [errno-99 EADDRNOTAVAIL]({{< relref "/languages/c/errno-eADDRNOTAVAIL" >}}) — cannot assign address.
- [errno-22 EINVAL](/languages/c/errno-eADDRINUSE/) — invalid argument.
