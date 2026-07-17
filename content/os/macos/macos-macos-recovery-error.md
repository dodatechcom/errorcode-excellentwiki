---
title: "[Solution] macOS Recovery: Internet Recovery Failed Error on Mac"
description: "Fix macOS Recovery errors when Internet Recovery fails, cannot connect to recovery servers, or recovery mode doesn't load."
platforms: ["macos"]
severities: ["error"]
error-types: ["system-error"]
tags: ["recovery", "internet-recovery", "boot", "install", "macos"]
weight: 5
---

# macOS Recovery: Internet Recovery Failed Error on Mac

Mac cannot enter Internet Recovery, shows spinning globe forever, or fails to download recovery image from Apple servers.

## What This Error Means

Internet Recovery downloads a minimal macOS recovery environment from Apple's servers when the local recovery partition is unavailable. Failures occur due to network issues, DNS problems, or Apple server connectivity problems.

## Common Causes

- Network connectivity issues
- DNS resolution failure
- Firewall blocking recovery servers
- Corrupted recovery partition
- Apple server outages
- Proxy/VPN interference

## How to Fix

### Check Network Connectivity

```bash
# Test connectivity to Apple recovery servers
curl -v https://osrecovery.apple.com

# Check DNS resolution
nslookup osrecovery.apple.com

# Try different DNS server
sudo networksetup -setdnsservers Wi-Fi 8.8.8.8 8.8.4.4
```

### Use Different Network

```bash
# Switch to different Wi-Fi network
# Use Ethernet if available
# Use iPhone Personal Hotspot

# Avoid networks with:
# - Captive portals (hotels, airports)
# - Strict firewalls
# - Corporate proxies
```

### Boot into Local Recovery

```bash
# Intel Mac: Restart holding Cmd+R
# Apple Silicon: Hold power button, select Recovery

# If local recovery fails, try Internet Recovery:
# Intel: Restart holding Option+Cmd+R
# Apple Silicon: Hold power button, select "Options"
```

### Create Bootable USB Installer

```bash
# Download macOS installer from App Store
# Create bootable USB:

# Format USB drive
diskutil eraseDisk JHFS+ "USB" GPTFormat /dev/disk2

# Create installer (Monterey example)
sudo /Applications/Install\ macOS\ Monterey.app/Contents/Resources/createinstallmedia \
  --volume /Volumes/USB
```

### Check Apple System Status

Visit [apple.com/support/systemstatus](https://www.apple.com/support/systemstatus/) to verify recovery services are operational.

### Reset Network Settings

```bash
# Reset network configuration
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder

# Remove network preferences
sudo rm /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist
```

## Related Errors

- [Boot Error]({{< relref "/os/macos/macos-boot-error-v2" >}}) — Boot issues
- [Firmware Update Error]({{< relref "/os/macos/macos-firmware-update-error" >}}) — Firmware issues
- [Wi-Fi Error]({{< relref "/os/macos/macos-wifi-error-v2" >}}) — Network issues
