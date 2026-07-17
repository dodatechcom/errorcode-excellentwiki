---
title: "[Solution] C errno 115 EINPROGRESS — Operation in Progress Fix"
description: "Fix C errno 115 EINPROGRESS for non-blocking sockets. Use select/poll/epoll to wait for connection, handle async I/O, and check socket errors."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 35
---

# [Solution] C errno 115 EINPROGRESS — Operation in Progress Fix

When you call `connect()` on a non-blocking socket, the connection cannot complete immediately. Instead of blocking, the kernel starts the connection in the background and returns `-1` with `errno` set to `EINPROGRESS` (110 on Linux). This is not an error — it is the expected behavior for non-blocking I/O. You must use `select()`, `poll()`, or `epoll()` to wait for the socket to become writable, then check the connection result with `getsockopt(SO_ERROR)`.

## What You'll See

```c
// Set socket to non-blocking
int flags = fcntl(sockfd, F_GETFL, 0);
fcntl(sockfd, F_SETFL, flags | O_NONBLOCK);

int result = connect(sockfd, (struct sockaddr *)&addr, sizeof(addr));
if (result == -1) {
    if (errno == EINPROGRESS) {
        // This is expected — connection is being established
        printf("Connection in progress, errno: %d\n", errno);  // 115
    }
}
```

## Common Mistake

```c
// WRONG — treating EINPROGRESS as a fatal error
if (connect(sockfd, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
    perror("connect");  // "Connection in progress"
    close(sockfd);
    return 1;  // exits without ever completing the connection
}
```

## Correct: Non-blocking connect with select()

```c
#include <sys/socket.h>
#include <sys/select.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);

    // Set non-blocking
    int flags = fcntl(sockfd, F_GETFL, 0);
    fcntl(sockfd, F_SETFL, flags | O_NONBLOCK);

    struct sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_port = htons(80),
    };
    inet_pton(AF_INET, "93.184.216.34", &addr.sin_addr);

    int ret = connect(sockfd, (struct sockaddr *)&addr, sizeof(addr));
    if (ret == 0) {
        // Connected immediately (rare, usually on localhost)
    } else if (errno == EINPROGRESS) {
        // Wait for the socket to become writable (connection completed)
        fd_set writefds;
        FD_ZERO(&writefds);
        FD_SET(sockfd, &writefds);

        struct timeval tv = { .tv_sec = 5, .tv_usec = 0 };  // 5-second timeout

        ret = select(sockfd + 1, NULL, &writefds, NULL, &tv);
        if (ret > 0 && FD_ISSET(sockfd, &writefds)) {
            // Check if the connection succeeded or failed
            int error = 0;
            socklen_t len = sizeof(error);
            getsockopt(sockfd, SOL_SOCKET, SO_ERROR, &error, &len);

            if (error != 0) {
                fprintf(stderr, "Connection failed: %s\n", strerror(error));
                close(sockfd);
                return 1;
            }
            printf("Connected!\n");
        } else {
            fprintf(stderr, "Connection timed out\n");
            close(sockfd);
            return 1;
        }
    } else {
        perror("connect");
        close(sockfd);
        return 1;
    }

    close(sockfd);
    return 0;
}
```

## Correct: Non-blocking connect with poll()

```c
#include <poll.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>

int connect_with_poll(const char *ip, int port, int timeout_ms) {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    int flags = fcntl(sockfd, F_GETFL, 0);
    fcntl(sockfd, F_SETFL, flags | O_NONBLOCK);

    struct sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_port = htons(port),
    };
    inet_pton(AF_INET, ip, &addr.sin_addr);

    int ret = connect(sockfd, (struct sockaddr *)&addr, sizeof(addr));
    if (ret == 0 || errno == EISCONN) {
        return sockfd;  // already connected
    }

    if (errno != EINPROGRESS) {
        close(sockfd);
        return -1;
    }

    struct pollfd pfd = { .fd = sockfd, .events = POLLOUT };
    ret = poll(&pfd, 1, timeout_ms);

    if (ret > 0 && (pfd.revents & POLLOUT)) {
        int error = 0;
        socklen_t len = sizeof(error);
        getsockopt(sockfd, SOL_SOCKET, SO_ERROR, &error, &len);
        if (error == 0) {
            return sockfd;
        }
    }

    close(sockfd);
    return -1;
}
```

## Correct: Non-blocking connect with epoll (Linux)

```c
#include <sys/epoll.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>

int connect_with_epoll(const char *ip, int port, int timeout_ms) {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    int flags = fcntl(sockfd, F_GETFL, 0);
    fcntl(sockfd, F_SETFL, flags | O_NONBLOCK);

    struct sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_port = htons(port),
    };
    inet_pton(AF_INET, ip, &addr.sin_addr);

    int ret = connect(sockfd, (struct sockaddr *)&addr, sizeof(addr));
    if (ret == 0 || errno == EISCONN) {
        return sockfd;
    }
    if (errno != EINPROGRESS) {
        close(sockfd);
        return -1;
    }

    int epfd = epoll_create1(0);
    struct epoll_event ev = {
        .events = EPOLLOUT | EPOLLERR | EPOLLHUP,
        .data.fd = sockfd,
    };
    epoll_ctl(epfd, EPOLL_CTL_ADD, sockfd, &ev);

    struct epoll_event events[1];
    ret = epoll_wait(epfd, events, 1, timeout_ms);

    if (ret > 0) {
        int error = 0;
        socklen_t len = sizeof(error);
        getsockopt(sockfd, SOL_SOCKET, SO_ERROR, &error, &len);
        close(epfd);
        if (error == 0) return sockfd;
    }

    close(epfd);
    close(sockfd);
    return -1;
}
```

## Summary

| Method | When to Use |
|---|---|
| `select()` | Portable, works on all Unix systems |
| `poll()` | Cleaner API than `select()`, no fd limit |
| `epoll` | High-performance Linux-only (thousands of connections) |
| Check `SO_ERROR` | Always — after select/poll indicates writability |

## Related Errors

- [errno-110 ETIMEDOUT](errno-110) — connection timed out.
- [errno-99 EADDRNOTAVAIL](errno-99) — address not available.
- [errno-32 EPIPE](errno-32) — broken pipe.
