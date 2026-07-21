---
title: "[Solution] macOS AirDrop Not Working -- Mac Cannot Send or Receive via AirDrop"
description: "Fix macOS AirDrop not working when Mac cannot discover or send files to nearby devices. Resolve AirDrop discovery and transfer failures."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS AirDrop Not Working -- Mac Cannot Send or Receive via AirDrop

AirDrop uses a combination of Bluetooth and WiFi to transfer files between Apple devices. When it fails, the Mac may not discover nearby devices, or the transfer may fail to start.

## Common Causes
- Bluetooth or WiFi is turned off
- Firewall is blocking AirDrop connections
- AirDrop is set to 'Contacts Only' and the sender is not in your contacts
- Both devices are not on the same WiFi network (required for some transfers)
- Bluetooth discovery is not enabled

## How to Fix
1. Ensure both WiFi and Bluetooth are turned on
2. Set AirDrop to 'Everyone' temporarily for testing
3. Disable the firewall temporarily to test AirDrop
4. Sign out and back into iCloud on both devices
5. Reset Bluetooth by turning it off and on again

```bash
# Check Bluetooth status
system_profiler SPBluetoothDataType | grep -i "state\|discoverable"

# Check WiFi status
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I
```

## Examples

```bash
# Disable firewall temporarily for testing
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate off

# Re-enable after testing
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on
```

This error is common when one device has Bluetooth off, when the firewall is blocking AirDrop ports, or when AirDrop is set to Contacts Only and the devices do not share a contact.
