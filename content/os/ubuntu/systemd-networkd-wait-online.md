---
title: "Systemd-networkd Wait Online Error"
description: "System hangs waiting for network connectivity during boot"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Systemd-networkd Wait Online Error

System hangs waiting for network connectivity during boot

## Common Causes

- Network interface not configured (DHCP or static)
- DNS server unreachable causing timeout
- systemd-networkd not managing the interface
- Wait online timeout exceeded

## How to Fix

1. Check timeout: `systemd-analyze time`
2. Reduce timeout: `NetworkInterfaceTimeout=5s` in networkd-wait-online.conf
3. Skip wait: `systemctl mask systemd-networkd-wait-online.service`
4. Check network: `networkctl status`

## Examples

```bash
# Check boot time analysis
systemd-analyze blame | head -10

# Check networkd wait-online status
systemctl status systemd-networkd-wait-online

# Reduce wait timeout
echo '[Service]\nTimeoutStartSec=10' | sudo tee /etc/systemd/system/systemd-networkd-wait-online.service.d/timeout.conf
```
