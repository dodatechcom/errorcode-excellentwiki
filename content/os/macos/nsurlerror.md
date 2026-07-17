---
title: "[Solution] macOS NSURLError — Network Connection Errors"
description: "Fix macOS NSURLError network connection errors. Causes and solutions for NSURLSession failures, timeouts, and connectivity issues."
platforms: ["macos"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nsurlerror", "network", "urlsession", "connectivity", "foundation"]
weight: 5
---

# macOS NSURLError — Network Connection Errors

NSURLError (domain: `NSURLErrorDomain`) is a family of Foundation framework errors indicating failures in URL loading and network operations. These errors span connectivity issues, timeouts, SSL problems, and request failures.

## What This Error Means

NSURLError codes range from -997 to -3007 and cover all aspects of URL-based networking in macOS. The most common variants:

- `NSURLErrorTimedOut (-1001)` — Request exceeded time limit
- `NSURLErrorCannotFindHost (-1003)` — DNS lookup failed
- `NSURLErrorCannotConnectToHost (-1004)` — TCP connection refused
- `NSURLErrorNetworkConnectionLost (-1005)` — Connection dropped unexpectedly
- `NSURLErrorNotConnectedToInternet (-1009)` — No internet connectivity

## Common Causes

- No active network connection (Wi-Fi or Ethernet disconnected)
- DNS server is unreachable or returning errors
- Firewall or proxy blocking the connection
- Server is down or rejecting connections

## How to Fix

### Verify Network Connectivity

```bash
# Check active network interfaces
ifconfig | grep "flags.*UP"

# Test DNS resolution
nslookup example.com

# Test basic connectivity
ping -c 4 8.8.8.8
```

### Reset Network Configuration

```bash
# Flush DNS cache
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder

# Renew DHCP lease
sudo ipconfig set en0 DHCP
```

### Check Proxy Settings

```bash
# View current proxy configuration
networksetup -getwebproxy Wi-Fi
networksetup -getsecurewebproxy Wi-Fi

# Disable proxy temporarily
networksetup -setwebproxystate Wi-Fi off
networksetup -setsecurewebproxystate Wi-Fi off
```

### Increase Timeout in Application Code

```swift
let config = URLSessionConfiguration.default
config.timeoutIntervalForRequest = 60
config.timeoutIntervalForResource = 300
let session = URLSession(configuration: config)
```

## Related Errors

- [NSURLError Server Trust (-1202)]({{< relref "/os/macos/nsurlerror-trust" >}}) — SSL/TLS certificate validation failure
- [Core Foundation Errors]({{< relref "/os/macos/core-foundation" >}}) — Lower-level networking errors
- [Bonjour Service Discovery Errors]({{< relref "/os/macos/bonjour-error" >}}) — Service discovery failures on the network
