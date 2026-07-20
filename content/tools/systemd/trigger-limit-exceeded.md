---
title: "[Solution] systemd socket trigger limit exceeded"
description: "Fix systemd socket trigger limit exceeded. Resolve socket activation rate limiting."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd socket trigger limit exceeded

## Error Description

myapp.socket: Trigger limit hit. Refusing to activate service.

The socket unit has been triggered too many times.

## Common Causes

Common Causes:
- Too many connections arriving in a short time
- Service is not starting fast enough to handle connections
- Rate limiting is too restrictive

## How to Fix

How to Fix:
```bash
# Check socket trigger limits
systemctl show myapp.socket | grep TriggerLimit

# Increase the trigger limit
sudo systemctl edit myapp.socket
```

```ini
[Socket]
TriggerLimitIntervalSec=60
TriggerLimitBurst=1000
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