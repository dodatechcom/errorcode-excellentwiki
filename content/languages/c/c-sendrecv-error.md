---
title: "[Solution] C send/recv Error — How to Fix"
description: "Fix C send() and recv() errors including partial sends, EPIPE, and non-blocking I/O."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C send/recv Error — How to Fix

send/recv may transfer fewer bytes than requested. Common errors include not handling partial sends (short write), ignoring EPIPE/ECONNRESET, and not looping until all data is sent/received.

## Common Error Messages

- `send: Broken pipe (EPIPE)`
- `send: Connection reset by peer (ECONNRESET)`
- `recv returns 0 — connection closed`
- `send/recv: Resource temporarily unavailable (EAGAIN)`

## How to Fix It

### Loop to handle partial sends

```c
#include <sys/socket.h>
#include <unistd.h>
#include <errno.h>

int send_all(int fd, const void *buf, size_t len) {
    const char *p = (const char *)buf;
    size_t sent = 0;
    while (sent < len) {
        ssize_t n = send(fd, p + sent, len - sent, MSG_NOSIGNAL);
        if (n == -1) {
            if (errno == EINTR) continue;
            return -1;
        }
        sent += n;
    }
    return 0;
}
```

### Handle recv returning 0 or error

```c
#include <sys/socket.h>
#include <unistd.h>
#include <errno.h>

int recv_all(int fd, void *buf, size_t len) {
    char *p = (char *)buf;
    size_t received = 0;
    while (received < len) {
        ssize_t n = recv(fd, p + received, len - received, 0);
        if (n <= 0) {
            if (n == 0) return 0;  // connection closed
            if (errno == EINTR) continue;
            return -1;
        }
        received += n;
    }
    return received;
}
```

### Use MSG_NOSIGNAL to prevent EPIPE

```c
#include <sys/socket.h>
#include <unistd.h>

int main(void) {
    int fd = socket(AF_INET, SOCK_STREAM, 0);
    // ... connect ...
    ssize_t n = send(fd, "hello", 5, MSG_NOSIGNAL);
    if (n == -1) perror("send");
    close(fd);
    return 0;
}
```

### Non-blocking send/recv with poll

```c
#include <sys/socket.h>
#include <poll.h>
#include <errno.h>

int send_nb(int fd, const void *buf, size_t len) {
    struct pollfd pfd = { .fd = fd, .events = POLLOUT };
    size_t sent = 0;
    while (sent < len) {
        ssize_t n = send(fd, (const char *)buf + sent, len - sent, MSG_NOSIGNAL);
        if (n > 0) { sent += n; continue; }
        if (n == -1 && errno == EAGAIN) {
            poll(&pfd, 1, -1);
            continue;
        }
        return -1;
    }
    return 0;
}
```

## Common Scenarios

### Scenario 1: send() returns fewer bytes than requested

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Ignoring EPIPE causing process termination

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: recv returns 0 meaning peer closed connection

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always loop until all bytes are sent/received
- **Tip 2:** Use MSG_NOSIGNAL or handle SIGPIPE to prevent EPIPE crashes
- **Tip 3:** Handle recv returning 0 as connection close
