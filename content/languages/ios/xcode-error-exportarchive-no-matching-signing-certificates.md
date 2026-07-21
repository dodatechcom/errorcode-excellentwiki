---
title: "[Solution] Xcode Error: ExportArchive No Matching Signing Certificates"
description: "Fix missing signing certificate errors when exporting Xcode archives."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: ExportArchive No Matching Signing Certificates

This error appears during archive export when Xcode cannot find a valid signing certificate. The certificate may be missing, expired, or not in the keychain.

## Common Causes
- Signing certificate not installed in keychain
- Certificate expired or revoked
- Keychain not unlocked during command-line builds
- Distribution certificate does not match provisioning profile

## How to Fix
1. Download the certificate from the Apple Developer portal
2. Double-click to install it in Keychain Access
3. Ensure the certificate is not expired and is trusted
4. For CI builds, import certificates into the build keychain

```swift
// Import certificate for CI builds:
// $ security import cert.p12 -k ~/Library/Keychains/login.keychain-db \
//   -P certificate-password -T /usr/bin/codesign

// List available certificates:
// $ security find-identity -v -p codesigning

// Verify certificate is valid:
// $ security find-certificate -c "iPhone Distribution" -p
```

## Examples
```swift
// Example: ExportOptions.plist with certificate specification
// <dict>
//     <key>method</key>
//     <string>app-store</string>
//     <key>signingCertificate</key>
//     <string>iPhone Distribution: My Company (TEAMID)</string>
//     <key>provisioningProfiles</key>
//     <dict>
//         <key>com.example.myapp</key>
//         <string>MyApp App Store Profile</string>
//     </dict>
// </dict>
```
