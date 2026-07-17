---
title: "[Solution] C errno ENETDOWN — Network is down Fix"
description: "Fix C ENETDOWN (Network is down) by checking network interface status, handling disconnections, and implementing reconnection logic."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ENETDOWN — Network is down Fix

When a network operation fails because the local network interface is down, the system call sets `errno` to `ENETDOWN`. This error indicates that the network stack has detected the interface is not operational.

## Common Causes

- The network interface was administratively down (`ifconfig eth0 down`).
- The network cable was disconnected (for wired interfaces).
- The wireless adapter lost connection.
- A virtual network interface (bridge, tunnel) was torn down.

## How to Fix

Check network interface status and implement reconnection logic. Handle `ENETDOWN` by waiting and retrying.

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <errno.h>
#include <unistd.h>

int connect_with_retry(int sock, struct sockaddr *addr, socklen_t addrlen) {
    for (int i = 0; i < 5; i++) {
        if (connect(sock, addr, addrlen) == 0) return 0;
        if (errno == ENETDOWN) {
            fprintf(stderr, "Network is down — retrying in %ds\n", i + 1);
            sleep(i + 1);
        } else {
            return -1;
        }
    }
    return -1;
}

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr = {0};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(8080);
    addr.sin_addr.s_addr = inet_addr("192.168.1.1");

    if (connect_with_retry(sock, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        fprintf(stderr, "Failed to connect — network may be down\n");
    }
    close(sock);
    return 0;
}
```

## Examples

Sending data when network is down:

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    ssize_t n = send(sock, "data", 4, 0);
    if (n == -1) {
        if (errno == ENETDOWN) {
            fprintf(stderr, "Network interface is down (errno %d)\n", errno);
        }
    }
    return 0;
}
```

## Related Errors

- [errno-100 ENETDOWN]({{< relref "/languages/c/errno-eNETDOWN" >}}) — network is down (numeric).
- [errno-101 ENETUNREACH]({{< relref "/languages/c/errno-eNETUNREACH" >}}) — network is unreachable.
- [errno-102 ENETRESET]({{< relref "/languages/c/errno-eNETRESET" >}}) — network connection reset.
