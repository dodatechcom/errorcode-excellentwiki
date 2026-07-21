---
title: "[Solution] macOS Bluetooth Not Discoverable -- Mac Not Visible to Other Devices"
description: "Fix macOS Bluetooth not discoverable when other devices cannot find your Mac. Resolve Mac not appearing in Bluetooth searches."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Bluetooth Not Discoverable -- Mac Not Visible to Other Devices

When your Mac's Bluetooth is not discoverable, other devices cannot find it during a Bluetooth scan. The Mac may work fine connecting to devices it already knows, but new pairings fail.

## Common Causes
- Bluetooth is turned off or in airplane mode
- Mac is not in discoverable mode
- Another Bluetooth adapter is interfering
- macOS Bluetooth stack has a software glitch
- Bluetooth hardware is malfunctioning

## How to Fix
1. Open System Preferences > Bluetooth and ensure it is on
2. Make sure 'Allow Bluetooth devices to find this computer' is checked
3. Toggle Bluetooth off and on to reset the discovery state
4. Restart the Bluetooth daemon from terminal
5. Reset the Bluetooth module by holding Shift+Option and clicking the Bluetooth icon

```bash
# Restart the Bluetooth daemon
sudo pkill bluetoothd

# Check Bluetooth status
system_profiler SPBluetoothDataType | head -20
```

## Examples

```bash
# Check if Bluetooth hardware is detected
system_profiler SPBluetoothDataType | grep -i "chipset\|manufacturer"
```

This error is common after a macOS update resets Bluetooth settings, when the Bluetooth daemon crashes, or when interference from USB 3.0 devices disrupts the Bluetooth radio.
