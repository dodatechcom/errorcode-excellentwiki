---
title: "[Solution] systemd WantedBy not found"
description: "Fix systemd WantedBy not found errors. Resolve service enable failures when the WantedBy target does not exist."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd WantedBy not found

## Error Description

Failed to enable myapp.service: Unit file WantedBy target not found.

The target specified in WantedBy= does not exist.

## Common Causes

Common Causes:
- Target name typo in WantedBy=
- Required target package not installed
- Custom target not created

## How to Fix

How to Fix:
```bash
# List available targets
systemctl list-unit-files --type=target

# Common targets: multi-user.target, graphical.target, network-online.target

# Edit the unit file
sudo systemctl edit myapp --force
```

```ini
[Install]
WantedBy=multi-user.target
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