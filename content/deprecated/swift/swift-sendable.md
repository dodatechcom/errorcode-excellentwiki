---
title: "[Solution] Deprecated Function Migration: @Sendable annotation to Sendable protocol"
description: "Migrate from deprecated @Sendable annotation to Sendable protocol."
deprecated_function: "@Sendable closure"
replacement_function: "struct Value: Sendable {}"
languages: ["swift"]
deprecated_since: "Swift 5.5+"
---

# [Solution] Deprecated Function Migration: @Sendable annotation to Sendable protocol

The `@Sendable closure` has been deprecated in favor of `struct Value: Sendable {}`.

## Migration Guide

Sendable protocol is more comprehensive.

## Before (Deprecated)

```swift
let handler: @Sendable () -> Void = { }
```

## After (Modern)

```swift
struct MyValue: Sendable {
    let data: Int
}
```

## Key Differences

- Sendable protocol is more comprehensive
