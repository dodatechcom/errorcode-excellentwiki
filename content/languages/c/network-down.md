---
title: "[Solution] C Network is down: ENETDOWN"
description: "Fix C network is down (ENETDOWN). Check network interface status."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Network is down: ENETDOWN

ENETDOWN occurs when you try to use a network interface that has been administratively disabled or has failed.

## Common Causes

```c
// Cause 1: Interface is down
// eth0 has been brought down

// Cause 2: Network driver failure
// Hardware issue with NIC

// Cause 3: Virtual interface destroyed
// Container network interface removed
```

## How to Fix

### Fix 1: Bring up the interface

```bash
ip link set eth0 up
```

### Fix 2: Check interface status

```bash
ip link show
# Look for state UP or DOWN
```

### Fix 3: Restart networking

```bash
systemctl restart networking
# or
systemctl restart NetworkManager
```

## Examples

```c
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) {
        if (errno == ENETDOWN) {
            fprintf(stderr, "Network is down\n");
        }
        perror("socket");
        return 1;
    }
    close(sock);
    return 0;
}
```

## Related Errors

- [Network unreachable]({{< relref "/languages/c/network-unreachable" >}}) — ENETUNREACH.
- [Host unreachable]({{< relref "/languages/c/host-unreachable" >}}) — EHOSTUNREACH.
- [Connection refused]({{< relref "/languages/c/connection-refused-c" >}}) — ECONNREFUSED.
