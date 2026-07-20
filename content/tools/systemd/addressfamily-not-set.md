---
title: "[Solution] systemd AddressFamily not set"
description: "Fix systemd AddressFamily not set. Resolve network configuration issues with missing address family specification."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd AddressFamily not set

## Error Description

eth0.network: AddressFamily= not set. Defaults to inet+inet6.

AddressFamily was not explicitly specified in network configuration.

## Common Causes

Common Causes:
- AddressFamily= is not specified in .network file
- Service expects IPv4 only but IPv6 is being used
- Dual-stack issues causing unexpected behavior

## How to Fix

How to Fix:
```bash
# Specify AddressFamily in network config
sudo tee /etc/systemd/network/10-eth0.network <<'EOF'
[Match]
Name=eth0

[Network]
AddressFamily=inet
DHCP=yes
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