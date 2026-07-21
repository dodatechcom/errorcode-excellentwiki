---
title: "[Solution] macOS Internet Recovery Error -- Internet Recovery Not Working"
description: "Fix macOS internet recovery error when Option+Command+R fails to start internet recovery. Resolve internet recovery issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Internet Recovery Error -- Internet Recovery Not Working

Internet Recovery downloads the macOS recovery image from Apple's servers when the local recovery partition is missing or corrupted. When it fails, you cannot repair or reinstall macOS.

## Common Causes
- WiFi connection is too weak or unstable
- DNS resolution for Apple servers is failing
- Firewall is blocking Apple CDN domains
- Apple servers are experiencing an outage
- Network proxy is interfering with the connection

## How to Fix
1. Move closer to the WiFi router or use Ethernet
2. Change DNS servers to a public DNS (1.1.1.1 or 8.8.8.8)
3. Disable any VPN or proxy
4. Try Option+Command+R (latest compatible) or Shift+Option+Command+R (original)
5. Create a bootable USB installer as an alternative

```bash
# Test connectivity to Apple servers
ping appldnld.apple.com
ping swcdn.apple.com

# Create a bootable USB installer (if you have another Mac)
sudo /Applications/Install\ macOS\ Sequoia.app/Contents/Resources/createinstallmedia --volume /Volumes/USBDrive
```

## Examples

```bash
# Check Apple system status
# Visit https://www.apple.com/support/systemstatus/
```

This error is common when the WiFi signal is too weak, when corporate firewalls block Apple CDN domains, or when Apple's servers are experiencing downtime.
