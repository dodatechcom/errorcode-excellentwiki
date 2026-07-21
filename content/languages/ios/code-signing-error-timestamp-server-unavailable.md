---
title: "[Solution] Code Signing Error: Timestamp Server Unavailable"
description: "Fix code signing timestamp errors when Apple's timestamp servers are down."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Code Signing Error: Timestamp Server Unavailable

Code signing requires a timestamp from Apple's servers. When these servers are unavailable, the signing process fails with a timestamp error.

## Common Causes
- Apple timestamp server is experiencing downtime
- Network connectivity issues to Apple servers
- Firewall blocking timestamp server access
- Corporate proxy interfering with signing

## How to Fix
1. Wait and retry when Apple servers are available
2. Check network connectivity to Apple servers
3. Allow timestamp server domains through firewall
4. Use local timestamp for development builds

```swift
// Skip timestamp for development:
// Build Settings > Code Signing > Other Code Signing Flags
// Add: --timestamp=none

// For production, timestamp is required
// Wait for Apple's servers to be available

// Check timestamp server status:
// https://developer.apple.com/system-status/
```

## Examples
```swift
// Example: Code signing with explicit timestamp
// $ codesign --force --sign "iPhone Distribution: Team" \
//   --timestamp=http://timestamp.apple.com/code YourApp.app

// For development:
// $ codesign --force --sign "iPhone Developer: Name" \
//   --timestamp=none YourApp.app
```
