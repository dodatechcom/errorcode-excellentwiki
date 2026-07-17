---
title: "[Solution] Linux EINPROGRESS (errno 79) — Operation Now in Progress Fix"
description: "Fix Linux EINPROGRESS (errno 79) Operation now in progress error. Solutions for non-blocking connection and I/O issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux EINPROGRESS (errno 79) — Operation Now in Progress

EINPROGRESS (errno 79) means a non-blocking operation has been initiated and is currently in progress. This is typically a normal return value from `connect()` on a non-blocking socket, indicating the connection attempt has started but not yet completed. It is distinct from EALREADY (errno 78) because EINPROGRESS indicates the first time an operation is pending, while EALREADY indicates a repeated attempt.

## Common Causes

- `connect()` called on a non-blocking socket (normal behavior)
- Application not waiting for the connection to complete
- Event loop not properly monitoring socket readiness
- DNS resolution is taking longer than expected

## How to Fix EINPROGRESS

### 1. Understand This Is Normal

For non-blocking sockets, EINPROGRESS from `connect()` is expected. Wait for the socket to become writable:

```bash
# In C: use poll() to wait for connection
struct pollfd fds = { .fd = sock, .events = POLLOUT };
int ret = poll(&fds, 1, timeout_ms);
if (ret > 0 && (fds.revents & POLLOUT)) {
    // Connection completed, check for errors
    int error;
    socklen_t len = sizeof(error);
    getsockopt(sock, SOL_SOCKET, SO_ERROR, &error, &len);
}
```

### 2. Use select() to Monitor the Socket

Wait for the socket to become ready:

```bash
# In C: use select()
fd_set writefds;
FD_ZERO(&writefds);
FD_SET(sock, &writefds);
struct timeval tv = { .tv_sec = 5 };
select(sock + 1, NULL, &writefds, NULL, &tv);
```

### 3. Use epoll for Scalable I/O

For many connections, use epoll:

```bash
# In C: add to epoll with EPOLLOUT
struct epoll_event ev = { .events = EPOLLOUT, .data.fd = sock };
epoll_ctl(epfd, EPOLL_CTL_ADD, sock, &ev);
```

### 4. Set Appropriate Timeouts

Configure connection timeout to avoid hanging:

```bash
# In C: set socket timeout
struct timeval tv = { .tv_sec = 10 };
setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, &tv, sizeof(tv));
setsockopt(sock, SOL_SOCKET, SO_SNDTIMEO, &tv, sizeof(tv));
```

## Verification

After implementing proper event handling, confirm connections complete:

```bash
strace -e trace=connect,poll,select,epoll_wait ./program
```

## Related Error Codes

- [EALREADY (errno 78)](/os/linux/errno-78/) — Operation already in progress
- [ETIMEDOUT (errno 74)](/os/linux/errno-74/) — Connection timed out
- [ECONNREFUSED (errno 75)](/os/linux/errno-75/) — Connection refused
