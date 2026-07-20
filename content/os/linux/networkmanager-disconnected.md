---
title: "[Solution] Linux: networkmanager-disconnected — NetworkManager device disconnected"
description: "Fix Linux networkmanager-disconnected errors. NetworkManager device disconnected with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 8
---
# Linux: NetworkManager Disconnected

NetworkManager shows "disconnected" when the network management service cannot establish connectivity.

## Common Causes

- Wi-Fi disabled via hardware switch or rfkill
- Ethernet cable unplugged
- Airplane mode enabled
- NetworkManager dispatcher scripts blocking connectivity
- Interface managed by another network service

## How to Fix

### 1. Check RF Kill Status

```bash
rfkill list
sudo rfkill unblock all
```

### 2. Check Wi-Fi Radio Status

```bash
nmcli radio wifi
nmcli radio wifi on
```

### 3. Enable Networking

```bash
nmcli networking on
```

### 4. Rescan and Connect

```bash
nmcli device wifi rescan
nmcli device wifi list
nmcli device wifi connect <SSID> password <password>
```

### 5. Check Interface State

```bash
ip link set wlan0 up
```

## Examples

```bash
$ nmcli device status
DEVICE  TYPE      STATE        CONNECTION
eth0    ethernet  unavailable  --
wlan0   wifi      disconnected  --

$ rfkill list
0: phy0: Wireless LAN
        Soft blocked: yes
$ sudo rfkill unblock wifi
$ nmcli radio wifi
enabled
$ nmcli device wifi connect MyWifi password secret123
```
