---
title: "[Solution] C accept() Error — How to Fix"
description: "Fix C accept() errors including EMFILE, non-blocking accept, and connection handling."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C accept() Error — How to Fix

accept() extracts a pending connection. Common errors include EMFILE (too many connections), not handling EAGAIN on non-blocking sockets, and not closing the accepted fd on error.

## Common Error Messages

- `accept: Too many open files (EMFILE)`
- `accept: Invalid argument (EINVAL)`
- `accept: Resource temporarily unavailable (EAGAIN)`
- `Accepted connection fd leaked — not closed`

## How to Fix It

### Check accept return value

```c
#include <sys/socket.h>
#include <stdio.h>

int main(void) {
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    // ... bind, listen ...
    struct sockaddr_in client_addr;
    socklen_t client_len = sizeof(client_addr);
    int client_fd = accept(server_fd, (struct sockaddr *)&client_addr, &client_len);
    if (client_fd == -1) {
        perror("accept");
        return 1;
    }
    // handle client ...
    close(client_fd);
    close(server_fd);
    return 0;
}
```

### Handle EMFILE gracefully

```c
#include <sys/socket.h>
#include <errno.h>

int accept_connection(int server_fd) {
    int client_fd = accept(server_fd, NULL, NULL);
    if (client_fd == -1) {
        if (errno == EMFILE || errno == ENFILE) {
            // temp fd to drain pending connections
            int tmp = accept(server_fd, NULL, NULL);
            if (tmp != -1) close(tmp);
        }
        return -1;
    }
    return client_fd;
}
```

### Non-blocking accept with poll

```c
#include <sys/socket.h>
#include <poll.h>
#include <stdio.h>

int main(void) {
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    // ... bind, listen ...
    struct pollfd pfd = { .fd = server_fd, .events = POLLIN };
    while (1) {
        int ret = poll(&pfd, 1, -1);
        if (ret > 0 && (pfd.revents & POLLIN)) {
            int client_fd = accept(server_fd, NULL, NULL);
            if (client_fd != -1) {
                printf("New connection: fd=%d\n", client_fd);
                close(client_fd);
            }
        }
    }
    return 0;
}
```

### Accept with client info

```c
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdio.h>

void handle_accept(int server_fd) {
    struct sockaddr_in client;
    socklen_t len = sizeof(client);
    int fd = accept(server_fd, (struct sockaddr *)&client, &len);
    if (fd != -1) {
        printf("Client: %s:%d\n", inet_ntoa(client.sin_addr), ntohs(client.sin_port));
        close(fd);
    }
}
```

## Common Scenarios

### Scenario 1: accept returns -1 but errno not checked

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: EMFILE reached — no graceful handling

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Accepted fd not closed causing fd leak

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always check accept return value and errno
- **Tip 2:** Handle EMFILE by temporarily draining connections
- **Tip 3:** Close accepted fd as soon as you are done with it
