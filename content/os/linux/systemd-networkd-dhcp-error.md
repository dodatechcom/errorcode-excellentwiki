---
title: "[Solution] Linux: systemd-networkd-dhcp-error -- DHCP lease failure"
description: "Fix Linux systemd-networkd DHCP errors. DHCP lease acquisition failure in systemd-networkd."
os: ["linux"]
error-types: ["systemd-error"]
severities: ["error"]
---

# Linux: Systemd-Networkd DHCP Error

Systemd-networkd DHCP errors occur when the daemon fails to obtain or maintain a DHCP lease.

## Common Causes

- DHCP server unreachable or not responding
- Network interface not managed by systemd-networkd
- Invalid .network file configuration
- Firewall blocking DHCP packets
- Conflicting NetworkManager configuration

## How to Fix

### 1. Check Network Status

```bash
networkctl status
systemctl status systemd-networkd
journalctl -u systemd-networkd -n 30
```

### 2. Review Network Files

```bash
ls /etc/systemd/network/
cat /etc/systemd/network/*.network
```

### 3. Force DHCP Renewal

```bash
networkctl renew <interface>
sudo systemctl restart systemd-networkd
sudo networkctl reconfigure <interface>
```

## Examples

```bash
$ networkctl status
● 2: eth0
     State: configuring
     Type: ether
DHCPv4: error (ip)
$ networkctl renew eth0
Requesting DHCP lease
```
