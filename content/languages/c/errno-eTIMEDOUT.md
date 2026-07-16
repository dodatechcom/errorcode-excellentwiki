---
title: "[Solution] C errno ETIMEDOUT — Connection timed out Fix"
description: "Fix C ETIMEDOUT (Connection timed out) by checking network connectivity, adjusting timeouts, and implementing reconnection."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["etimedout", "connection-timed-out", "tcp-timeout", "keepalive", "reconnect"]
weight: 5
---

# [Solution] C errno ETIMEDOUT — Connection timed out Fix

When a TCP connection attempt or data transfer times out (no response within the configured timeout period), the system call fails and sets `errno` to `ETIMEDOUT`. This is one of the most common network errors, indicating the peer did not respond in time.

## Common Causes

- The remote host is unreachable or firewalled, causing SYN retransmissions to time out.
- The network path is congested and retransmissions exceed the timeout.
- The peer is overloaded and cannot respond within the TCP timeout.
- `connect()` times out because the server is not listening on the target port.

## How to Fix

Check network connectivity before connecting. Implement reconnection with exponential backoff.

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <errno.h>
#include <unistd.h>

int connect_with_backoff(int sock, struct sockaddr *addr, socklen_t addrlen) {
    int delays[] = {1, 2, 4, 8, 16};
    for (int i = 0; i < 5; i++) {
        if (connect(sock, addr, addrlen) == 0) return 0;
        if (errno == ETIMEDOUT) {
            fprintf(stderr, "Connection timed out — retrying in %ds\n", delays[i]);
            sleep(delays[i]);
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
    addr.sin_addr.s_addr = inet_addr("192.168.1.100");

    if (connect_with_backoff(sock, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        fprintf(stderr, "Failed to connect after retries\n");
    }
    close(sock);
    return 0;
}
```

## Examples

Connect timeout:

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
    addr.sin_port = htons(9999);
    addr.sin_addr.s_addr = inet_addr("10.0.0.1");

    if (connect(sock, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        if (errno == ETIMEDOUT) {
            fprintf(stderr, "Connection to 10.0.0.1:9999 timed out\n");
            fprintf(stderr, "errno: %d (ETIMEDOUT)\n", errno);
        }
    }
    close(sock);
    return 0;
}
```

## Related Errors

- [errno-110 ETIMEDOUT]({{< relref "/languages/c/errno-eTIMEDOUT" >}}) — connection timed out (numeric).
- [errno-113 EHOSTUNREACH]({{< relref "/languages/c/errno-eHOSTUNREACH" >}}) — no route to host.
- [errno-110 ETIMEDOUT]({{< relref "/languages/c/errno-eTIMEDOUT" >}}) — operation timed out.
