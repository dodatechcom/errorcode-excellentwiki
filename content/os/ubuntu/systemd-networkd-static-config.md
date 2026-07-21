---
title: "Systemd-networkd Static IP Configuration Error"
description: "Static IP configuration in systemd-networkd .network file not working"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Systemd-networkd Static IP Configuration Error

Static IP configuration in systemd-networkd .network file not working

## Common Causes

- Syntax error in .network file
- Address/CIDR notation incorrect
- Gateway not on same subnet
- DNS configuration missing

## How to Fix

1. Check config: `networkctl status`
2. Verify file in `/etc/systemd/network/`
3. Test with `networkctl reconfigure <interface>`
4. Check logs: `journalctl -u systemd-networkd`

## Examples

```bash
# Example static configuration
cat <<'EOF' | sudo tee /etc/systemd/network/10-static.network
[Match]
Name=eth0

[Network]
Address=192.168.1.100/24
Gateway=192.168.1.1
DNS=8.8.8.8
DNS=8.8.4.4
EOF

# Restart networkd
sudo systemctl restart systemd-networkd
```
