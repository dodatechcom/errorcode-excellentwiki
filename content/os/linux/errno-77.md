---
title: "[Solution] Linux EHOSTUNREACH (errno 77) — No Route to Host Fix"
description: "Fix Linux EHOSTUNREACH (errno 77) No route to host error. Solutions for routing and host reachability issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["ehostunreach", "host", "errno-77", "routing", "unreachable"]
weight: 5
---

# Linux EHOSTUNREACH (errno 77) — No Route to Host

EHOSTUNREACH (errno 77) means there is no route to the target host. This error occurs when the system cannot determine how to reach a specific remote host, even though the network itself is up. It is distinct from ENETUNREACH (errno 65) because EHOSTUNREACH refers to a specific host, while ENETUNREACH refers to an entire network.

## Common Causes

- No route exists to the destination host
- Gateway does not know how to reach the host
- Host is on a different network with no routing path
- Static route is missing or misconfigured

## How to Fix EHOSTUNREACH

### 1. Check Routing Table

Verify routes to the destination:

```bash
ip route show
route -n | grep destination_ip
```

### 2. Add a Route

If no route exists, add one:

```bash
sudo ip route add destination_ip via gateway_ip
```

### 3. Check Default Gateway

Ensure a default gateway is configured:

```bash
ip route show | grep default
```

### 4. Verify Gateway Reachability

Test if the gateway is reachable:

```bash
ping gateway_ip
```

### 5. Use traceroute to Find the Break

Identify where routing fails:

```bash
traceroute host.example.com
mtr host.example.com
```

## Verification

After adding the route, confirm the host is reachable:

```bash
ping host.example.com
ip route get destination_ip
```

## Related Error Codes

- [ENETUNREACH (errno 65)](/os/linux/errno-65/) — Network is unreachable
- [EHOSTDOWN (errno 76)](/os/linux/errno-76/) — Host is down
- [ETIMEDOUT (errno 74)](/os/linux/errno-74/) — Connection timed out
