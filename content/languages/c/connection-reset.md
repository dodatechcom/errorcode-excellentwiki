---
title: "[Solution] C Connection reset by peer: ECONNRESET"
description: "Fix C connection reset by peer (ECONNRESET). Handle abrupt connection closures gracefully."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["econnreset", "connection-reset", "peer", "socket", "errno"]
weight: 5
---

# Connection reset by peer: ECONNRESET

ECONNRESET occurs when the remote end of a connection abruptly closes it (sends a RST packet) while data is being transferred.

## Common Causes

```c
// Cause 1: Server crashed
send(sock, "data", 4, 0); // server process died

// Cause 2: Server closed connection
// Server called close() on socket

// Cause 3: Firewall RST
// Firewall injecting RST packet
```

## How to Fix

### Fix 1: Handle gracefully

```c
ssize_t result = recv(sock, buf, size, 0);
if (result == -1 && errno == ECONNRESET) {
    fprintf(stderr, "Connection reset by peer\n");
    close(sock);
}
```

### Fix 2: Use keepalive

```c
int opt = 1;
setsockopt(sock, SOL_SOCKET, SO_KEEPALIVE, &opt, sizeof(opt));
```

### Fix 3: Implement reconnection

```c
for (int i = 0; i < 3; i++) {
    if (connect(sock, (struct sockaddr*)&addr, sizeof(addr)) == 0) {
        break;
    }
    sleep(1);
}
```

## Related Errors

- [Broken pipe]({{< relref "/languages/c/broken-pipe" >}}) — EPIPE.
- [Connection refused]({{< relref "/languages/c/connection-refused-c" >}}) — ECONNREFUSED.
- [Connection timed out]({{< relref "/languages/c/operation-timed-out" >}}) — ETIMEDOUT.
