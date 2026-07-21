---
title: "[Solution] Deprecated Function Migration: NSError to Swift Error protocol"
description: "Migrate from deprecated NSError patterns to Swift Error protocol for error handling."
deprecated_function: "NSError with domain/code"
replacement_function: "enum Error: Error"
languages: ["swift"]
deprecated_since: "Swift 2.0+"
---

# [Solution] Deprecated Function Migration: NSError to Swift Error protocol

The `NSError with domain/code` has been deprecated in favor of `enum Error: Error`.

## Migration Guide

Swift Error protocol provides type-safe errors with enum cases.

## Before (Deprecated)

```swift
let error = NSError(
    domain: "com.app",
    code: 42,
    userInfo: [NSLocalizedDescriptionKey: "Something failed"]
)
do {
    try riskyOperation()
} catch let error as NSError {
    print(error.localizedDescription)
}
```

## After (Modern)

```swift
enum AppError: Error {
    case notFound
    case unauthorized
    case serverError(code: Int)
}

do {
    try riskyOperation()
} catch AppError.notFound {
    print("Not found")
} catch AppError.serverError(let code) {
    print("Server error: \(code)")
} catch {
    print("Unknown error")
}
```

## Key Differences

- Swift Error protocol for type safety
- Enum cases for specific errors
- Associated values for extra data
- catch for pattern matching errors
