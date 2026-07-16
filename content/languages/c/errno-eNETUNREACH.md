---
title: "[Solution] C errno ENETUNREACH — Network is unreachable Fix"
description: "Fix C ENETUNREACH (Network is unreachable) by checking routing tables, gateway configuration, and network connectivity."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enetunreach", "network-unreachable", "routing", "gateway", "connectivity"]
weight: 5
---

# [Solution] C errno ENETUNREACH — Network is unreachable Fix

When a network operation fails because the destination network is unreachable (no route exists), the system call sets `errno` to `ENETUNREACH`. This error occurs when the kernel's routing table has no route to the destination network.

## Common Causes

- No default gateway is configured on the system.
- The routing table does not have a route to the destination network.
- The network interface is down, removing its associated routes.
- A firewall or routing policy blocks the route.

## How to Fix

Check and fix routing configuration. Add a default gateway or specific routes.

```bash
# Check routing table
ip route show

# Add a default gateway
sudo ip route add default via 192.168.1.1

# Check if interface is up
ip link show
```

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr = {0};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(80);
    addr.sin_addr.s_addr = inet_addr("10.0.0.1");

    if (connect(sock, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        if (errno == ENETUNREACH) {
            fprintf(stderr, "Network unreachable — check routing\n");
        } else {
            perror("connect");
        }
        close(sock);
        return 1;
    }
    close(sock);
    return 0;
}
```

## Examples

Connecting to a remote host with no route:

```c
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr = {0};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(80);
    addr.sin_addr.s_addr = inet_addr("172.16.0.1");

    if (connect(sock, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        if (errno == ENETUNREACH) {
            fprintf(stderr, "No route to network 172.16.0.0\n");
            fprintf(stderr, "errno: %d (ENETUNREACH)\n", errno);
        }
    }
    close(sock);
    return 0;
}
```

## Related Errors

- [errno-101 ENETUNREACH]({{< relref "/languages/c/errno-eNETUNREACH" >}}) — network is unreachable (numeric).
- [errno-100 ENETDOWN]({{< relref "/languages/c/errno-eNETDOWN" >}}) — network is down.
- [errno-113 EHOSTUNREACH]({{< relref "/languages/c/errno-eHOSTUNREACH" >}}) — no route to host.
