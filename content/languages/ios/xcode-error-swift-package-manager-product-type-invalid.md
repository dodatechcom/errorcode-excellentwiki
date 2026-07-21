---
title: "[Solution] Xcode Error: Swift Package Manager Product Type Invalid"
description: "Fix invalid product type errors in Swift Package Manager configuration."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: Swift Package Manager Product Type Invalid

Invalid product type errors occur when the package's product type does not match what Xcode expects. Common when mixing library and executable product types.

## Common Causes
- Package declares executable but you expect a library
- Product type mismatch between Package.swift and Xcode
- Test product not properly configured for XCTest
- Plugin product type not supported by Xcode version

## How to Fix
1. Verify the product type in the package's Package.swift
2. Use .library for reusable code, .executable for command-line tools
3. Ensure test products use .testTarget
4. Check Xcode version supports the product type

```swift
// In Package.swift, product types:
.library(name: "MyLib", targets: ["MyLib"])     // Reusable code
.executable(name: "MyCLI", targets: ["MyCLI"])  // Command-line tool
.plugin(name: "MyPlugin", capability: ...)      // Build plugin

// For Xcode to use a library product:
// File > Add Package Dependencies > Select the library product
```

## Examples
```swift
// Example: Correcting product type in Package.swift
// Package.swift:
let package = Package(
    name: "MyPackage",
    products: [
        .library(
            name: "MyLibrary",
            type: .dynamic,  // or .static or omit for auto
            targets: ["MyLibrary"]
        ),
    ],
    targets: [
        .target(name: "MyLibrary"),
        .testTarget(name: "MyLibraryTests", dependencies: ["MyLibrary"]),
    ]
)
```
