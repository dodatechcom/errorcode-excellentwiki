---
title: "[Solution] C connect() Error — How to Fix"
description: "Fix C connect() errors including EINPROGRESS, ETIMEDOUT, and ECONNREFUSED handling."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C connect() Error — How to Fix

connect() initiates a connection. Common errors include not handling EINPROGRESS on non-blocking sockets, ETIMEDOUT from unreachable hosts, and ECONNREFUSED when no server is listening.

## Common Error Messages

- `connect: Connection refused (ECONNREFUSED)`
- `connect: Connection timed out (ETIMEDOUT)`
- `connect: Operation now in progress (EINPROGRESS)`
- `connect: No route to host (EHOSTUNREACH)`

## How to Fix It

### Handle connect return value

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>

int main(void) {
    int fd = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_port = htons(8080),
        .sin_addr.s_addr = inet_addr("127.0.0.1")
    };
    if (connect(fd, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        perror("connect");
        close(fd);
        return 1;
    }
    printf("Connected!\n");
    close(fd);
    return 0;
}
```

### Non-blocking connect with timeout

```c
#include <sys/socket.h>
#include <fcntl.h>
#include <select.h>
#include <stdio.h>

int connect_timeout(int fd, struct sockaddr *addr, socklen_t len, int secs) {
    int flags = fcntl(fd, F_GETFL, 0);
    fcntl(fd, F_SETFL, flags | O_NONBLOCK);
    int ret = connect(fd, addr, len);
    if (ret == 0 || errno == EISCONN) return 0;
    if (errno != EINPROGRESS) return -1;
    fd_set wfds;
    FD_ZERO(&wfds);
    FD_SET(fd, &wfds);
    struct timeval tv = { .tv_sec = secs };
    ret = select(fd + 1, NULL, &wfds, NULL, &tv);
    fcntl(fd, F_SETFL, flags);
    if (ret > 0) return 0;
    return -1;
}
```

### Resolve hostname with getaddrinfo first

```c
#include <sys/socket.h>
#include <netdb.h>
#include <stdio.h>

int connect_host(const char *host, int port) {
    struct addrinfo hints = { .ai_family = AF_UNSPEC, .ai_socktype = SOCK_STREAM };
    struct addrinfo *result;
    char port_str[6];
    snprintf(port_str, sizeof(port_str), "%d", port);
    if (getaddrinfo(host, port_str, &hints, &result) != 0) return -1;
    int fd = socket(result->ai_family, result->ai_socktype, result->ai_protocol);
    if (fd == -1) { freeaddrinfo(result); return -1; }
    if (connect(fd, result->ai_addr, result->ai_addrlen) == -1) {
        close(fd); fd = -1;
    }
    freeaddrinfo(result);
    return fd;
}
```

### Set SO_NOSIGPIPE on macOS

```c
#include <sys/socket.h>

int main(void) {
    int fd = socket(AF_INET, SOCK_STREAM, 0);
    #ifdef SO_NOSIGPIPE
    int opt = 1;
    setsockopt(fd, SOL_SOCKET, SO_NOSIGPIPE, &opt, sizeof(opt));
    #endif
    close(fd);
    return 0;
}
```

## Common Scenarios

### Scenario 1: connect returns ECONNREFUSED — server not listening

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Non-blocking connect returns EINPROGRESS without handling

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: DNS resolution fails causing connect to fail

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always check connect return value and handle EINPROGRESS
- **Tip 2:** Use getaddrinfo to resolve hostnames before connecting
- **Tip 3:** Set timeouts to prevent indefinite blocking on connect
