---
title: "[Solution] C Socket type not supported: EOPNOTSUPP"
description: "Fix C socket type not supported (EOPNOTSUPP). Use supported socket types for your platform."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["eopnotsupp", "socket-type", "not-supported", "errno", "socket"]
weight: 5
---

# Socket type not supported: EOPNOTSUPP

EOPNOTSUPP occurs when you try to use a socket type or option that is not supported by the underlying system or protocol.

## Common Causes

```c
// Cause 1: Unsupported socket type
int sock = socket(AF_INET, SOCK_RAW, IPPROTO_RAW); // may fail

// Cause 2: Unsupported socket option
setsockopt(sock, SOL_SOCKET, SO_KEEPALIVE, &opt, sizeof(opt)); // EOPNOTSUPP

// Cause 3: Wrong address family
int sock = socket(AF_UNIX, SOCK_STREAM, 0);
// Trying to use with AF_INET operations
```

## How to Fix

### Fix 1: Check socket type support

```c
int sock = socket(AF_INET, SOCK_STREAM, 0); // standard TCP
if (sock == -1) {
    perror("socket");
}
```

### Fix 2: Use supported options

```c
// Check if option is supported before setting
int opt = 1;
int result = setsockopt(sock, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
if (result == -1 && errno == EOPNOTSUPP) {
    // Option not supported, continue without it
}
```

### Fix 3: Check platform support

```bash
# Check available socket options
man socket
man setsockopt
```

## Related Errors

- [Protocol error]({{< relref "/languages/c/protocol-error" >}}) — EPROTO.
- [Address already in use]({{< relref "/languages/c/address-already-in-use" >}}) — EADDRINUSE.
- [Not connected]({{< relref "/languages/c/not-connected" >}}) — ENOTCONN.
