---
title: "[Solution] C No route to host: EHOSTUNREACH"
description: "Fix C no route to host (EHOSTUNREACH). Check routing tables and network configuration."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["ehostunreach", "no-route-to-host", "routing", "network", "errno"]
weight: 5
---

# No route to host: EHOSTUNREACH

EHOSTUNREACH occurs when a route to the destination host cannot be found. This is different from ENETUNREACH which means no route to the network.

## Common Causes

```c
// Cause 1: Host is unreachable
connect(sock, (struct sockaddr*)&addr, sizeof(addr)); // EHOSTUNREACH

// Cause 2: Wrong subnet
// Host is on different subnet without gateway

// Cause 3: Host is down
// Target machine powered off
```

## How to Fix

### Fix 1: Check routing table

```bash
ip route show
# or
route -n
```

### Fix 2: Add route

```bash
ip route add 10.0.0.0/24 via 192.168.1.1
```

### Fix 3: Verify host is up

```bash
ping target_host
arping target_host
```

## Related Errors

- [Network unreachable]({{< relref "/languages/c/network-unreachable" >}}) — ENETUNREACH.
- [Connection refused]({{< relref "/languages/c/connection-refused-c" >}}) — ECONNREFUSED.
- [Connection timed out]({{< relref "/languages/c/operation-timed-out" >}}) — ETIMEDOUT.
