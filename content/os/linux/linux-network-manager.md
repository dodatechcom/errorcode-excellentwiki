---
title: "[Solution] Linux NetworkManager Connection Failed — Fix"
description: "Fix Linux NetworkManager connection failures. Resolve network connectivity, Wi-Fi, and VPN issues with NetworkManager."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: NetworkManager: connection failed

NetworkManager connection failures prevent network connectivity. These errors can appear in the GUI as "Connection failed" or in command-line tools like `nmcli`.

## Common Causes

- Wi-Fi driver or firmware issues
- Incorrect network credentials (Wi-Fi password, VPN key)
- Network interface disabled or not detected
- DHCP server not responding
- IP address conflict
- DNS configuration issues
- VPN configuration errors

## How to Fix

### 1. Check NetworkManager Status

```bash
# Check if NetworkManager is running
sudo systemctl status NetworkManager

# Restart if needed
sudo systemctl restart NetworkManager

# Check overall status
nmcli general status
```

### 2. List Available Networks

```bash
# List Wi-Fi networks
nmcli dev wifi list

# List all connections
nmcli con show

# List devices
nmcli dev status
```

### 3. Connect to a Wi-Fi Network

```bash
# Connect to a Wi-Fi network
nmcli dev wifi connect "SSID" password "password"

# Connect to a hidden network
nmcli con add type wifi con-name "MyNetwork" ssid "SSID"
nmcli con modify "MyNetwork" wifi-sec.key-mgmt wpa-psk wifi-sec.psk "password"
nmcli con up "MyNetwork"
```

### 4. Fix DHCP Issues

```bash
# Release and renew DHCP lease
sudo dhclient -r
sudo dhclient

# Or using nmcli
nmcli con down "Connection Name"
nmcli con up "Connection Name"
```

### 5. Reset Network Interfaces

```bash
# Bring the interface down and up
sudo nmcli device disconnect eth0
sudo nmcli device connect eth0

# Or using ip
sudo ip link set eth0 down
sudo ip link set eth0 up
```

### 6. Check IP Configuration

```bash
# View IP address
ip addr show

# Check DHCP lease
nmcli con show "Connection Name" | grep ipv4

# Set static IP
nmcli con mod "Connection Name" ipv4.addresses 192.168.1.100/24
nmcli con mod "Connection Name" ipv4.gateway 192.168.1.1
nmcli con mod "Connection Name" ipv4.dns "8.8.8.8"
nmcli con mod "Connection Name" ipv4.method manual
nmcli con up "Connection Name"
```

### 7. Fix VPN Connections

```bash
# Check VPN connection status
nmcli con show --active | grep vpn

# Restart VPN
nmcli con down "VPN Connection"
nmcli con up "VPN Connection"
```

### 8. Delete and Recreate Connection

```bash
# Remove the problematic connection
nmcli con delete "Connection Name"

# Scan and reconnect
nmcli dev wifi rescan
nmcli dev wifi connect "SSID" password "password"
```

## Examples

```bash
$ nmcli dev status
DEVICE  TYPE      STATE         CONNECTION
eth0    ethernet  disconnected  --
wlan0   wifi      disconnected  --

$ nmcli dev wifi list
IN-USE  SSID          MODE   CHAN  RATE        SIGNAL  SECURITY
        MyNetwork     Infra  6     130 Mbit/s  75      WPA2

$ nmcli dev wifi connect "MyNetwork" password "securepassword"
Device 'wlan0' successfully activated with 'MyNetwork'

$ nmcli dev status
DEVICE  TYPE      STATE         CONNECTION
wlan0   wifi      connected     MyNetwork
```

## Related Errors

- [Wi-Fi authentication failed]({{< relref "/os/linux/linux-wifi-error" >}}) — WPA/WPA2 authentication issues
- [DNS errors]({{< relref "/os/linux/linux-resolv-conf-error" >}}) — Name resolution problems
- [DHCP/ip errors]({{< relref "/os/linux/linux-ip-error" >}}) — IP configuration issues
