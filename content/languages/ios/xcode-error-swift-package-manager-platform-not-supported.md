---
title: "[Solution] Xcode Error: Swift Package Manager Platform Not Supported"
description: "Fix platform support errors when using Swift Package Manager dependencies."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: Swift Package Manager Platform Not Supported

This error occurs when a Swift package does not declare support for the platform you are building for. The package's Package.swift excludes your target platform.

## Common Causes
- Package only supports macOS but you need iOS
- Package requires visionOS but you target iOS
- Platform requirement in Package.swift excludes your target
- Package uses APIs only available on certain platforms

## How to Fix
1. Check the package's Package.swift for platform declarations
2. Fork the package and add iOS platform support
3. Use conditional compilation in the package to support iOS
4. Find an alternative package that supports your platform

```swift
// In Package.swift, platforms are declared:
// platforms: [.iOS(.v15), .macOS(.v12), .watchOS(.v8)]

// If iOS is missing, the package cannot be used for iOS
// You can fork and add it:
// platforms: [.iOS(.v15), .macOS(.v12), .watchOS(.v8)]
```

## Examples
```swift
// Example: Checking platform support before adding dependency
// Visit the package's GitHub repository
// Look at Package.swift for:
// platforms: [
//     .iOS(.v15),     // Supports iOS 15+
//     .macOS(.v12),   // Supports macOS 12+
//     .watchOS(.v8)   // Supports watchOS 8+
// ]

// If iOS is not listed, the package cannot be used for iOS projects
```
