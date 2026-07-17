---
title: "[Solution] Linux ERFKILL (errno 89) — Operation Not Possible Due to RF-Kill Fix"
description: "Fix Linux ERFKILL (errno 89) Operation not possible due to RF-kill error. Solutions for RF-kill and wireless device issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux ERFKILL (errno 89) — Operation Not Possible Due to RF-Kill

ERFKILL (errno 89) means the operation is not possible because RF-kill is active. This error occurs when a wireless device is blocked by the RF-kill switch (hardware or software), preventing the system from using wireless interfaces. It is distinct from ENODEV (errno 19) because ERFKILL specifically indicates RF-kill blocking, not device absence.

## Common Causes

- Hardware wireless switch is turned off
- Software RF-kill is enabled via rfkill or NetworkManager
- BIOS/UEFI has disabled wireless
- Fn key combination disabled wireless radio

## How to Fix ERFKILL

### 1. Check RF-Kill Status

View the current RF-kill state:

```bash
rfkill list all
```

### 2. Unblock Software RF-Kill

Enable wireless via software:

```bash
sudo rfkill unblock all
sudo rfkill unblock wifi
sudo rfkill unblock bluetooth
```

### 3. Check Hardware Switch

Ensure the physical wireless switch is enabled:

- Look for a wireless switch on the laptop chassis
- Check for Fn+F5 or similar key combination
- Check BIOS/UEFI settings for wireless option

### 4. Check Kernel Messages

Look for RF-kill related kernel messages:

```bash
dmesg | grep -i "rfkill\|wireless\|wifi"
```

### 5. Reset Network Interface

After unblocking, bring the interface up:

```bash
sudo ip link set wlan0 up
sudo systemctl restart NetworkManager
```

## Verification

After unblocking RF-kill, confirm wireless is active:

```bash
rfkill list all
iwconfig
ip link show wlan0
```

## Related Error Codes

- [ENODEV (errno 19)](/os/linux/errno-19/) — No such device
- [ENONET (errno 49)](/os/linux/errno-49/) — Machine is not on the network
- [ENETDOWN (errno 64)](/os/linux/errno-64/) — Network is down
