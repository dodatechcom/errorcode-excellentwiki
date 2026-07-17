---
title: "[Solution] C Connection timed out: ETIMEDOUT"
description: "Fix C connection timed out (ETIMEDOUT). Set appropriate socket timeouts and handle network delays."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["etimedout", "connection-timed-out", "socket", "timeout", "errno"]
weight: 5
---

# Connection timed out: ETIMEDOUT

ETIMEDOUT occurs when a connection attempt takes too long. This typically means the host is unreachable or the network is congested, and the kernel gives up after the timeout period.

## Common Causes

```c
// Cause 1: Host too slow to respond
connect(sock, (struct sockaddr*)&addr, sizeof(addr)); // ETIMEDOUT

// Cause 2: Network congestion
// Packets being dropped due to congestion

// Cause 3: Firewall silently dropping packets
// No response at all (unlike ECONNREFUSED)
```

## How to Fix

### Fix 1: Set connect timeout

```c
struct timeval tv;
tv.tv_sec = 5;
tv.tv_usec = 0;
setsockopt(sock, SOL_SOCKET, SO_SNDTIMEO, &tv, sizeof(tv));
connect(sock, (struct sockaddr*)&addr, sizeof(addr));
```

### Fix 2: Use non-blocking connect

```c
fcntl(sock, F_SETFL, O_NONBLOCK);
connect(sock, (struct sockaddr*)&addr, sizeof(addr));
// select() or poll() with timeout
```

### Fix 3: Check network connectivity

```bash
ping -c 3 target_host
traceroute target_host
```

## Related Errors

- [Connection refused]({{< relref "/languages/c/connection-refused-c" >}}) — ECONNREFUSED.
- [Network unreachable]({{< relref "/languages/c/network-unreachable" >}}) — ENETUNREACH.
- [Host unreachable]({{< relref "/languages/c/host-unreachable" >}}) — EHOSTUNREACH.
