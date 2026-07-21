---
title: "[Solution] Provisioning Profile Bundle Identifier Mismatch"
description: "Fix bundle identifier mismatches between provisioning profile and project."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Provisioning Profile Bundle Identifier Mismatch

This error occurs when the bundle identifier in your project does not match the one specified in the provisioning profile. They must be an exact match.

## Common Causes
- Bundle identifier changed in Xcode but profile not updated
- Copy-paste error when setting the identifier
- Wildcard profile used with a specific identifier requirement
- Extension bundle identifier does not follow app prefix pattern

## How to Fix
1. Verify the bundle identifier in both the project and portal
2. Regenerate the profile with the correct bundle identifier
3. Ensure all extensions use the app's bundle ID as prefix
4. Use automatic signing to keep identifiers in sync

```swift
// Check your bundle identifier:
// Target > General > Identity > Bundle Identifier
// Must match exactly with: com.example.myapp

// For extensions:
// Main app: com.example.myapp
// Widget: com.example.myapp.widget
// Share extension: com.example.myapp.share
```

## Examples
```swift
// Example: Verifying bundle ID consistency
// $ /usr/libexec/PlistBuddy -c "Print CFBundleIdentifier" Info.plist
// com.example.myapp

// Compare with provisioning profile:
// $ security cms -D -i embedded.mobileprovision | \
//   grep -A1 "application-identifier"
```
