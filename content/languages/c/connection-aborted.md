---
title: "[Solution] C Connection aborted: ECONNABORTED"
description: "Fix C connection aborted (ECONNABORTED). Handle aborted connections gracefully."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Connection aborted: ECONNABORTED

ECONNABORTED indicates a connection was aborted by the operating system, usually due to a TCP keepalive timeout or local protocol error detection.

## Common Causes

```c
// Cause 1: TCP keepalive timeout
// Connection idle for too long

// Cause 2: Local protocol error
// TCP stack detected invalid sequence

// Cause 3: Application close during pending I/O
```

## How to Fix

### Fix 1: Enable TCP keepalive

```c
int enable = 1;
setsockopt(sock, SOL_SOCKET, SO_KEEPALIVE, &enable, sizeof(enable));
```

### Fix 2: Send periodic keepalives

```c
// Application-level heartbeat
time_t last_active = time(NULL);
while (1) {
    if (time(NULL) - last_active > 30) {
        send(sock, "ping", 4, 0);
        last_active = time(NULL);
    }
}
```

### Fix 3: Handle and reconnect

```c
if (errno == ECONNABORTED) {
    close(sock);
    sock = reconnect(addr);
}
```

## Related Errors

- [Connection reset]({{< relref "/languages/c/connection-reset" >}}) — ECONNRESET.
- [Connection timed out]({{< relref "/languages/c/operation-timed-out" >}}) — ETIMEDOUT.
- [Broken pipe]({{< relref "/languages/c/broken-pipe" >}}) — EPIPE.
