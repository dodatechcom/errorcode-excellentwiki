---
title: "[Solution] Code Signing Error: Resource Missing Info.plist"
description: "Fix code signing errors when Info.plist is missing from a bundle."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Code Signing Error: Resource Missing Info.plist

Code signing fails when a framework or bundle being signed does not contain an Info.plist file. Every signed bundle requires this file.

## Common Causes
- Framework built without Info.plist in the bundle
- Resource bundle missing its Info.plist
- Copy Bundle Resources phase does not include Info.plist
- Framework build settings misconfigured

## How to Fix
1. Add an Info.plist file to the framework target
2. Ensure INFOPLIST_FILE build setting points to the correct file
3. Verify the Info.plist is included in the Copy Bundle Resources phase
4. For resource bundles, create a minimal Info.plist

```swift
// Create Info.plist for framework:
// File > New > File > iOS > Property List
// Name it: Info.plist

// In Build Settings:
// INFOPLIST_FILE = $(SRCROOT)/Frameworks/MyFramework/Info.plist

// Minimum required Info.plist content:
// CFBundleDevelopmentRegion = en
// CFBundleIdentifier = $(PRODUCT_BUNDLE_IDENTIFIER)
// CFBundleVersion = 1
```

## Examples
```swift
// Example: Minimal Info.plist for framework
// <?xml version="1.0" encoding="UTF-8"?>
// <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
//   "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
// <plist version="1.0">
// <dict>
//     <key>CFBundleDevelopmentRegion</key>
//     <string>$(DEVELOPMENT_LANGUAGE)</string>
//     <key>CFBundleExecutable</key>
//     <string>$(EXECUTABLE_NAME)</string>
//     <key>CFBundleIdentifier</key>
//     <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
//     <key>CFBundleInfoDictionaryVersion</key>
//     <string>6.0</string>
//     <key>CFBundleName</key>
//     <string>$(PRODUCT_NAME)</string>
//     <key>CFBundlePackageType</key>
//     <string>$(PRODUCT_BUNDLE_PACKAGE_TYPE)</string>
//     <key>CFBundleShortVersionString</key>
//     <string>1.0</string>
//     <key>CFBundleVersion</key>
//     <string>1</string>
// </dict>
// </plist>
```
