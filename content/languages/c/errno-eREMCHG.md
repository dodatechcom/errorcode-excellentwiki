---
title: "[Solution] C errno EREMCHG — Remote address changed Fix"
description: "Fix C EREMCHG (Remote address changed) by handling mobile hosts, reconnecting after address changes, and using DNS updates."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EREMCHG — Remote address changed Fix

When a connected socket's remote address has changed (typically due to a mobile host changing networks or an IP address update), the system call fails and sets `errno` to `EREMCHG`. This error is specific to systems supporting mobile IP or dynamic addressing.

## Common Causes

- A mobile host changed its network, causing its IP address to change.
- The remote host's IP address was reassigned (DHCP lease renewal).
- Network routing changes caused the remote endpoint to appear at a different address.
- NAT or firewall reconnection changed the visible remote address.

## How to Fix

Implement reconnection logic that detects address changes and reconnects to the new address.

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <errno.h>

int reconnect_with_retry(int sock, struct sockaddr *addr, socklen_t addrlen, int max_retries) {
    for (int i = 0; i < max_retries; i++) {
        if (connect(sock, addr, addrlen) == 0) return 0;
        if (errno == EREMCHG) {
            fprintf(stderr, "Remote address changed — reconnecting (attempt %d)\n", i + 1);
            // Refresh DNS / address lookup here
        } else {
            return -1;
        }
        usleep(1000000 * (i + 1));  // 1s, 2s, 3s backoff
    }
    return -1;
}

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr = {0};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(8080);
    addr.sin_addr.s_addr = inet_addr("192.168.1.100");

    if (reconnect_with_retry(sock, (struct sockaddr *)&addr, sizeof(addr), 3) == -1) {
        fprintf(stderr, "Failed to reconnect\n");
    }
    close(sock);
    return 0;
}
```

## Examples

Detecting a remote address change:

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    ssize_t n = send(sock, "keepalive", 9, 0);
    if (n == -1) {
        if (errno == EREMCHG) {
            fprintf(stderr, "Remote address changed — need to reconnect\n");
        }
    }
    return 0;
}
```

## Related Errors

- [errno-65 EREMCHG]({{< relref "/languages/c/errno-eREMCHG" >}}) — remote address changed (numeric).
- [errno-113 EHOSTUNREACH]({{< relref "/languages/c/errno-eHOSTUNREACH" >}}) — no route to host.
- [errno-110 ETIMEDOUT]({{< relref "/languages/c/errno-eTIMEDOUT" >}}) — connection timed out.
