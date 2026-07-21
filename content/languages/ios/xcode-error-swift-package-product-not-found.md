---
title: "[Solution] Xcode Error: Swift Package Product Not Found"
description: "Fix missing Swift package product errors in Xcode dependencies."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: Swift Package Product Not Found

This error appears when Xcode cannot find a product defined in a Swift package dependency. The product name may be incorrect or the package may not have been resolved.

## Common Causes
- Product name typo in package dependency
- Package not resolved or downloaded
- Package.swift does not define the requested product
- Version conflict prevents package resolution

## How to Fix
1. Verify the product name in the package's Package.swift
2. Resolve packages via File > Packages > Resolve Package Versions
3. Check that the package URL points to the correct repository
4. Update the version requirement if needed

```swift
// In Package.swift, products are defined like:
// .library(name: "MyLibrary", targets: ["MyLibrary"])

// In Xcode, add via:
// File > Add Package Dependencies
// Enter repository URL
// Select the product from the list

// Or in Package Dependencies tab:
// Click the package and verify the product is checked
```

## Examples
```swift
// Example: Adding a package dependency in code
// File > Add Package Dependencies
// Repository URL: https://github.com/user/repo.git
// Version: Up to Next Major Version - 1.0.0

// After adding, check Package Dependencies:
// Navigator > YourProject > Package Dependencies
// Verify the package appears and is resolved
```
