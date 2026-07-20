---
title: "[Solution] systemd CapabilityBoundingSet too restrictive"
description: "Fix systemd CapabilityBoundingSet too restrictive. Resolve service failures when capabilities are stripped."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd CapabilityBoundingSet too restrictive

## Error Description

myapp.service: Operation not permitted. Missing capability: CAP_NET_BIND_SERVICE.

The service lacks the required Linux capability.

## Common Causes

Common Causes:
- CapabilityBoundingSet does not include needed capabilities
- Service needs to bind to privileged ports
- Service needs to change process priorities
- Too many capabilities were removed

## How to Fix

How to Fix:
```bash
# Add required capabilities
sudo systemctl edit myapp
```

```ini
[Service]
CapabilityBoundingSet=CAP_NET_BIND_SERVICE CAP_SYS_ADMIN
AmbientCapabilities=CAP_NET_BIND_SERVICE
```

## Examples

```bash
# Check systemd version
systemctl --version

# Verify unit file syntax
sudo systemd-analyze verify /etc/systemd/system/myapp.service

# Analyze system boot
systemd-analyze blame

# List failed units
systemctl --failed

# View service logs
journalctl -u myapp -n 50 --no-pager
```