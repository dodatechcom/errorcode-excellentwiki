---
title: "[Solution] C socket() Error — How to Fix"
description: "Fix C socket creation errors including protocol mismatch, address family, and descriptor limits."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C socket() Error — How to Fix

socket() creates a communication endpoint. Common errors include wrong address family, protocol mismatch, and exceeding fd limits. Not checking return value leads to using invalid socket descriptors.

## Common Error Messages

- `socket: Protocol not supported (EPROTONOSUPPORT)`
- `socket: Too many open files (EMFILE)`
- `socket: Address family not supported (EAFNOSUPPORT)`
- `socket: No such device or address`

## How to Fix It

### Check socket return value

```c
#include <sys/socket.h>
#include <stdio.h>

int main(void) {
    int fd = socket(AF_INET, SOCK_STREAM, 0);
    if (fd == -1) { perror("socket"); return 1; }
    printf("Socket fd: %d\n", fd);
    close(fd);
    return 0;
}
```

### Use correct address family

```c
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdio.h>

int main(void) {
    int fd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (fd == -1) { perror("socket"); return 1; }
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

### Set socket options before bind

```c
#include <sys/socket.h>

int main(void) {
    int fd = socket(AF_INET, SOCK_STREAM, 0);
    int opt = 1;
    setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
    setsockopt(fd, SOL_SOCKET, SO_REUSEPORT, &opt, sizeof(opt));
    close(fd);
    return 0;
}
```

### Create UDP socket

```c
#include <sys/socket.h>
#include <stdio.h>

int main(void) {
    int fd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if (fd == -1) { perror("socket"); return 1; }
    printf("UDP socket: %d\n", fd);
    close(fd);
    return 0;
}
```

## Common Scenarios

### Scenario 1: socket() returns -1 due to wrong protocol

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Using invalid socket fd after creation failure

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Not setting SO_REUSEADDR causing bind failure after restart

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always check socket() return value
- **Tip 2:** Use correct AF_INET/AF_INET6 and SOCK_STREAM/SOCK_DGRAM
- **Tip 3:** Set SO_REUSEADDR before bind to avoid address-in-use errors
