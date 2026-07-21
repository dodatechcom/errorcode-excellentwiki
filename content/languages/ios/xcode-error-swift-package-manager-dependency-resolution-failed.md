---
title: "[Solution] Xcode Error: Swift Package Manager Dependency Resolution Failed"
description: "Fix SPM dependency resolution failures in Xcode projects."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: Swift Package Manager Dependency Resolution Failed

SPM dependency resolution fails when Xcode cannot fetch, resolve, or build a Swift Package dependency. Network issues or version conflicts are typical causes.

## Common Causes
- Package repository URL is inaccessible
- Version requirements conflict between dependencies
- Package contains incompatible Swift code
- Network proxy or firewall blocking package downloads

## How to Fix
1. Check network connectivity and proxy settings
2. Reset package caches via File > Packages > Reset Package Caches
3. Verify the package URL is correct and accessible
4. Update version requirements to compatible ranges

```swift
// In Package.swift, ensure compatible version range:
.package(url: "https://github.com/user/repo.git", from: "1.0.0")

// Or pin to a specific compatible version:
.package(url: "https://github.com/user/repo.git", exact: "1.2.3")

// For Xcode GUI, go to:
// File > Add Package Dependencies
// Enter the repository URL
// Select version requirement
```

## Examples
```swift
// Example: Debugging SPM resolution
// Terminal: Navigate to project and run:
// $ swift package resolve

// If this fails, check Package.resolved:
// $ cat Package.resolved

// To clear caches and re-resolve:
// $ rm -rf .build
// $ swift package resolve
```
