---
title: "[Solution] systemd default target not set"
description: "Fix systemd default target not set. Resolve boot issues when the system does not know which target to reach."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd default target not set

## Error Description

No default target set. System cannot determine boot target.

The default.target symlink is missing or broken.

## Common Causes

Common Causes:
- /etc/systemd/system/default.target symlink is missing
- Symlink points to a non-existent target
- System was installed without a default target

## How to Fix

How to Fix:
```bash
# Check current default target
systemctl get-default

# Set the default target
sudo systemctl set-default multi-user.target
# or for graphical desktop:
sudo systemctl set-default graphical.target

# Verify the symlink
ls -la /etc/systemd/system/default.target
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