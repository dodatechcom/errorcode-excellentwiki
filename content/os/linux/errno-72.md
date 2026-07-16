---
title: "[Solution] Linux ESHUTDOWN (errno 72) — Cannot Send After Shutdown Fix"
description: "Fix Linux ESHUTDOWN (errno 72) Cannot send after socket shutdown error. Solutions for socket shutdown state issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["eshutdown", "socket", "errno-72", "shutdown", "send"]
weight: 5
---

# Linux ESHUTDOWN (errno 72) — Cannot Send After Shutdown

ESHUTDOWN (errno 72) means the socket has been shut down and cannot accept more data for sending. This error occurs when a program tries to write to a socket that has had its send direction closed via `shutdown()` or the connection has been half-closed. It is distinct from EPIPE (errno 32) because ESHUTDOWN refers to an explicit shutdown, not a broken pipe.

## Common Causes

- `shutdown(sock, SHUT_WR)` was called on the socket
- Socket was half-closed by the application
- Trying to send after calling `close()` in another thread
- Protocol requires reading before sending more data

## How to Fix ESHUTDOWN

### 1. Check Socket Shutdown State

Verify the socket shutdown status:

```bash
ss -tnp | grep <port>
```

### 2. Avoid Writing to Shutdown Sockets

Check the socket state before writing:

```bash
# In C: check with getsockopt for SO_ERROR
int error;
socklen_t len = sizeof(error);
getsockopt(sock, SOL_SOCKET, SO_ERROR, &error, &len);
```

### 3. Create a New Socket

If the socket is shut down, create a new one:

```bash
close(sock);
sock = socket(AF_INET, SOCK_STREAM, 0);
connect(sock, &addr, sizeof(addr));
```

### 4. Use Full Close Instead of Half Shutdown

Use `close()` instead of `shutdown()` when done:

```bash
close(sock);
```

## Verification

After fixing the shutdown state, confirm sending works:

```bash
ss -tnp state established
strace -e trace=send,sendto ./program
```

## Related Error Codes

- [EPIPE (errno 32)](/os/linux/errno-32/) — Broken pipe
- [ENOTCONN (errno 71)](/os/linux/errno-71/) — Not connected
- [ECONNRESET (errno 68)](/os/linux/errno-68/) — Connection reset by peer
