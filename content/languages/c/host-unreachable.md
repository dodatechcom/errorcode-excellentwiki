---
title: "[Solution] C No route to host: EHOSTUNREACH"
description: "Fix C no route to host (EHOSTUNREACH). Fix routing and DNS resolution issues."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["ehostunreach", "no-route-to-host", "routing", "dns", "errno"]
weight: 5
---

# No route to host: EHOSTUNREACH

EHOSTUNREACH occurs when a specific host cannot be reached. Unlike ENETUNREACH (no route to network), this means a route exists but the host itself is unreachable.

## Common Causes

```c
// Cause 1: Host is down
connect(sock, (struct sockaddr*)&addr, sizeof(addr)); // EHOSTUNREACH

// Cause 2: Firewall blocking (ICMP reject)
// iptables rule rejecting packets to host

// Cause 3: Wrong IP address
// DNS resolved to wrong IP
```

## How to Fix

### Fix 1: Verify host is reachable

```bash
ping target_host
traceroute target_host
```

### Fix 2: Check firewall rules

```bash
iptables -L -n | grep DROP
# or
nft list ruleset
```

### Fix 3: Check DNS resolution

```bash
nslookup target_host
dig target_host
```

## Related Errors

- [Network unreachable]({{< relref "/languages/c/network-unreachable" >}}) — ENETUNREACH.
- [Connection refused]({{< relref "/languages/c/connection-refused-c" >}}) — ECONNREFUSED.
- [Connection timed out]({{< relref "/languages/c/operation-timed-out" >}}) — ETIMEDOUT.
