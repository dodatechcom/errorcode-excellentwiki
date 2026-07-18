---
title: "[Solution] macOS Network Setup Error — Network Interfaces Not Configured"
description: "Fix macOS Network Setup error: network interfaces not configured, network locations broken, network preferences corrupted."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 189
---

# Network Setup Error — Network Interfaces Not Configured

Fix macOS Network Setup error: network interfaces not configured, network locations broken, network preferences corrupted.

## Common Causes

- Network location settings corrupted
- Multiple network configurations conflicting
- System network preferences file corrupted
- Third-party network utility modifying system settings

## How to Fix

### 1. Check Network Interfaces

```bash
networksetup -listallhardwareports
ifconfig -a
networksetup -listallnetworkservices
```

### 2. Create New Network Location

```bash
# System Settings → Network → Locations → Edit Locations → Add → Create new location
```

### 3. Reset Network Preferences

```bash
sudo rm -f /Library/Preferences/SystemConfiguration/NetworkInterfaces.plist
sudo rm -f /Library/Preferences/SystemConfiguration/preferences.plist
sudo shutdown -r now
```

### 4. Repair Network from Recovery

```bash
# Recovery → Reinstall macOS to restore network configuration files
# This preserves data but resets network settings
```

## Common Scenarios

This error commonly occurs when:

- Network interfaces disappear from System Settings after macOS update
- Multiple network locations appear with conflicting settings
- Wi-Fi and Ethernet cannot be configured simultaneously
- Network settings revert to defaults after every restart

## Prevent It

- Create backup of network settings before major macOS updates
- Use network locations to manage different network configurations
- Reset network preferences if network settings become corrupted
- Keep macOS updated for network configuration stability improvements
