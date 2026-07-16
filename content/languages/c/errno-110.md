---
title: "[Solution] C errno 110 ETIMEDOUT — Connection Timed Out Fix"
description: "Fix C errno 110 ETIMEDOUT (Connection timed out) by checking network connectivity, increasing socket timeout, and verifying DNS resolution."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
tags: ["etimedout", "errno-110", "timeout", "network", "socket"]
weight: 30
---

# [Solution] C errno 110 ETIMEDOUT — Connection Timed Out Fix

When a network connection takes longer than the system-imposed timeout, the kernel sets `errno` to `ETIMEDOUT` (110 on Linux) and the `connect()`, `send()`, or `recv()` call returns `-1`. This typically means the remote host is unreachable, the network is congested, or DNS resolution is failing.

## What You'll See

```c
int sockfd = socket(AF_INET, SOCK_STREAM, 0);
int result = connect(sockfd, (struct sockaddr *)&addr, sizeof(addr));
if (result == -1) {
    perror("connect");  // "connect: Connection timed out"
    fprintf(stderr, "errno: %d\n", errno);  // errno: 110
}
```

## Common Causes

- The remote server is down or not listening on the specified port.
- A firewall is silently dropping packets instead of rejecting them.
- DNS resolution is slow or returning an unreachable IP.
- The default socket timeout is too short for the network conditions.
- Routing issues between the client and server.

## Wrong: No timeout handling

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(80);
    inet_pton(AF_INET, "93.184.216.34", &addr.sin_addr);

    // Blocks until the OS timeout (can be 60-120 seconds)
    if (connect(sockfd, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        fprintf(stderr, "Connection failed: errno %d\n", errno);
        return 1;
    }
    return 0;
}
```

## Correct: Set socket timeout before connecting

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <errno.h>
#include <unistd.h>

int main(void) {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1) {
        perror("socket");
        return 1;
    }

    // Set a 5-second connect timeout using SO_SNDTIMEO
    struct timeval tv;
    tv.tv_sec = 5;
    tv.tv_usec = 0;
    setsockopt(sockfd, SOL_SOCKET, SO_SNDTIMEO, &tv, sizeof(tv));

    // Alternatively, use non-blocking connect with select/poll for portable timeout
    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(80);
    inet_pton(AF_INET, "93.184.216.34", &addr.sin_addr);

    if (connect(sockfd, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        if (errno == ETIMEDOUT) {
            fprintf(stderr, "Connection timed out after 5 seconds\n");
        } else {
            perror("connect");
        }
        close(sockfd);
        return 1;
    }

    printf("Connected successfully\n");
    close(sockfd);
    return 0;
}
```

## Non-blocking connect with select (Portable Timeout)

```c
#include <sys/socket.h>
#include <sys/select.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <fcntl.h>

int connect_with_timeout(const char *ip, int port, int timeout_secs) {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1) return -1;

    // Set non-blocking mode
    int flags = fcntl(sockfd, F_GETFL, 0);
    fcntl(sockfd, F_SETFL, flags | O_NONBLOCK);

    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);
    inet_pton(AF_INET, ip, &addr.sin_addr);

    int result = connect(sockfd, (struct sockaddr *)&addr, sizeof(addr));
    if (result == 0) {
        fcntl(sockfd, F_SETFL, flags);  // restore blocking mode
        return sockfd;
    }

    if (errno != EINPROGRESS) {
        close(sockfd);
        return -1;
    }

    // Wait for connection with timeout using select
    fd_set writefds;
    FD_ZERO(&writefds);
    FD_SET(sockfd, &writefds);

    struct timeval tv;
    tv.tv_sec = timeout_secs;
    tv.tv_usec = 0;

    result = select(sockfd + 1, NULL, &writefds, NULL, &tv);
    if (result <= 0) {
        close(sockfd);
        return -1;  // timeout or error
    }

    // Check if connection succeeded
    int error = 0;
    socklen_t len = sizeof(error);
    getsockopt(sockfd, SOL_SOCKET, SO_ERROR, &error, &len);
    if (error != 0) {
        close(sockfd);
        return -1;
    }

    fcntl(sockfd, F_SETFL, flags);  // restore blocking mode
    return sockfd;
}
```

## Check DNS Resolution Before Connecting

```c
#include <netdb.h>
#include <stdio.h>

int resolve_host(const char *hostname) {
    struct addrinfo hints, *result;
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;

    int status = getaddrinfo(hostname, NULL, &hints, &result);
    if (status != 0) {
        fprintf(stderr, "DNS resolution failed: %s\n", gai_strerror(status));
        return -1;
    }

    char ip[INET_ADDRSTRLEN];
    struct sockaddr_in *addr = (struct sockaddr_in *)result->ai_addr;
    inet_ntop(AF_INET, &addr->sin_addr, ip, sizeof(ip));
    printf("Resolved %s to %s\n", hostname, ip);

    freeaddrinfo(result);
    return 0;
}
```

## Debugging Network Connectivity

```bash
# Test if the host is reachable
ping -c 3 93.184.216.34

# Test if the port is open
nc -zv 93.184.216.34 80

# Check DNS resolution time
time nslookup example.com

# Trace the route to find where packets are dropped
traceroute -n 93.184.216.34

# Check local firewall rules
iptables -L -n
```

## Summary

| Fix | When to Use |
|---|---|
| Set `SO_SNDTIMEO` / `SO_RCVTIMEO` | When you need a simple timeout on blocking I/O |
| Non-blocking connect + `select()`/`poll()` | When you need precise timeout control |
| DNS pre-check with `getaddrinfo()` | When DNS resolution may be slow |
| Retry with backoff | When failures are transient |
| Check firewall rules | When connections are silently dropped |

## Related Errors

- [errno-115 EINPROGRESS](errno-115) — operation in progress (non-blocking connect).
- [errno-99 EADDRNOTAVAIL](errno-99) — address not available.
- [errno-32 EPIPE](errno-32) — broken pipe.
