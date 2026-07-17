---
title: "[Solution] C Message too long: EMSGSIZE"
description: "Fix C message too long (EMSGSIZE). Split large messages or increase buffer sizes."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Message too long: EMSGSIZE

EMSGSIZE occurs when a message exceeds the maximum size allowed by the protocol or socket buffer. For UDP, this is typically ~65,507 bytes.

## Common Causes

```c
// Cause 1: UDP message too large
char huge[100000];
sendto(sock, huge, sizeof(huge), 0, ...); // EMSGSIZE

// Cause 2: Exceeding send buffer
// Kernel buffer full

// Cause 3: Protocol limit
// Some protocols have message size limits
```

## How to Fix

### Fix 1: Fragment large messages

```c
#define MAX_MSG 65507
for (size_t offset = 0; offset < total; offset += MAX_MSG) {
    size_t chunk = total - offset;
    if (chunk > MAX_MSG) chunk = MAX_MSG;
    sendto(sock, data + offset, chunk, 0, ...);
}
```

### Fix 2: Use TCP for large data

```c
// TCP handles fragmentation automatically
int sock = socket(AF_INET, SOCK_STREAM, 0);
send(sock, huge, sizeof(huge), 0); // OK
```

### Fix 3: Increase buffer size

```c
int buf_size = 1048576; // 1MB
setsockopt(sock, SOL_SOCKET, SO_SNDBUF, &buf_size, sizeof(buf_size));
```

## Related Errors

- [No buffer space]({{< relref "/languages/c/no-buffer-space" >}}) — ENOBUFS.
- [Connection reset]({{< relref "/languages/c/connection-reset" >}}) — ECONNRESET.
- [Bad file descriptor]({{< relref "/languages/c/bad-file-descriptor" >}}) — EBADF.
