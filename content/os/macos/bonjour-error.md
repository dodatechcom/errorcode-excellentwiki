---
title: "[Solution] macOS Bonjour Service Discovery Errors"
description: "Fix macOS Bonjour service discovery errors. Causes and solutions for mDNS, DNS-SD, and network service resolution failures."
platforms: ["macos"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# macOS Bonjour Service Discovery Errors

Bonjour errors indicate failures in mDNS (multicast DNS) service discovery and resolution. These errors affect AirPrint, AirPlay, file sharing, and local network service discovery.

## What This Error Means

Bonjour uses mDNS and DNS-SD protocols for zero-configuration networking. Errors manifest as:

- Service browser returns no results
- Service resolution times out
- `kDNSServiceErr_DefunctConnection (-65570)` — Connection to mDNSResponder is defunct
- `kDNSServiceErr_ServiceNotRunning (-65563)` — mDNSResponder daemon is not running

## Common Causes

- mDNSResponder daemon has crashed or is unresponsive
- Network is configured to block multicast traffic
- Firewall blocking mDNS port 5353/UDP
- VPN tunnel is intercepting multicast packets

## How to Fix

### Restart mDNSResponder

```bash
sudo killall -HUP mDNSResponder
```

### Test Bonjour Discovery

```bash
# Browse for all services
dns-sd -B _services._dns-sd._udp local.

# Browse for specific service type
dns-sd -B _http._tcp local.

# Resolve a specific service
dns-sd -L "ServiceName" _http._tcp local.
```

### Check Firewall Settings

```bash
# View firewall rules
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --listapps

# Allow mDNSResponder through firewall
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --add /usr/sbin/mDNSResponder
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --unblockapp /usr/sbin/mDNSResponder
```

### Verify Multicast Support

```bash
# Check if multicast is working
ping -c 3 224.0.0.1

# Check network interface for multicast support
ifconfig en0 | grep -i multicast
```

### Reset Network Configuration

```bash
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
sudo ifconfig en0 down && sudo ifconfig en0 up
```

## Related Errors

- [NSURLError]({{< relref "/os/macos/nsurlerror" >}}) — Network errors that may result from Bonjour failures
- [Wi-Fi / AirPort Errors]({{< relref "/os/macos/airport-error" >}}) — Wireless connectivity issues affecting Bonjour
- [Core Foundation Errors]({{< relref "/os/macos/core-foundation" >}}) — Low-level networking framework errors
