---
title: "[Solution] App Transport Security Blocked Request"
description: "Fix App Transport Security (ATS) blocking HTTP requests in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# App Transport Security Blocked Request

ATS blocks non-HTTPS connections by default. Apps need proper ATS configuration to allow specific HTTP domains or disable ATS for development.

## Common Causes
- App makes HTTP requests to non-HTTPS URLs
- ATS exception domain not configured in Info.plist
- Subdomains not included in exception
- NSAllowsArbitraryLoads set incorrectly

## How to Fix
1. Add ATS exception for specific domains in Info.plist
2. Use HTTPS whenever possible
3. Set NSAllowsArbitraryLoads only for debugging
4. Include all required subdomains in exceptions

```xml
<!-- Info.plist exception for specific domain -->
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSExceptionDomains</key>
    <dict>
        <key>example.com</key>
        <dict>
            <key>NSExceptionAllowsInsecureHTTPLoads</key>
            <true/>
        </dict>
    </dict>
</dict>
```

## Examples
```swift
// Check ATS exceptions at runtime:
if let url = URL(string: "http://example.com/api") {
    let config = URLSessionConfiguration.default
    config.urlCache = nil
    let session = URLSession(configuration: config)
    let task = session.dataTask(with: url) { data, response, error in
        if let error = error as? URLError, error.code == .secureConnectionFailed {
            print("ATS is blocking this request")
        }
    }
    task.resume()
}
```
