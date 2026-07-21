---
title: "[Solution] Xcode Error: Product Bundle Identifier Already Taken"
description: "Fix bundle identifier conflicts when registering your iOS app."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: Product Bundle Identifier Already Taken

This error occurs during archive or upload when your app's bundle identifier conflicts with an existing app on the App Store or in your developer account.

## Common Causes
- Another app already uses this bundle identifier
- Copy-paste from a template without changing the identifier
- Wildcard provisioning profiles being used with specific identifiers
- Renamed target without updating the bundle identifier

## How to Fix
1. Choose a unique bundle identifier for your app
2. Follow reverse-DNS format: com.yourcompany.appname
3. Check App Store Connect for conflicting registrations
4. Update the identifier in both Info.plist and target settings

```swift
// Set a unique bundle identifier:
// Target > General > Identity > Bundle Identifier
// Use format: com.yourcompany.appname

// For Info.plist:
// CFBundleIdentifier = com.yourcompany.appname

// For multiple targets (extensions):
// Main app: com.yourcompany.appname
// Widget: com.yourcompany.appname.widget
// Share extension: com.yourcompany.appname.share
```

## Examples
```swift
// Example: Checking bundle identifier consistency
// Use PlistBuddy to verify:
// $ /usr/libexec/PlistBuddy -c "Print CFBundleIdentifier" Info.plist
// Output: com.example.myapp

// Verify it matches your provisioning profile:
// $ security find-identity -v -p codesigning
```
