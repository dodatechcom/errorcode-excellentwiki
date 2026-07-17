---
title: "[Solution] C Cannot assign requested address: EADDRNOTAVAIL"
description: "Fix C cannot assign requested address (EADDRNOTAVAIL). Use available network interfaces."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Cannot assign requested address: EADDRNOTAVAIL

EADDRNOTAVAIL occurs when you try to bind or connect to an IP address that is not available on the local system. The interface may be down or the address may not be configured.

## Common Causes

```c
// Cause 1: Binding to unavailable address
struct sockaddr_in addr;
addr.sin_addr.s_addr = inet_addr("10.0.0.100"); // not on this machine
bind(sock, (struct sockaddr*)&addr, sizeof(addr)); // EADDRNOTAVAIL

// Cause 2: Interface is down
// eth0 is down but trying to bind to its IP

// Cause 3: IPv6 not configured
// Trying to bind to ::1 without IPv6
```

## How to Fix

### Fix 1: Use INADDR_ANY

```c
addr.sin_addr.s_addr = INADDR_ANY; // bind to all interfaces
bind(sock, (struct sockaddr*)&addr, sizeof(addr));
```

### Fix 2: Check available addresses

```bash
ip addr show
# or
ifconfig
```

### Fix 3: Bring up interface

```bash
ip link set eth0 up
```

## Related Errors

- [Address already in use]({{< relref "/languages/c/address-already-in-use" >}}) — EADDRINUSE.
- [Network unreachable]({{< relref "/languages/c/network-unreachable" >}}) — ENETUNREACH.
- [Connection refused]({{< relref "/languages/c/connection-refused-c" >}}) — ECONNREFUSED.
