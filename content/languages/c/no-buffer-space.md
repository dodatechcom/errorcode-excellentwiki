---
title: "[Solution] C No buffer space available: ENOBUFS"
description: "Fix C no buffer space available (ENOBUFS). Reduce buffer usage or increase system limits."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# No buffer space available: ENOBUFS

ENOBUFS occurs when the system has run out of buffer space for network operations. This can happen with too many connections or excessive data in flight.

## Common Causes

```c
// Cause 1: Too many connections
for (int i = 0; i < 10000; i++) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    // buffers exhausted
}

// Cause 2: Sending too much data
// Socket send buffer full

// Cause 3: Too many UDP datagrams
// Recv buffer full
```

## How to Fix

### Fix 1: Increase buffer limits

```bash
sysctl -w net.core.rmem_max=16777216
sysctl -w net.core.wmem_max=16777216
```

### Fix 2: Limit concurrent connections

```c
// Don't open too many sockets
if (connection_count >= MAX_CONNECTIONS) {
    fprintf(stderr, "Too many connections\n");
    return -1;
}
```

### Fix 3: Reduce send rate

```c
// Send in smaller chunks with delays
for (int i = 0; i < chunks; i++) {
    send(sock, data + offset, chunk_size, 0);
    usleep(1000); // throttle
}
```

## Related Errors

- [Message too long]({{< relref "/languages/c/message-too-long" >}}) — EMSGSIZE.
- [Too many open files]({{< relref "/languages/c/too-many-open-files" >}}) — EMFILE.
- [Out of memory]({{< relref "/languages/c/out-of-memory-malloc" >}}) — malloc failure.
