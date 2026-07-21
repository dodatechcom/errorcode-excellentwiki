---
title: "[Solution] macOS Bonjour Error -- Bonjour Service Discovery Not Working"
description: "Fix macOS Bonjour error when Bonjour cannot discover services on the local network. Resolve Bonjour discovery issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Bonjour Error -- Bonjour Service Discovery Not Working

Bonjour (mDNS) is Apple's zero-configuration networking protocol that discovers devices and services on the local network. When it fails, you cannot find AirPrint printers, AirPlay devices, or shared folders.

## Common Causes
- mDNSResponder process has crashed
- Firewall is blocking mDNS traffic (UDP port 5353)
- Router is not forwarding mDNS between network segments
- DNS cache is stale or corrupted
- Network interface is not properly configured

## How to Fix
1. Restart the mDNSResponder daemon
2. Flush the DNS cache
3. Check firewall settings for mDNS blocking
4. Ensure the router supports mDNS forwarding
5. Restart the Mac to reset all network services

```bash
# Restart mDNSResponder
sudo killall -HUP mDNSResponder

# Flush DNS cache
sudo dscacheutil -flushcache

# Test Bonjour discovery
dns-sd -B _services._dns-sd._tcp local.
```

## Examples

```bash
# Discover printers on the network
dns-sd -B _ipp._tcp local.

# Discover AirPlay devices
dns-sd -B _airplay._tcp local.
```

This error is common when the mDNSResponder process crashes, when the firewall blocks mDNS traffic, or when the router does not forward mDNS between VLANs.
