---
title: "[Solution] Linux bluetoothd Pairing Failed — Fix"
description: "Fix Linux Bluetooth 'bluetoothd: pairing failed' errors. Resolve Bluetooth device pairing, connection, and driver issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: bluetoothd: pairing failed

The `bluetoothd: pairing failed` error means the Bluetooth daemon could not complete pairing with a device. This can be caused by authentication failures, protocol mismatches, or hardware issues.

## Common Causes

- Incorrect pairing PIN or passkey
- Device not in discoverable/pairing mode
- Bluetooth adapter power management issues
- Bluetooth service not running
- Outdated Bluetooth firmware
- Device already connected to another host
- Bluetooth version incompatibility (BR/EDR vs BLE)
- BlueZ configuration issues

## How to Fix

### 1. Check Bluetooth Service

```bash
# Check Bluetooth service status
sudo systemctl status bluetooth

# Restart Bluetooth
sudo systemctl restart bluetooth

# Check Bluetooth adapter
hciconfig
bluetoothctl show
```

### 2. Use bluetoothctl for Pairing

```bash
# Enter the Bluetooth control shell
bluetoothctl

# Remove the device first if it was previously paired
remove <MAC-address>

# Scan for devices
scan on

# Pair with the device
pair <MAC-address>

# Trust and connect
trust <MAC-address>
connect <MAC-address>
```

### 3. Fix Power Management Issues

```bash
# Check if Bluetooth is blocked
rfkill list

# Unblock Bluetooth
rfkill unblock bluetooth

# Disable USB autosuspend (if using USB Bluetooth)
echo 'options usbcore autosuspend=-1' | sudo tee /etc/modprobe.d/usb-autosuspend.conf
```

### 4. Reset Bluetooth Adapter

```bash
# Reset the adapter
sudo hciconfig hci0 down
sudo hciconfig hci0 up

# Or using bluetoothctl
bluetoothctl power off
bluetoothctl power on
```

### 5. Fix PIN/Passkey Issues

```bash
# For devices that require a PIN
bluetoothctl
agent KeyboardOnly
default-agent
scan on
pair <MAC-address>
# Enter the PIN when prompted
```

### 6. Clear Bluetooth Cache

```bash
# Remove stored pairing information
rm -rf /var/lib/bluetooth/*

# Restart Bluetooth
sudo systemctl restart bluetooth

# Pair devices again from scratch
```

### 7. Update Bluetooth Firmware

```bash
# Check Bluetooth hardware
hciconfig -a

# Install firmware packages
sudo apt install firmware-brcm80211 firmware-iwlwifi  # Debian/Ubuntu
sudo dnf install linux-firmware                        # Fedora/RHEL
```

### 8. Check for Conflicting Services

```bash
# Check if pulseaudio-module-bluetooth is loaded for audio devices
pactl list modules short | grep bluetooth

# Install if missing
sudo apt install pulseaudio-module-bluetooth
```

## Examples

```bash
$ bluetoothctl
[bluetooth]# scan on
Discovery started
[CHG] Device 00:11:22:33:44:55 RSSI: -60
[NEW] Device 00:11:22:33:44:55 My Headphones

[bluetooth]# pair 00:11:22:33:44:55
Attempting to pair with 00:11:22:33:44:55
[CHG] Device 00:11:22:33:44:55 Connected: yes
[CHG] Device 00:11:22:33:44:55 Paired: yes

[bluetooth]# trust 00:11:22:33:44:55
[CHG] Device 00:11:22:33:44:55 Trusted: yes

[bluetooth]# connect 00:11:22:33:44:55
Connection successful
```

## Related Errors

- [PulseAudio error]({{< relref "/os/linux/linux-pulseaudio-error" >}}) — Audio device issues
- [USB/device errors]({{< relref "/os/linux/linux-kernel-module-error" >}}) — Driver problems
- [Wi-Fi authentication]({{< relref "/os/linux/linux-wifi-error" >}}) — Wireless connectivity issues
