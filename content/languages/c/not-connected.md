---
title: "[Solution] C Socket is not connected: ENOTCONN"
description: "Fix C socket is not connected (ENOTCONN). Connect socket before using send/recv."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Socket is not connected: ENOTCONN

ENOTCONN occurs when you try to send or receive data on a socket that has not been connected (or has been disconnected).

## Common Causes

```c
// Cause 1: Sending before connecting
int sock = socket(AF_INET, SOCK_STREAM, 0);
send(sock, "data", 4, 0); // ENOTCONN — not connected yet

// Cause 2: Connection was closed
// Server closed connection
send(sock, "data", 4, 0); // ENOTCONN

// Cause 3: UDP socket not connected
int sock = socket(AF_INET, SOCK_DGRAM, 0);
send(sock, "data", 4, 0); // ENOTCONN for UDP
```

## How to Fix

### Fix 1: Connect before sending

```c
int sock = socket(AF_INET, SOCK_STREAM, 0);
connect(sock, (struct sockaddr*)&addr, sizeof(addr));
send(sock, "data", 4, 0); // OK now
```

### Fix 2: Check connection status

```c
struct sockaddr_in peer;
socklen_t len = sizeof(peer);
if (getpeername(sock, (struct sockaddr*)&peer, &len) == -1) {
    fprintf(stderr, "Not connected\n");
}
```

### Fix 3: Use sendto for UDP

```c
int sock = socket(AF_INET, SOCK_DGRAM, 0);
sendto(sock, "data", 4, 0, (struct sockaddr*)&addr, sizeof(addr));
```

## Related Errors

- [Connection refused]({{< relref "/languages/c/connection-refused-c" >}}) — ECONNREFUSED.
- [Connection reset]({{< relref "/languages/c/connection-reset" >}}) — ECONNRESET.
- [Not connected]({{< relref "/languages/c/not-connected" >}}) — detailed analysis.
