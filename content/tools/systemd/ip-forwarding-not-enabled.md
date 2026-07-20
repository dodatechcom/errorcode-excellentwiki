---
title: "[Solution] systemd IP forwarding not enabled"
description: "Fix systemd IP forwarding not enabled. Resolve routing issues when IP forwarding is disabled."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd IP forwarding not enabled

## Error Description

IP forwarding is not enabled. Routing between interfaces will not work.

The kernel IP forwarding is disabled.

## Common Causes

Common Causes:
- net.ipv4.ip_forward is set to 0
- systemd-networkd did not enable forwarding
- Firewall rules blocking forwarded traffic

## How to Fix

How to Fix:
```bash
# Enable IP forwarding
echo "net.ipv4.ip_forward = 1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p

# Or enable in network config
sudo tee /etc/systemd/network/forwarding.network <<'EOF'
[Match]
Name=*

[Network]
IPForward=yes
EOF

sudo systemctl restart systemd-networkd
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