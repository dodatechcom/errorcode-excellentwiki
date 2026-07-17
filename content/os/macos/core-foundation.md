---
title: "[Solution] macOS Core Foundation Errors"
description: "Fix macOS Core Foundation errors. Causes and solutions for CFError, CFNetwork, and low-level framework failures."
platforms: ["macos"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# macOS Core Foundation Errors

Core Foundation errors (`CFErrorDomain`) are low-level framework errors in macOS that occur in CFNetwork, CFString, CFPropertyList, and other Core Foundation subsystems. They often underlie higher-level NSURLError or NSCocoaError failures.

## What This Error Means

Core Foundation errors include:

- `kCFErrorDomainCFNetwork` — Network stack errors (DNS, proxy, SSL)
- `kCFErrorDomainPOSIX` — POSIX system call errors (errno values)
- `kCFErrorDomainOSStatus` — OSStatus codes from Security framework
- `kCFErrorDomainCocoa` — Cocoa framework general errors

These errors are typically surfaced through `CFErrorRef` and may be wrapped by NSError in higher-level code.

## Common Causes

- Network stack configuration issues (DNS, proxy, VPN)
- POSIX file system errors (permission denied, file not found)
- Certificate validation failures at the transport layer
- Memory allocation failures in Core Foundation objects

## How to Fix

### Inspect CFError Details

```swift
if let cfError = error as CFError? {
    let domain = CFErrorGetDomain(cfError)
    let code = CFErrorGetCode(cfError)
    let userInfo = CFErrorCopyUserInfo(cfError)
    print("Domain: \(domain), Code: \(code), Info: \(userInfo!)")
}
```

### Fix Network Configuration

```bash
# Check DNS settings
scutil --dns | head -20

# Reset network configuration
sudo dscacheutil -flushcache
sudo networksetup -setdnsservers Wi-Fi empty
```

### Handle POSIX Errors

```swift
let posixError = POSIXError(rawValue: errno)
print("POSIX error: \(posixError?.localizedDescription ?? "unknown")")
```

### Reset Network Stack

```bash
sudo ifconfig en0 down
sudo ifconfig en0 up
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
```

## Related Errors

- [NSURLError]({{< relref "/os/macos/nsurlerror" >}}) — Higher-level network errors wrapping CFNetwork errors
- [NSURLError Server Trust (-1202)]({{< relref "/os/macos/nsurlerror-trust" >}}) — SSL/TLS trust evaluation failures
- [NSFileError]({{< relref "/os/macos/nsfileerror" >}}) — File system errors with POSIX error codes
