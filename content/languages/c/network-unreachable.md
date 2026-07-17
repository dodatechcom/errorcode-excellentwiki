---
title: "[Solution] C Network is unreachable: ENETUNREACH"
description: "Fix C network unreachable (ENETUNREACH). Check network configuration and routing."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["enetunreach", "network-unreachable", "routing", "socket", "errno"]
weight: 5
---

# Network is unreachable: ENETUNREACH

ENETUNREACH occurs when a network operation cannot reach the target network. This usually means no route exists to the destination, or the network interface is down.

## Common Causes

```c
// Cause 1: No route to destination
connect(sock, (struct sockaddr*)&addr, sizeof(addr)); // ENETUNREACH

// Cause 2: Network interface down
// WiFi disconnected or ethernet unplugged

// Cause 3: IPv6 not configured
// Trying to connect via IPv6 without IPv6 support
```

## How to Fix

### Fix 1: Check network connectivity

```bash
ip route show
# or
route -n
```

### Fix 2: Check interface status

```bash
ip link show
# or
ifconfig
```

### Fix 3: Add route

```bash
ip route add 10.0.0.0/8 via 192.168.1.1
```

## Related Errors

- [Host unreachable]({{< relref "/languages/c/host-unreachable" >}}) — EHOSTUNREACH.
- [Connection refused]({{< relref "/languages/c/connection-refused-c" >}}) — ECONNREFUSED.
- [Connection timed out]({{< relref "/languages/c/operation-timed-out" >}}) — ETIMEDOUT.
