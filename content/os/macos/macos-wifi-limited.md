---
title: "[Solution] macOS WiFi Limited Connection -- Mac Shows No Internet on WiFi"
description: "Fix macOS WiFi limited connection when Mac connects to WiFi but has no internet access. Resolve WiFi connected no internet on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS WiFi Limited Connection -- Mac Shows No Internet on WiFi

Your Mac may connect to WiFi successfully but show 'No Internet Connection' or have a yellow dot in the WiFi menu. The local network works but internet access is unavailable.

## Common Causes
- DNS resolution is failing even though the connection is active
- ISP service is down or the modem needs a restart
- Router's DNS relay is not forwarding requests
- VPN is routing traffic through a non-functional tunnel
- Captive portal (hotel/airport WiFi) has not been accepted

## How to Fix
1. Test DNS resolution using terminal
2. Restart the modem and router
3. Set DNS servers manually to a public DNS
4. Disable VPN and check if internet works
5. Open a browser and complete the captive portal if prompted

```bash
# Test DNS resolution
dig google.com
nslookup google.com

# Test raw internet connectivity
ping -c 4 8.8.8.8
```

## Examples

```bash
# Check if DNS is the issue
# If ping 8.8.8.8 works but dig google.com fails, DNS is the problem
networksetup -setdnsservers Wi-Fi 1.1.1.1 8.8.8.8
```

This error is common when the ISP modem needs a restart, when the router's DNS relay is malfunctioning, or when connecting to a captive portal WiFi that requires browser interaction.
