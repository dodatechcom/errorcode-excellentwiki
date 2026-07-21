---
title: "[Solution] Ubuntu Server: netplan-wifi-network-error"
description: "Fix Ubuntu netplan-wifi-network-error. WiFi configuration in netplan fails to connect."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Netplan WiFi Network Error

WiFi configuration in netplan fails to connect or authenticate.

## Common Causes
- Incorrect SSID or password in netplan YAML
- WiFi adapter not detected
- wpa_supplicant not running
- Hidden SSID not handled properly

## How to Fix
1. Check WiFi adapter
```bash
iwconfig
nmcli device wifi list
```
2. Verify netplan WiFi syntax
```bash
sudo netplan generate
```
3. Connect manually to test
```bash
sudo iwlist wlan0 scan
nmcli device wifi connect "SSID" password "password"
```

## Examples
```bash
$ iwconfig
wlan0     IEEE 802.11  ESSID:off/any

$ sudo netplan generate
# Check for YAML errors
```
