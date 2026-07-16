---
title: "[Solution] C errno EHOSTUNREACH — No route to host Fix"
description: "Fix C EHOSTUNREACH (No route to host) by checking routing, gateways, firewall rules, and network configuration."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["ehostunreach", "no-route-to-host", "routing", "gateway", "firewall"]
weight: 5
---

# [Solution] C errno EHOSTUNREACH — No route to host Fix

When a network operation fails because the destination host is unreachable (no route exists or the host is not responding), the system call sets `errno` to `EHOSTUNREACH`. This error indicates the kernel cannot find a path to the target host.

## Common Causes

- No route exists to the target host's network.
- The default gateway is not configured or is unreachable.
- A firewall rule drops packets to the target, causing ICMP unreachable responses.
- The target host is on a different subnet and the gateway is down.

## How to Fix

Verify routing configuration and gateway availability. Check firewall rules.

```bash
# Check routing table
ip route show

# Trace route to find where packets are dropped
traceroute 10.0.0.1

# Check for firewall rules blocking the path
sudo iptables -L -n
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
    addr.sin_addr.s_addr = inet_addr("10.0.0.50");

    if (connect(sock, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        if (errno == EHOSTUNREACH) {
            fprintf(stderr, "No route to host 10.0.0.50\n");
            fprintf(stderr, "Check gateway and routing table\n");
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

Connecting to an unreachable host:

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
    addr.sin_addr.s_addr = inet_addr("172.31.255.254");

    if (connect(sock, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        if (errno == EHOSTUNREACH) {
            fprintf(stderr, "No route to host (errno %d)\n", errno);
        }
    }
    close(sock);
    return 0;
}
```

## Related Errors

- [errno-113 EHOSTUNREACH]({{< relref "/languages/c/errno-eHOSTUNREACH" >}}) — no route to host (numeric).
- [errno-101 ENETUNREACH]({{< relref "/languages/c/errno-eNETUNREACH" >}}) — network is unreachable.
- [errno-112 EHOSTDOWN]({{< relref "/languages/c/errno-eHOSTDOWN" >}}) — host is down.
