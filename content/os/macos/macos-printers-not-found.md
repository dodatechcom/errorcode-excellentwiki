---
title: "[Solution] macOS Printers Not Found -- Mac Cannot Discover Printers"
description: "Fix macOS printers not found when the Mac cannot find or connect to printers. Resolve printer discovery issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Printers Not Found -- Mac Cannot Discover Printers

When your Mac cannot find printers on the network or via USB, the Print dialog shows no available printers. This affects both network (AirPrint) and USB-connected printers.

## Common Causes
- Printer and Mac are on different network segments or VLANs
- Bonjour/mDNS is disabled on the router
- Printer is in sleep mode and not responding to discovery
- USB cable is faulty or the port is not working
- macOS firewall is blocking printer discovery

## How to Fix
1. Add the printer manually by IP address
2. Ensure the printer and Mac are on the same network
3. Wake the printer from sleep mode
4. Try a different USB cable or port
5. Restart the printing services

```bash
# Restart printing services
sudo launchctl stop org.cups.cupsd
sudo launchctl start org.cups.cupsd

# Add a printer by IP address (via CUPS web interface)
open http://localhost:631
```

## Examples

```bash
# Check if the printer is discoverable via Bonjour
dns-sd -B _ipp._tcp local.

# Check if the printer responds on its IP
nc -zv printer-ip-address 631
```

This error is common when the printer is on a different VLAN, when Bonjour/mDNS is disabled on the router, or when the printer is in deep sleep mode and not responding to network probes.
