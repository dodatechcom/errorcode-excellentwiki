---
title: "[Solution] Linux EAGAIN (errno 11) — Resource Temporarily Unavailable Fix"
description: "Fix Linux EAGAIN (errno 11) Resource Temporarily Unavailable error. Handle non-blocking I/O, poll/select/epoll, and resource exhaustion."
platforms: ["linux"]
severities: ["error"]
error_types: ["runtime"]
weight: 110
---

# Linux EAGAIN (errno 11) — Resource Temporarily Unavailable

EAGAIN (errno 11) means the resource you requested is not available at this moment, but it may become available later. This is distinct from EWOULDBLOCK in some implementations, but on Linux they share the same value. It commonly appears when performing non-blocking I/O on a file descriptor that would block, or when a system-wide resource limit has been reached. It is not an error in the traditional sense — it is a signal to try again.

## Common Causes

- Non-blocking socket or file descriptor has no data ready to read
- Non-blocking socket cannot accept more data to write
- Process hit a per-process or system-wide resource limit
- Semaphore or mutex is currently unavailable
- Fork failed due to memory limits
- Thread creation hit the `RLIMIT_NPROC` limit

## How to Fix EAGAIN

### 1. Retry the Operation

The simplest approach for transient EAGAIN:

```c
int flags = fcntl(fd, F_GETFL);
fcntl(fd, F_SETFL, flags | O_NONBLOCK);

ssize_t n;
do {
    n = read(fd, buffer, sizeof(buffer));
} while (n == -1 && errno == EAGAIN);
```

### 2. Use select() for Readability/Writability

Wait until the file descriptor is ready before operating on it:

```c
#include <sys/select.h>

fd_set readfds;
FD_ZERO(&readfds);
FD_SET(fd, &readfds);

struct timeval tv = { .tv_sec = 5, .tv_usec = 0 };

int ready = select(fd + 1, &readfds, NULL, NULL, &tv);
if (ready > 0 && FD_ISSET(fd, &readfds)) {
    ssize_t n = read(fd, buffer, sizeof(buffer));
    if (n == -1 && errno == EAGAIN) {
        // Should not happen after select says ready, but handle it
    }
}
```

### 3. Use poll() as an Alternative to select()

`poll()` scales better than `select()` with many file descriptors:

```c
#include <poll.h>

struct pollfd pfd = {
    .fd = fd,
    .events = POLLIN,  // Wait for readability
    .revents = 0
};

int ready = poll(&pfd, 1, 5000); // 5 second timeout
if (ready > 0 && (pfd.revents & POLLIN)) {
    ssize_t n = read(fd, buffer, sizeof(buffer));
}
```

### 4. Use epoll for High-Performance I/O (Linux)

`epoll` is the preferred method on Linux for monitoring many file descriptors:

```c
#include <sys/epoll.h>

int epfd = epoll_create1(0);

struct epoll_event ev = {
    .events = EPOLLIN,
    .data.fd = fd
};
epoll_ctl(epfd, EPOLL_CTL_ADD, fd, &ev);

struct epoll_event events[10];
int nfds = epoll_wait(epfd, events, 10, 5000);

for (int i = 0; i < nfds; i++) {
    ssize_t n = read(events[i].data.fd, buffer, sizeof(buffer));
    if (n == -1 && errno == EAGAIN) {
        // Handle transient condition
    }
}
```

### 5. Check and Increase Resource Limits

If EAGAIN comes from hitting a resource limit, identify and adjust it:

```bash
# View current limits
ulimit -a

# Check specific limits
ulimit -n      # open files
ulimit -u      # max user processes
ulimit -s      # stack size

# Temporarily increase open files
ulimit -n 65535

# Check system-wide limits
cat /proc/sys/fs/file-max
cat /proc/sys/kernel/threads-max
```

For persistent changes, edit `/etc/security/limits.conf`:

```
* soft nofile 65535
* hard nofile 65535
* soft nproc 65535
* hard nproc 65535
```

### 6. Handle EAGAIN in Network Servers

In a server, EAGAIN on `accept()` or `recv()` means no more connections or data are ready:

```c
// Non-blocking accept loop
while (1) {
    int client_fd = accept(server_fd, &addr, &addrlen);
    if (client_fd == -1) {
        if (errno == EAGAIN || errno == EWOULDBLOCK) {
            // No more pending connections, wait with epoll
            epoll_wait(epfd, events, MAX_EVENTS, -1);
            continue;
        }
        perror("accept");
        break;
    }
    handle_client(client_fd);
}
```

### 7. Fix Thread/Fork Resource Exhaustion

EAGAIN from `fork()` or `pthread_create()` means you hit process/thread limits:

```bash
# Check current nproc limit
ulimit -u

# Check how many processes you have
ps -u $(whoami) | wc -l

# Increase the limit
ulimit -u 4096
```

### 8. Python: Handle EAGAIN Gracefully

```python
import os
import errno

def read_nonblocking(fd, size):
    while True:
        try:
            return os.read(fd, size)
        except OSError as e:
            if e.errno == errno.EAGAIN:
                import select
                select.select([fd], [], [])  # Wait for readability
                continue
            raise
```

## Key Differences on Linux

On Linux, `EAGAIN` and `EWOULDBLOCK` are the same value (11). Your code can check either. POSIX allows them to be different, so portable code should check both:

```c
if (errno == EAGAIN || errno == EWOULDBLOCK) {
    // Resource unavailable, retry later
}
```

## Related Error Codes

- [EINTR (errno 4)](/os/linux/errno-4/) — Interrupted system call
- [EWOULDBLOCK (errno 11)](/os/linux/errno-11/) — Operation would block (same as EAGAIN on Linux)
- [ENOMEM (errno 12)](/os/linux/errno-12/) — Out of memory
