---
title: "[Solution] C Connection refused: ECONNREFUSED"
description: "Fix C connection refused (ECONNREFUSED). Ensure server is listening before connecting."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Connection refused: ECONNREFUSED

ECONNREFUSED occurs when a connection attempt is actively rejected by the server. No process is listening on the target port, or a firewall is blocking the connection.

## Common Causes

```c
// Cause 1: Server not running
int sock = socket(AF_INET, SOCK_STREAM, 0);
struct sockaddr_in addr = {
    .sin_family = AF_INET,
    .sin_port = htons(8080),
    .sin_addr.s_addr = inet_addr("127.0.0.1")
};
connect(sock, (struct sockaddr*)&addr, sizeof(addr)); // ECONNREFUSED

// Cause 2: Wrong port
// Server on 3000, client connects to 8080

// Cause 3: Firewall blocking
// iptables blocking incoming connections
```

## How to Fix

### Fix 1: Verify server is running

```bash
ss -tlnp | grep 8080
# or
netstat -tlnp | grep 8080
```

### Fix 2: Check port is correct

```c
// Match server's listening port
.sin_port = htons(3000); // correct port
```

### Fix 3: Retry with backoff

```c
for (int i = 0; i < 5; i++) {
    if (connect(sock, (struct sockaddr*)&addr, sizeof(addr)) == 0) {
        break;
    }
    sleep(1 << i); // exponential backoff
}
```

## Related Errors

- [Network unreachable]({{< relref "/languages/c/network-unreachable" >}}) — ENETUNREACH.
- [Connection timed out]({{< relref "/languages/c/operation-timed-out" >}}) — ETIMEDOUT.
- [Connection reset]({{< relref "/languages/c/connection-reset" >}}) — ECONNRESET.
