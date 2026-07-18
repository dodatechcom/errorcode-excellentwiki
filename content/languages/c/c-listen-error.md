---
title: "[Solution] C listen() Error — How to Fix"
description: "Fix C listen() errors including backlog tuning, non-blocking issues, and errno handling."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C listen() Error — How to Fix

listen() marks a socket as passive (server). Common errors include calling listen before bind, using invalid backlog values, and not handling the transition from listen to accept properly.

## Common Error Messages

- `listen: Invalid argument (EINVAL)`
- `listen: Transport endpoint is not connected (ENOTCONN)`
- `listen: Too many open files (EMFILE)`
- `Connection backlog full — clients rejected`

## How to Fix It

### Check listen return value

```c
#include <sys/socket.h>
#include <stdio.h>

int main(void) {
    int fd = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_port = htons(8080),
        .sin_addr.s_addr = INADDR_ANY
    };
    bind(fd, (struct sockaddr *)&addr, sizeof(addr));
    if (listen(fd, 128) == -1) {
        perror("listen");
        close(fd);
        return 1;
    }
    printf("Listening on port 8080\n");
    close(fd);
    return 0;
}
```

### Tune backlog appropriately

```c
#include <sys/socket.h>
#include <stdio.h>

int main(void) {
    int fd = socket(AF_INET, SOCK_STREAM, 0);
    // ... bind ...
    int backlog = 128;  // SOMAXCONN on Linux
    if (listen(fd, backlog) == -1) {
        perror("listen");
    }
    close(fd);
    return 0;
}
```

### Use non-blocking server pattern

```c
#include <sys/socket.h>
#include <fcntl.h>
#include <stdio.h>

int main(void) {
    int fd = socket(AF_INET, SOCK_STREAM, 0);
    int flags = fcntl(fd, F_GETFL, 0);
    fcntl(fd, F_SETFL, flags | O_NONBLOCK);
    struct sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_port = htons(8080),
        .sin_addr.s_addr = INADDR_ANY
    };
    bind(fd, (struct sockaddr *)&addr, sizeof(addr));
    listen(fd, 128);
    close(fd);
    return 0;
}
```

### Full server startup pattern

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>

int create_server(int port) {
    int fd = socket(AF_INET, SOCK_STREAM, 0);
    int opt = 1;
    setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
    struct sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_port = htons(port),
        .sin_addr.s_addr = INADDR_ANY
    };
    if (bind(fd, (struct sockaddr *)&addr, sizeof(addr)) == -1) return -1;
    if (listen(fd, 128) == -1) return -1;
    return fd;
}
```

## Common Scenarios

### Scenario 1: Calling listen before bind

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Using backlog value that is negative or too large

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Not setting SO_REUSEADDR causing bind to fail after restart

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always call bind before listen
- **Tip 2:** Use SOMAXCONN or reasonable backlog value
- **Tip 3:** Set SO_REUSEADDR for quick server restart
