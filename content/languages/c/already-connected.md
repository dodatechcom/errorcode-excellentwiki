---
title: "[Solution] C Socket is already connected: EISCONN"
description: "Fix C socket is already connected (EISCONN). Don't connect an already-connected socket."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Socket is already connected: EISCONN

EISCONN occurs when you try to `connect()` a socket that is already connected, or when you use `sendto()` on a connected TCP socket.

## Common Causes

```c
// Cause 1: Double connect
connect(sock, (struct sockaddr*)&addr, sizeof(addr)); // first connect
connect(sock, (struct sockaddr*)&addr2, sizeof(addr2)); // EISCONN

// Cause 2: sendto on connected socket
// Use send() instead for connected sockets

// Cause 3: UDP connect then sendto
connect(sock, (struct sockaddr*)&addr, sizeof(addr));
sendto(sock, data, len, 0, (struct sockaddr*)&addr, sizeof(addr)); // EISCONN
```

## How to Fix

### Fix 1: Check connection status first

```c
struct sockaddr_in peer;
socklen_t len = sizeof(peer);
if (getpeername(sock, (struct sockaddr*)&peer, &len) == 0) {
    // already connected
} else {
    connect(sock, (struct sockaddr*)&addr, sizeof(addr));
}
```

### Fix 2: Use send() for connected sockets

```c
// After connect(), use send()
send(sock, data, len, 0); // OK
```

### Fix 3: Use sendto() for unconnected UDP

```c
// Before connect(), use sendto()
sendto(sock, data, len, 0, (struct sockaddr*)&addr, sizeof(addr));
```

## Related Errors

- [Not connected]({{< relref "/languages/c/not-connected" >}}) — ENOTCONN.
- [Connection refused]({{< relref "/languages/c/connection-refused-c" >}}) — ECONNREFUSED.
- [Bad file descriptor]({{< relref "/languages/c/bad-file-descriptor" >}}) — EBADF.
