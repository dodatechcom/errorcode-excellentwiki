---
title: "[Solution] C errno EHOSTDOWN — Host is down Fix"
description: "Fix C EHOSTDOWN (Host is down) by detecting unreachable hosts, implementing health checks, and using failover."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EHOSTDOWN — Host is down Fix

When a network operation fails because the target host is down (not responding to ARP requests or ICMP), the system call may set `errno` to `EHOSTDOWN`. This error indicates the host on the local network is not reachable.

## Common Causes

- The target host is powered off or has crashed.
- The network cable to the host is disconnected.
- The host's network interface is down.
- ARP resolution failed because the host is not responding on the LAN.

## How to Fix

Implement health checks and failover logic. Use ICMP ping to detect host availability.

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <errno.h>
#include <unistd.h>

int connect_with_health_check(struct sockaddr *addr, socklen_t addrlen) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) return -1;

    if (connect(sock, addr, addrlen) == 0) return sock;

    if (errno == EHOSTDOWN) {
        fprintf(stderr, "Target host is down\n");
    }
    close(sock);
    return -1;
}

int main(void) {
    struct sockaddr_in addr = {0};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(80);
    addr.sin_addr.s_addr = inet_addr("192.168.1.10");

    int sock = connect_with_health_check((struct sockaddr *)&addr, sizeof(addr));
    if (sock == -1) {
        fprintf(stderr, "Cannot reach host\n");
    } else {
        close(sock);
    }
    return 0;
}
```

## Examples

Detecting a down host:

```c
#include <stdio.h>
#include <errno.h>

int main(void) {
    // connect() to a host that is down
    // Kernel returns EHOSTDOWN after ARP failures
    fprintf(stderr, "Host is down (errno %d)\n", EHOSTDOWN);
    return 1;
}
```

## Related Errors

- [errno-112 EHOSTDOWN]({{< relref "/languages/c/errno-eHOSTDOWN" >}}) — host is down (numeric).
- [errno-113 EHOSTUNREACH]({{< relref "/languages/c/errno-eHOSTUNREACH" >}}) — no route to host.
- [errno-110 ETIMEDOUT]({{< relref "/languages/c/errno-eTIMEDOUT" >}}) — connection timed out.
