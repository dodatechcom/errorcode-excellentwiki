---
title: "[Solution] macOS WiFi DNS Error — DNS Resolution Failing"
description: "Fix macOS WiFi DNS error: DNS resolution fails, cannot resolve hostnames, DNS server not responding, internet works by IP not name."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 163
---

# WiFi DNS Error — DNS Resolution Failing

Fix macOS WiFi DNS error: DNS resolution fails, cannot resolve hostnames, DNS server not responding, internet works by IP not name.

## Common Causes

- DNS server configured in network settings is down or unreachable
- DNS cache corrupted on Mac
- Router DNS forwarding not working properly
- ISP DNS servers experiencing outage

## How to Fix

### 1. Flush DNS Cache

```bash
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
# Wait 10 seconds and test DNS
```

### 2. Change DNS Servers

```bash
sudo networksetup -setdnsservers Wi-Fi 8.8.8.8 8.8.4.4 1.1.1.1
# Or System Settings → Network → WiFi → Details → DNS → Add servers
```

### 3. Test DNS Resolution

```bash
nslookup google.com
dig google.com
host google.com
```

### 4. Reset DNS Configuration

```bash
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
sudo ifconfig en0 down && sudo ifconfig en0 up
```

## Common Scenarios

This error commonly occurs when:

- Websites won't load by name but work by IP address
- DNS resolution takes several seconds before page loads
- Some websites work while others fail with 'cannot find server'
- DNS error appears only on Mac but not on other devices on same network

## Prevent It

- Use reliable public DNS servers like Google (8.8.8.8) or Cloudflare (1.1.1.1)
- Flush DNS cache if hostname resolution becomes slow
- Restart Mac's network services before changing DNS configuration
- Keep router firmware updated for proper DNS forwarding
