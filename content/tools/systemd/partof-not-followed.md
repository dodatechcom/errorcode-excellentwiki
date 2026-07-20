---
title: "[Solution] systemd PartOf not followed"
description: "Fix systemd PartOf not followed. Resolve issues where PartOf= stop/restart is not propagated."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd PartOf not followed

## Error Description

When stopping parent.service, myapp.service was expected to be stopped but was not.

PartOf= was not correctly configured.

## Common Causes

Common Causes:
- PartOf= points to a non-existent unit
- The dependent unit was masked
- systemd did not propagate the stop signal

## How to Fix

How to Fix:
```bash
# Verify PartOf= target exists
systemctl list-unit-files | grep parent.service

# PartOf= only propagates stop and restart, not start
sudo systemctl edit myapp
```

```ini
[Unit]
PartOf=parent.service
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