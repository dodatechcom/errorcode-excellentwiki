---
title: "EAGAIN in C — How to Fix 'Resource Temporarily Unavailable'"
description: "Fix EAGAIN (errno 11) in C — resource temporarily unavailable on sockets, pipes, and non-blocking I/O. With code examples and solutions."
languages: ["c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What is EAGAIN?

**EAGAIN** (Error Again) — errno 11 — means the resource is temporarily unavailable. Try again later. This commonly occurs with non-blocking I/O operations.

On Linux, EAGAIN and EWOULDBLOCK are the same value (11), but on some systems they differ.

**Quick Fix:** Retry the operation, use blocking mode, or implement proper I/O multiplexing with `select()`, `poll()`, or `epoll()`.

## Common Causes

- **Non-blocking socket has no data** to read
- **Non-blocking pipe is full** when writing
- **Process limit reached** (`fork()` failed)
- **File descriptor limit** exceeded

## How to Fix

### 1. Retry the Operation

```c
#include <errno.h>
#include <unistd.h>

ssize_t safe_write(int fd, const void *buf, size_t count) {
    size_t written = 0;
    while (written < count) {
        ssize_t result = write(fd, (const char *)buf + written, count - written);
        if (result > 0) {
            written += result;
        } else if (result == -1) {
            if (errno == EAGAIN || errno == EWOULDBLOCK) {
                // Resource temporarily unavailable, retry
                usleep(1000); // 1ms delay
                continue;
            }
            return -1; // Real error
        }
    }
    return written;
}
```

### 2. Use select() or poll()

```c
#include <sys/select.h>
#include <errno.h>

int wait_for_writable(int fd, int timeout_ms) {
    fd_set write_fds;
    struct timeval tv;

    FD_ZERO(&write_fds);
    FD_SET(fd, &write_fds);

    tv.tv_sec = timeout_ms / 1000;
    tv.tv_usec = (timeout_ms % 1000) * 1000;

    int result = select(fd + 1, NULL, &write_fds, NULL, &tv);
    if (result > 0) {
        return 0; // fd is writable
    } else if (result == 0) {
        return -2; // Timeout
    }
    return -1; // Error
}
```

### 3. Use epoll for High-Performance

```c
#include <sys/epoll.h>

int epoll_wait_for_events(int epfd, struct epoll_event *events, int maxevents) {
    int nfds = epoll_wait(epfd, events, maxevents, 5000); // 5 second timeout
    if (nfds == -1) {
        if (errno == EAGAIN) {
            // No events ready, continue waiting
            return 0;
        }
        perror("epoll_wait");
        return -1;
    }
    return nfds;
}
```

### 4. Set Non-Blocking Mode

```c
#include <fcntl.h>

int set_nonblocking(int fd) {
    int flags = fcntl(fd, F_GETFL, 0);
    if (flags == -1) return -1;
    return fcntl(fd, F_SETFL, flags | O_NONBLOCK);
}
```

## Examples

### Socket Example

```c
#include <sys/socket.h>
#include <errno.h>

int recv_nonblocking(int sockfd, char *buf, size_t len) {
    ssize_t n = recv(sockfd, buf, len, 0);
    if (n == -1) {
        if (errno == EAGAIN || errno == EWOULDBLOCK) {
            printf("No data available yet\n");
            return 0;
        }
        perror("recv");
        return -1;
    }
    return n;
}
```

### Pipe Example

```c
#include <unistd.h>
#include <errno.h>

void write_to_pipe(int pipefd, const char *data) {
    while (1) {
        ssize_t n = write(pipefd, data, strlen(data));
        if (n == -1) {
            if (errno == EAGAIN) {
                // Pipe is full, wait and retry
                usleep(10000); // 10ms
                continue;
            }
            perror("write");
            break;
        }
        break;
    }
}
```

## Quick Command Reference

| Command | Description |
|---------|-------------|
| `errno 11` | Show EAGAIN description |
| `man errno` | List all errno values |
| `strace -e trace=read,write ./program` | Trace I/O syscalls |
| `lsof -p PID` | Check open file descriptors |

## Related Errors

- [EWOULDBLOCK]({{< relref "/languages/c/errno-11" >}}) — same as EAGAIN on Linux
- [ETIMEDOUT]({{< relref "/languages/c/errno-110" >}}) — connection timed out
- [EINPROGRESS]({{< relref "/languages/c/errno-115" >}}) — operation in progress
- [ENOMEM]({{< relref "/languages/c/errno-enomem" >}}) — cannot allocate memory
