---
title: "[Solution] macOS NSURLErrorUnsupportedURL — Fix Protocol Errors"
description: "Fix macOS NSURLErrorUnsupportedURL (-1002) with these step-by-step solutions. Includes terminal commands and system settings."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime"]
weight: 307
---

# macOS NSURLErrorUnsupportedURL — Fix Protocol Errors

NSURLErrorUnsupportedURL (-1002) indicates the URL uses a protocol scheme that NSURLSession does not support.

## Common Causes

1. Custom URL scheme is not registered with the system
2. Using an unsupported protocol (e.g., ftp:// on iOS)
3. URL scheme contains invalid characters
4. App does not handle the specified scheme
5. URL scheme is case-sensitive and incorrectly cased

## How to Fix

### Fix 1: Check URL Scheme Support

```swift
// Verify the URL scheme is supported
if let url = URL(string: "myapp://resource") {
    if UIApplication.shared.canOpenURL(url) {
        UIApplication.shared.open(url)
    }
}
```

### Fix 2: Register Custom URL Scheme

Add the URL scheme to your app's `Info.plist`:

```xml
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
        <string>com.example.myapp</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>myapp</string>
        </array>
    </dict>
</array>
```

### Fix 3: Verify Protocol Support

```bash
# Check if a protocol scheme is handled
curl --version | grep -i "protocols"

# Test URL scheme availability
/usr/bin/python3 -c "import urllib.parse; print(urllib.parse.urlsplit('https://example.com').scheme)"
```

## Related Errors

- [NSURLErrorBadURL](/os/macos/nsurlerror-bad-url/)
- [NSURLErrorCannotConnectToHost](/os/macos/nsurlerror-cannot-connect/)
- [NSURLErrorTimedOut](/os/macos/nsurlerror-timedout/)
