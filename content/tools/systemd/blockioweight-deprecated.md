---
title: "[Solution] systemd BlockIOWeight deprecated"
description: "Fix systemd BlockIOWeight deprecated. Resolve deprecation warnings for legacy IO control directives."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd BlockIOWeight deprecated

## Error Description

myapp.service: BlockIOWeight= is deprecated. Use IOWeight= instead.

The BlockIOWeight= directive is no longer supported.

## Common Causes

Common Causes:
- Using legacy cgroup v1 BlockIO directives on a cgroup v2 system
- Unit file was written for an older systemd version
- Deprecated directive not updated

## How to Fix

How to Fix:
```bash
# Replace deprecated directives
# BlockIOWeight= → IOWeight=
# BlockIOReadBandwidthMax= → IOReadBandwidthMax=
# BlockIOWriteBandwidthMax= → IOWriteBandwidthMax=

sudo systemctl edit myapp
```

```ini
[Service]
IOWeight=500
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