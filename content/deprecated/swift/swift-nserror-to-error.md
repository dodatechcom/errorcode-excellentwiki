---
title: "[Solution] Deprecated Function Migration: NSError to Error protocol"
description: "Migrate from deprecated NSError to Swift Error protocol."
deprecated_function: "NSError(domain:code:userInfo:)"
replacement_function: "Error protocol enum"
languages: ["swift"]
deprecated_since: "Swift 2.0+"
---

# [Solution] Deprecated Function Migration: NSError to Error protocol

The `NSError(domain:code:userInfo:)` has been deprecated in favor of `Error protocol enum`.

## Migration Guide

Error protocol provides type safety

NSError is verbose and type-unsafe. Error protocol with enums is cleaner.

## Before (Deprecated)

```swift
let error = NSError(
    domain: "App",
    code: 42,
    userInfo: [NSLocalizedDescriptionKey: "Failed"]
)
```

## After (Modern)

```swift
enum AppError: Error {
    case notFound
    case serverError(code: Int)
}

throw AppError.notFound

// Catch with pattern matching
catch AppError.serverError(let code) {
    print("Server error: \(code)")
}
```

## Key Differences

- Error protocol for type safety
- Enum cases for specific errors
- Associated values for extra data
- Pattern matching with catch
