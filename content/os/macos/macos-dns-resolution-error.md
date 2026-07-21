---
title: "[Solution] macOS DNS Resolution Error -- Mac Cannot Resolve Domain Names"
description: "Fix macOS DNS resolution error when Mac cannot resolve domain names. Resolve DNS not working on Mac while IP connectivity works."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS DNS Resolution Error -- Mac Cannot Resolve Domain Names

DNS resolution errors occur when your Mac can reach the internet by IP address but cannot translate domain names to IP addresses. Web browsers show 'Server not found' while ping to IP addresses works.

## Common Causes
- DNS server is down or unreachable
- DNS cache is corrupted
- VPN or proxy is interfering with DNS resolution
- /etc/resolv.conf has incorrect or missing DNS entries
- Router DNS relay is malfunctioning

## How to Fix
1. Flush the local DNS cache
2. Set DNS servers manually to a public DNS
3. Check /etc/resolv.conf for correct entries
4. Disable VPN or proxy and test DNS again
5. Restart the networking services

```bash
# Flush DNS cache
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder

# Set DNS servers
networksetup -setdnsservers Wi-Fi 1.1.1.1 8.8.8.8

# Check current DNS settings
scutil --dns
```

## Examples

```bash
# Test DNS resolution
dig google.com
nslookup google.com
```

This error is common when the ISP's DNS server goes down, when the DNS cache is corrupted after a network change, or when a VPN client modifies DNS settings and then disconnects without restoring them.
