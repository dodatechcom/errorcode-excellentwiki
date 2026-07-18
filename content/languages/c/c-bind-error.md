---
title: "[Solution] C bind() Error — How to Fix"
description: "Fix C bind() errors including EADDRINUSE, permission denied, and wrong address structure."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C bind() Error — How to Fix

bind() associates a socket with an address. Common errors include EADDRINUSE (address in use), EACCES (non-root binding to privileged port), and incorrect sockaddr structure setup.

## Common Error Messages

- `bind: Address already in use (EADDRINUSE)`
- `bind: Permission denied (EACCES)`
- `bind: Cannot assign requested address (EADDRNOTAVAIL)`
- `bind: Invalid argument (EINVAL)`

## How to Fix It

### Use SO_REUSEADDR before bind

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>

int main(void) {
    int fd = socket(AF_INET, SOCK_STREAM, 0);
    int opt = 1;
    setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
    struct sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_port = htons(8080),
        .sin_addr.s_addr = INADDR_ANY
    };
    if (bind(fd, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        perror("bind");
    }
    close(fd);
    return 0;
}
```

### Use specific interface address

```c
#include <sys/socket.h>
#include <arpa/inet.h>

int main(void) {
    int fd = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_port = htons(3000),
        .sin_addr.s_addr = inet_addr("127.0.0.1")
    };
    bind(fd, (struct sockaddr *)&addr, sizeof(addr));
    close(fd);
    return 0;
}
```

### Bind IPv6 socket

```c
#include <sys/socket.h>
#include <netinet/in.h>

int main(void) {
    int fd = socket(AF_INET6, SOCK_STREAM, 0);
    int off = 0;
    setsockopt(fd, IPPROTO_IPV6, IPV6_V6ONLY, &off, sizeof(off));
    struct sockaddr_in6 addr = {
        .sin6_family = AF_INET6,
        .sin6_port = htons(8080),
        .sin6_addr = in6addr_any
    };
    bind(fd, (struct sockaddr *)&addr, sizeof(addr));
    close(fd);
    return 0;
}
```

### Bind to Unix domain socket

```c
#include <sys/socket.h>
#include <sys/un.h>
#include <stdio.h>

int main(void) {
    int fd = socket(AF_UNIX, SOCK_STREAM, 0);
    struct sockaddr_un addr = { .sun_family = AF_UNIX };
    strncpy(addr.sun_path, "/tmp/mysock", sizeof(addr.sun_path) - 1);
    unlink(addr.sun_path);
    bind(fd, (struct sockaddr *)&addr, sizeof(addr));
    listen(fd, 5);
    close(fd);
    return 0;
}
```

## Common Scenarios

### Scenario 1: EADDRINUSE from previous socket in TIME_WAIT

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: EACCES from binding to port < 1024 as non-root

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Wrong sockaddr structure size causes EINVAL

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always set SO_REUSEADDR before bind
- **Tip 2:** Use root or capabilities for ports below 1024
- **Tip 3:** Ensure sockaddr structure size matches address family
