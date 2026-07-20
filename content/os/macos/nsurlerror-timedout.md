---
title: "[Solution] macOS NSURLErrorTimedOut — Increase Timeout & Check Network"
description: "Fix macOS NSURLErrorTimedOut (-1001) with these step-by-step solutions. Includes terminal commands and system settings."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime"]
weight: 301
---

# macOS NSURLErrorTimedOut — Increase Timeout & Check Network

NSURLErrorTimedOut (-1001) occurs when a network request exceeds its allowed time limit before receiving a response from the server.

## Common Causes

1. Slow or unreliable network connection
2. Server is overloaded or unreachable
3. Default timeout value is too short for the request
4. Proxy or firewall is delaying the connection
5. Large file download taking longer than expected

## How to Fix

### Fix 1: Increase the Request Timeout

```swift
let config = URLSessionConfiguration.default
config.timeoutIntervalForRequest = 60
config.timeoutIntervalForResource = 300
let session = URLSession(configuration: config)
```

```objectivec
NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:url];
[request setTimeoutInterval:60];
```

### Fix 2: Check Network Connection

```bash
# Test basic connectivity
ping -c 4 google.com

# Check network interface status
networksetup -listallhardwareports

# Test DNS resolution
nslookup example.com
```

### Fix 3: Check Server Response Time

```bash
# Measure server response time
curl -o /dev/null -s -w "Time: %{time_total}s\n" https://example.com

# Test with verbose output
curl -v --connect-timeout 30 https://example.com
```

## Related Errors

- [NSURLErrorCannotConnectToHost](/os/macos/nsurlerror-cannot-connect/)
- [NSURLErrorNetworkConnectionLost](/os/macos/nsurlerror-network-lost/)
- [NSURLErrorDNSLookupFailed](/os/macos/nsurlerror-dns-failed/)
