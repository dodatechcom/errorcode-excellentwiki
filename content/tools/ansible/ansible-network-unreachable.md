---
title: "[Solution] Ansible Network Unreachable Error"
description: "Fix Ansible network unreachable errors when target hosts are not accessible"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot reach the target host due to network-level issues.

```
UNREACHABLE! => "ssh: connect to host 10.0.50.10 port 22: Network is unreachable"
```

## Common Causes

- No route to target network
- VPN not connected
- Network interface down
- Routing table misconfigured
- Gateway unreachable

## How to Fix

```yaml
# Use jump host
[proxy]
bastion ansible_host=203.0.113.50

[targets]
target1 ansible_host=10.0.50.10 ansible_ssh_common_args='-o ProxyJump=admin@203.0.113.50'
```

```bash
ping -c 3 10.0.50.10
ip route show
```
