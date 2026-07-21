---
title: "[Solution] macOS Spinning Globe at Startup -- Internet Recovery Stuck"
description: "Fix macOS spinning globe stuck during internet recovery. Resolve Mac showing spinning globe instead of Apple logo at boot."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Spinning Globe at Startup -- Internet Recovery Stuck

The spinning globe appears when macOS is attempting to boot from Internet Recovery -- downloading the recovery image from Apple servers. When this globe spins indefinitely, the Mac cannot connect to Apple or the download is failing.

## Common Causes
- Weak or unstable Wi-Fi connection during recovery
- DNS server issues preventing Apple server resolution
- Firewall or proxy blocking access to Apple CDN
- Corrupted local recovery partition forcing internet recovery
- Apple server outage in your region

## How to Fix
1. Move closer to the Wi-Fi router or use an Ethernet adapter
2. Click the Wi-Fi icon in the menu bar and select a different network
3. Use Command+R instead of Option+Command+R to try local Recovery first
4. Create a bootable USB installer using another Mac if internet recovery fails

```bash
# Create a bootable USB installer on another Mac
# Download macOS from App Store, then:
sudo /Applications/Install\ macOS\ Sequoia.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume
```

## Examples

```bash
# Test DNS resolution from another Mac on the same network
dig appldnld.apple.com
ping swcdn.apple.com
```

The spinning globe error is common after a failed firmware update, when the internal recovery partition has been deleted, or on networks with strict corporate firewalls.
