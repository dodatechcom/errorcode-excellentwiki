---
title: "[Solution] Linux EALREADY (errno 78) — Operation Already in Progress Fix"
description: "Fix Linux EALREADY (errno 78) Operation already in progress error. Solutions for non-blocking socket and operation issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux EALREADY (errno 78) — Operation Already in Progress

EALREADY (errno 78) means a non-blocking operation is already in progress. This error occurs when a program tries to initiate a new operation on a socket that already has an operation pending, such as calling `connect()` on a non-blocking socket that is already attempting to connect. It is distinct from EINPROGRESS (errno 115) because EALREADY indicates the operation was already started, while EINPROGRESS indicates the initial pending state.

## Common Causes

- Calling `connect()` twice on a non-blocking socket
- Attempting a new operation before the previous one completed
- Race condition in event-driven I/O programs
- Application logic error in managing non-blocking sockets

## How to Fix EALREADY

### 1. Check Socket Blocking Mode

Verify if the socket is in non-blocking mode:

```bash
strace -e trace=fcntl ./program | grep F_SETFL
```

### 2. Wait for Previous Operation to Complete

Use `poll()` or `select()` to wait for the socket state:

```bash
# In C: use poll to check socket readiness
struct pollfd fds = { .fd = sock, .events = POLLOUT };
poll(&fds, 1, timeout_ms);
```

### 3. Use Non-Blocking I/O Properly

Check for EALREADY and handle it:

```bash
# In C: handle EALREADY
if (errno == EALREADY) {
    // Previous connect still in progress, wait and retry
}
```

### 4. Use epoll for Event-Driven I/O

Monitor socket state with epoll:

```bash
# In C: add socket to epoll
epoll_ctl(epfd, EPOLL_CTL_ADD, sock, &event);
```

## Verification

After fixing the non-blocking logic, confirm operations succeed:

```bash
strace -e trace=connect,poll,select ./program
```

## Related Error Codes

- [EINPROGRESS (errno 79)](/os/linux/errno-79/) — Operation now in progress
- [EISCONN (errno 70)](/os/linux/errno-70/) — Already connected
- [EAGAIN (errno 11)](/os/linux/errno-11/) — Resource temporarily unavailable
