---
title: "[Solution] Linux wpa_supplicant Authentication Failed — Wi-Fi Fix"
description: "Fix Linux Wi-Fi 'wpa_supplicant: authentication failed' errors. Resolve WPA/WPA2 authentication issues, wrong passwords, and driver problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: wpa_supplicant: authentication failed

The `wpa_supplicant: authentication failed` error means the Wi-Fi client could not authenticate with the access point. This can happen due to incorrect credentials, security protocol mismatches, or driver issues.

## Common Causes

- Incorrect Wi-Fi password (PSK)
- Security protocol mismatch (WPA2 vs WPA3)
- Hidden SSID with incorrect configuration
- 802.1x / Enterprise Wi-Fi configuration errors
- Regulatory domain restrictions (channels not allowed)
- Wi-Fi driver or firmware issues
- Too many connected clients (AP full)

## How to Fix

### 1. Verify the Wi-Fi Password

```bash
# Check the stored password
sudo grep -A2 psk /etc/NetworkManager/system-connections/<SSID>.nmconnection

# Ensure the password is correct (8-63 characters for WPA2-PSK)
# Try reconnecting with the correct password
nmcli dev wifi connect "SSID" password "correct-password"
```

### 2. Check Security Protocol

```bash
# Check what security the AP uses
nmcli dev wifi list | grep "SSID"

# Force WPA2 if the AP doesn't support WPA3
nmcli con modify "SSID" 802-11-wireless-security.key-mgmt wpa-psk
nmcli con up "SSID"
```

### 3. Connect to Hidden SSID

```bash
# Add connection with hidden SSID
nmcli con add type wifi con-name "HiddenNet" ssid "HiddenSSID"
nmcli con modify "HiddenNet" 802-11-wireless.hidden yes
nmcli con modify "HiddenNet" wifi-sec.key-mgmt wpa-psk
nmcli con modify "HiddenNet" wifi-sec.psk "password"
nmcli con up "HiddenNet"
```

### 4. Fix 802.1x Enterprise Authentication

```bash
# Configure enterprise Wi-Fi
nmcli con add type wifi con-name "Enterprise" ssid "EnterpriseSSID"
nmcli con modify "Enterprise" 802-11-wireless-security.key-mgmt wpa-eap
nmcli con modify "Enterprise" 802-11-wireless-security.eap peap
nmcli con modify "Enterprise" 802-11-wireless-security.identity "username"
nmcli con modify "Enterprise" 802-11-wireless-security.password "password"
nmcli con up "Enterprise"
```

### 5. Set Regulatory Domain

```bash
# Check current regulatory domain
iw reg get

# Set correct country
sudo iw reg set US   # Replace with your country code
```

### 6. Restart wpa_supplicant

```bash
# Check wpa_supplicant status
sudo systemctl status wpa_supplicant

# Restart
sudo systemctl restart wpa_supplicant

# Or use NetworkManager restart
sudo systemctl restart NetworkManager
```

### 7. Check Wi-Fi Hardware and Drivers

```bash
# Check Wi-Fi device
lspci -k | grep -i network
lsusb | grep -i wireless

# Check driver
lsmod | grep -E 'iwl|ath|rtl|b43'

# Check firmware
dmesg | grep -i firmware
```

## Examples

```bash
$ nmcli dev wifi connect "CorpWiFi" password "wrongpass"
Error: Connection activation failed: (7) Secrets were required, but not provided

$ nmcli dev wifi connect "CorpWiFi" password "correctpass"
Device 'wlan0' successfully activated with 'CorpWiFi'
```

```bash
# Enterprise Wi-Fi failure
$ nmcli dev wifi list
SSID          SECURITY
Enterprise    WPA2 802.1X

$ nmcli con add type wifi con-name "Enterprise" ssid "Enterprise"
$ nmcli con modify "Enterprise" 802-11-wireless-security.key-mgmt wpa-eap
$ nmcli con modify "Enterprise" 802-11-wireless-security.eap peap
$ nmcli con modify "Enterprise" 802-11-wireless-security.identity "user@domain.com"
$ nmcli con modify "Enterprise" 802-11-wireless-security.password "mypassword"
$ nmcli con up "Enterprise"
Connection successfully activated
```

## Related Errors

- [NetworkManager error]({{< relref "/os/linux/linux-network-manager" >}}) — Network management issues
- [ip/RTNETLINK errors]({{< relref "/os/linux/linux-ip-error" >}}) — Interface configuration issues
- [DNS errors]({{< relref "/os/linux/linux-resolv-conf-error" >}}) — DNS resolution failures
