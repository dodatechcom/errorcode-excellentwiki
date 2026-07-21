---
title: "[Solution] App Transport Security ATS Exception Error"
description: "Fix App Transport Security exception configuration errors in Info.plist."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# App Transport Security ATS Exception Error

ATS exceptions fail when the domain is misspelled, when the exception keys are incorrect, or when required exception levels are not specified.

## Common Causes
- Domain name misspelled in exception
- Missing NSExceptionRequiresForwardSecrecy for specific domains
- NSAllowsArbitraryLoads conflicts with specific domain exceptions
- Subdomains not properly included

## How to Fix
1. Verify domain spelling matches the request URL exactly
2. Set appropriate exception level for each domain
3. Use NSExceptionRequiresForwardSecrecy when needed
4. Test each exception domain individually

```xml
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSExceptionDomains</key>
    <dict>
        <key>api.example.com</key>
        <dict>
            <key>NSExceptionAllowsInsecureHTTPLoads</key>
            <true/>
            <key>NSIncludesSubdomains</key>
            <true/>
        </dict>
    </dict>
</dict>
```

## Examples
```swift
// Common ATS exception patterns:
// 1. Allow specific domain HTTP:
// NSExceptionAllowsInsecureHTTPLoads = true for domain

// 2. Allow all HTTP (development only):
// NSAllowsArbitraryLoads = true

// 3. Allow local networking:
// NSAllowsLocalNetworking = true

// 4. Exception for legacy TLS:
// NSExceptionMinimumTLSVersion = TLSv1.0
```
