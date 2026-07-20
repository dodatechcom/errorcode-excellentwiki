---
title: "[Solution] systemd DNS resolution failed"
description: "Fix systemd DNS resolution failed. Resolve DNS lookup failures with systemd-resolved."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd DNS resolution failed

## Error Description

myapp.service: DNS resolution failed: Name or service not known

The system cannot resolve domain names.

## Common Causes

Common Causes:
- systemd-resolved is not running
- DNS servers are not configured
- /etc/resolv.conf is missing or incorrect
- DNS over TLS configuration error

## How to Fix

How to Fix:
```bash
# Check resolved status
systemctl status systemd-resolved

# Check DNS configuration
resolvectl status

# Configure DNS
sudo tee /etc/systemd/resolved.conf <<'EOF'
[Resolve]
DNS=8.8.8.8 8.8.4.4
FallbackDNS=1.1.1.1
DNSOverTLS=opportunistic
EOF

sudo systemctl restart systemd-resolved

# Link resolv.conf
sudo ln -sf /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
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