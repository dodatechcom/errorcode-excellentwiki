---
title: "[Solution] C Software caused connection abort: ECONNABORTED"
description: "Fix C software caused connection abort (ECONNABORTED). Handle abnormal connection closures."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Software caused connection abort: ECONNABORTED

ECONNABORTED occurs when a connection is aborted by the local software, typically due to a timeout or protocol error detected by the local TCP stack.

## Common Causes

```c
// Cause 1: Keepalive timeout
// Connection idle too long, local TCP stack aborted

// Cause 2: Protocol error detected locally
// Local side detected invalid data

// Cause 3: Firewall timeout
// Firewall killed idle connection
```

## How to Fix

### Fix 1: Configure keepalive

```c
int idle = 60; // seconds
setsockopt(sock, IPPROTO_TCP, TCP_KEEPIDLE, &idle, sizeof(idle));

int interval = 10;
setsockopt(sock, IPPROTO_TCP, TCP_KEEPINTVL, &interval, sizeof(interval));

int count = 6;
setsockopt(sock, IPPROTO_TCP, TCP_KEEPCNT, &count, sizeof(count));
```

### Fix 2: Handle gracefully

```c
ssize_t result = recv(sock, buf, size, 0);
if (result == -1 && errno == ECONNABORTED) {
    fprintf(stderr, "Connection aborted\n");
    close(sock);
}
```

### Fix 3: Reconnect automatically

```c
// Implement retry logic
```

## Related Errors

- [Connection reset]({{< relref "/languages/c/connection-reset" >}}) — ECONNRESET.
- [Connection timed out]({{< relref "/languages/c/operation-timed-out" >}}) — ETIMEDOUT.
- [Broken pipe]({{< relref "/languages/c/broken-pipe" >}}) — EPIPE.
