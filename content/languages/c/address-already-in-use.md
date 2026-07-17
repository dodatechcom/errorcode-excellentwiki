---
title: "[Solution] C Address already in use: EADDRINUSE"
description: "Fix C address already in use (EADDRINUSE). Use SO_REUSEADDR or wait for TIME_WAIT to expire."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Address already in use: EADDRINUSE

EADDRINUSE occurs when you try to bind a socket to an address and port that is already in use by another socket, including one in TIME_WAIT state.

## Common Causes

```c
// Cause 1: Port already bound
int sock = socket(AF_INET, SOCK_STREAM, 0);
bind(sock, (struct sockaddr*)&addr, sizeof(addr)); // EADDRINUSE

// Cause 2: Previous server still in TIME_WAIT
// Server was restarted but old socket is in TIME_WAIT

// Cause 3: Another process using same port
// Another server is already listening on that port
```

## How to Fix

### Fix 1: Use SO_REUSEADDR

```c
int opt = 1;
setsockopt(sock, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
bind(sock, (struct sockaddr*)&addr, sizeof(addr));
```

### Fix 2: Wait for TIME_WAIT

```bash
# Check TIME_WAIT connections
ss -tan state time-wait | grep 8080
```

### Fix 3: Use different port

```c
sin_port = htons(8081); // try different port
```

## Examples

```c
#include <sys/socket.h>

int sock = socket(AF_INET, SOCK_STREAM, 0);
int opt = 1;
setsockopt(sock, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

struct sockaddr_in addr = {
    .sin_family = AF_INET,
    .sin_port = htons(8080),
    .sin_addr.s_addr = INADDR_ANY
};

if (bind(sock, (struct sockaddr*)&addr, sizeof(addr)) == -1) {
    perror("bind");
}
```

## Related Errors

- [Connection refused]({{< relref "/languages/c/connection-refused-c" >}}) — ECONNREFUSED.
- [Address already in use]({{< relref "/languages/c/address-already-in-use" >}}) — detailed analysis.
- [Network unreachable]({{< relref "/languages/c/network-unreachable" >}}) — ENETUNREACH.
