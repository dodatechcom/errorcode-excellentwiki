---
title: "[Solution] C errno ENOBUFS — No buffer space available Fix"
description: "Fix C ENOBUFS (No buffer space available) by tuning network buffers, reducing memory pressure, and using SO_SNDBUF/SO_RCVBUF."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ENOBUFS — No buffer space available Fix

When the kernel cannot allocate buffer space for a network operation (send or receive), the system call fails and sets `errno` to `ENOBUFS`. This error indicates the network buffer pool is exhausted.

## Common Causes

- The system is under heavy network load and all buffers are in use.
- The socket's send or receive buffer is full and cannot grow.
- The kernel's network memory limits (`net.core.wmem_max`, `net.core.rmem_max`) are too low.
- Memory pressure from other processes reduces available network buffers.

## How to Fix

Increase network buffer limits and tune socket buffer sizes.

```bash
# Check current limits
sysctl net.core.wmem_max net.core.rmem_max net.core.wmem_default net.core.rmem_default

# Increase limits
sysctl -w net.core.wmem_max=16777216
sysctl -w net.core.rmem_max=16777216
```

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);

    // Set send buffer size
    int sndbuf = 1024 * 1024;  // 1MB
    if (setsockopt(sock, SOL_SOCKET, SO_SNDBUF, &sndbuf, sizeof(sndbuf)) == -1) {
        perror("setsockopt SO_SNDBUF");
    }

    // Set receive buffer size
    int rcvbuf = 1024 * 1024;
    if (setsockopt(sock, SOL_SOCKET, SO_RCVBUF, &rcvbuf, sizeof(rcvbuf)) == -1) {
        perror("setsockopt SO_RCVBUF");
    }

    ssize_t n = send(sock, "data", 4, 0);
    if (n == -1 && errno == ENOBUFS) {
        fprintf(stderr, "No buffer space available\n");
    }
    close(sock);
    return 0;
}
```

## Examples

Send failing due to full buffers:

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    // Sending faster than the peer can consume
    for (int i = 0; i < 100000; i++) {
        ssize_t n = send(sock, "data", 4, MSG_DONTWAIT);
        if (n == -1) {
            if (errno == ENOBUFS || errno == EAGAIN) {
                fprintf(stderr, "Send buffer full (errno %d)\n", errno);
                break;
            }
        }
    }
    return 0;
}
```

## Related Errors

- [errno-105 ENOBUFS]({{< relref "/languages/c/errno-eNOBUFS" >}}) — no buffer space available (numeric).
- [errno-11 EAGAIN](/languages/c/errno-eNOBUFS/) — resource unavailable, try again.
- [errno-12 ENOMEM]({{< relref "/languages/c/errno-enomem" >}}) — cannot allocate memory.
