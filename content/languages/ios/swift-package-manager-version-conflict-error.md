---
title: "[Solution] Swift Package Manager Version Conflict Error"
description: "Fix SPM version conflict errors when multiple dependencies require incompatible versions."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Swift Package Manager Version Conflict Error

Version conflicts arise when two or more dependencies require different versions of the same package or incompatible Swift tools versions.

## Common Causes
- Two dependencies depend on different versions of a shared library
- Minimum deployment target incompatible with package version
- Swift tools version mismatch between packages
- Transitive dependency version conflict

## How to Fix
1. Check the dependency graph for conflicts
2. Update version requirements to compatible ranges
3. Fork and modify packages if necessary
4. Use SPM diagnostics to identify conflicting packages

```swift
// Resolve conflicts:
// $ swift package resolve
// Shows conflicting dependencies

// Update to compatible versions:
.package(url: "...", from: "2.0.0") // Use wider range
```

## Examples
```swift
// Diagnose SPM conflicts:
// $ swift package show-dependencies
// $ swift package diagnose-api-breaking-changes main

// In Package.swift, use compatible ranges:
dependencies: [
    .package(url: "https://github.com/A/Dep1.git", from: "1.0.0"),
    .package(url: "https://github.com/B/Dep2.git", .upToNextMajor(from: "2.0.0"))
]
```
