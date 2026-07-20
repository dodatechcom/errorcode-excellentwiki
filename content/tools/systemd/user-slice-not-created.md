---
title: "[Solution] systemd user slice not created"
description: "Fix systemd user slice not created. Resolve user resource management failures when slices are missing."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd user slice not created

## Error Description

user-1000.slice: Slice not created. Resource limits not applied.

The user slice was not created by systemd-logind.

## Common Causes

Common Causes:
- systemd-logind did not create the slice
- Slice configuration has errors
- Resource limits exceed system capabilities
- Missing kernel resource control support

## How to Fix

How to Fix:
```bash
# Check if slice exists
systemctl status user-1000.slice

# Create the slice manually
sudo tee /etc/systemd/system/user-1000.slice <<'EOF'
[Unit]
Description=User Slice for UID 1000

[Slice]
CPUQuota=100%
MemoryMax=4G
TasksMax=4096

[Install]
WantedBy=slices.target
EOF

sudo systemctl daemon-reload
sudo systemctl start user-1000.slice
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