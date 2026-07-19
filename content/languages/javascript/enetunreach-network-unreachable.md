---
title: "[Solution] ENETUNREACH — Network Unreachable Error"
description: "Fix ENETUNREACH when Node.js cannot reach a network destination. Check routing, firewalls, and VPN connectivity."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ENETUNREACH — Network Unreachable

The network destination is unreachable.

## Diagnose

```bash
ip route show
ping -c 1 <destination>
traceroute <destination>
```

## Common Causes

- VPN not connected
- Firewall blocking outbound
- Missing default route
