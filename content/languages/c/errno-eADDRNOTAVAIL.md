---
title: "[Solution] C errno EADDRNOTAVAIL — Cannot assign address Fix"
description: "Fix C EADDRNOTAVAIL (Cannot assign address) by checking interface addresses, using INADDR_ANY, and verifying network configuration."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EADDRNOTAVAIL — Cannot assign address Fix

When `bind()` or `connect()` is called with an address that is not available on any local network interface, the call fails and sets `errno` to `EADDRNOTAVAIL`. This error indicates the requested IP address or interface does not exist on the system.

## Common Causes

- Binding to an IP address that is not assigned to any local network interface.
- The network interface is down or not configured.
- The requested address belongs to a different subnet.
- Connecting to a local address that does not exist on the system.

## How to Fix

Use `INADDR_ANY` to bind to all available interfaces, or verify the local IP configuration.

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) { perror("socket"); return 1; }

    struct sockaddr_in addr = {0};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(8080);
    addr.sin_addr.s_addr = INADDR_ANY;  // Bind to all interfaces

    if (bind(sock, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        if (errno == EADDRNOTAVAIL) {
            fprintf(stderr, "Requested address not available on any interface\n");
        } else {
            perror("bind");
        }
        close(sock);
        return 1;
    }
    close(sock);
    return 0;
}
```

## Examples

Binding to a non-existent interface:

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
    addr.sin_port = htons(8080);
    addr.sin_addr.s_addr = inet_addr("192.168.99.99");  // Not on this machine

    if (bind(sock, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        if (errno == EADDRNOTAVAIL) {
            fprintf(stderr, "Address 192.168.99.99 not available (errno %d)\n", errno);
        }
    }
    close(sock);
    return 0;
}
```

## Related Errors

- [errno-99 EADDRNOTAVAIL]({{< relref "/languages/c/errno-eADDRNOTAVAIL" >}}) — cannot assign address (numeric).
- [errno-98 EADDRINUSE]({{< relref "/languages/c/errno-eADDRINUSE" >}}) — address already in use.
- [errno-19 ENODEV](/languages/c/errno-eADDRNOTAVAIL/) — no such device.
