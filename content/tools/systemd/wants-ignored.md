---
title: "[Solution] systemd Wants ignored"
description: "Fix systemd Wants ignored. Resolve situations where Wants= dependencies are silently skipped."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd Wants ignored

## Error Description

myapp.service: Wants=optional-service.service ignored.

The Wants= dependency was not started because the unit does not exist.

## Common Causes

Common Causes:
- The wanted unit does not exist on the system
- The unit file for the dependency is not installed
- Silent failure is expected behavior for Wants=

## How to Fix

How to Fix:
```bash
# Wants= is optional by design - no error if missing
# To make it required, use Requires= instead

# Check if the wanted unit exists
systemctl list-unit-files | grep optional-service

# To install it
sudo apt install <package-providing-the-unit>
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