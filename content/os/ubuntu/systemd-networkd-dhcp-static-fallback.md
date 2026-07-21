---
title: "Systemd-networkd DHCP with Static Fallback Error"
description: "Static fallback IP configured but DHCP still taking precedence"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Systemd-networkd DHCP with Static Fallback Error

Static fallback IP configured but DHCP still taking precedence

## Common Causes

- FallbackStatic options not properly configured
- DHCP always succeeds even on wrong network
- Network matching not restricting DHCP to specific interfaces
- Route metrics not set to prefer static over DHCP

## How to Fix

1. Check network config: `cat /etc/systemd/network/*.network`
2. Set DHCP route metric: `DHCPRouteMetric=100`
3. Set static route metric lower: `RouteMetric=50`
4. Use [RoutingPolicyRule] for conditional routing

## Examples

```bash
# Check network configuration files
ls -la /etc/systemd/network/

# View network status
networkctl status
```
