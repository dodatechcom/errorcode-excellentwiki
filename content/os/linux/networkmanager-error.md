---
title: "[Solution] Linux: networkmanager-error — NetworkManager error"
description: "Fix Linux networkmanager-error errors. NetworkManager error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 8
---
# Linux: NetworkManager Error

NetworkManager errors occur when the network management service fails to connect to networks or manage interfaces.

## Common Causes

- NetworkManager service not running
- NetworkManager conflicts with systemd-networkd or ifupdown
- Connection profile corrupted or missing
- ModemManager interfering with mobile broadband
- VPN plugin not installed or incompatible

## How to Fix

### 1. Check NetworkManager Status

```bash
sudo systemctl status NetworkManager
nmcli general status
```

### 2. Restart NetworkManager

```bash
sudo systemctl restart NetworkManager
```

### 3. Manage Connections

```bash
# List connections
nmcli connection show
# List devices
nmcli device status
# Connect to a network
nmcli device wifi connect <SSID> password <password>
```

### 4. Check Logs

```bash
journalctl -u NetworkManager -n 50 --no-pager
```

### 5. Remove and Recreate Connection

```bash
nmcli connection delete <connection-name>
nmcli device wifi connect <SSID> password <password>
```

## Examples

```bash
$ nmcli device status
DEVICE  TYPE      STATE      CONNECTION
eth0    ethernet  connected  Wired connection 1
wlan0   wifi      disconnected  --

$ sudo systemctl restart NetworkManager
$ nmcli device wifi connect MyWifi password secret123
Device 'wlan0' successfully activated with 'MyWifi'
```
