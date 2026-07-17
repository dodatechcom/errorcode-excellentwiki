---
title: "[Solution] C errno ECONNREFUSED — Connection refused Fix"
description: "Fix C ECONNREFUSED (Connection refused) by verifying server availability, checking port binding, and handling rejected connections."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ECONNREFUSED — Connection refused Fix

When `connect()` is called on a port where no process is listening, the remote TCP stack responds with a RST segment, and the local system call fails with `errno` set to `ECONNREFUSED`. This is one of the most common connection errors.

## Common Causes

- No server process is listening on the target port.
- The server process crashed or was stopped.
- The server is listening on a different address or port.
- A firewall is actively rejecting the connection with RST.

## How to Fix

Verify the server is running and listening on the expected port. Implement retry logic for transient failures.

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <errno.h>
#include <unistd.h>

int connect_retry(int sock, struct sockaddr *addr, socklen_t addrlen, int max_retries) {
    for (int i = 0; i < max_retries; i++) {
        if (connect(sock, addr, addrlen) == 0) return 0;
        if (errno == ECONNREFUSED) {
            fprintf(stderr, "Connection refused — server may be down (attempt %d)\n", i + 1);
            sleep(1);
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
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    if (connect_retry(sock, (struct sockaddr *)&addr, sizeof(addr), 3) == -1) {
        fprintf(stderr, "Could not connect to server\n");
    }
    close(sock);
    return 0;
}
```

## Examples

Connect to a non-existent server:

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
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    if (connect(sock, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        if (errno == ECONNREFUSED) {
            fprintf(stderr, "Connection refused on port 8080\n");
            fprintf(stderr, "errno: %d (ECONNREFUSED)\n", errno);
        }
    }
    close(sock);
    return 0;
}
```

## Related Errors

- [errno-111 ECONNREFUSED]({{< relref "/languages/c/errno-eCONNREFUSED" >}}) — connection refused (numeric).
- [errno-110 ETIMEDOUT]({{< relref "/languages/c/errno-eTIMEDOUT" >}}) — connection timed out.
- [errno-113 EHOSTUNREACH]({{< relref "/languages/c/errno-eHOSTUNREACH" >}}) — no route to host.
