---
title: "[Solution] Deprecated Function Migration: NSNotification to Notification.Name"
description: "Migrate from deprecated NSNotification string-based to Notification.Name."
deprecated_function: "NSNotification.Name()"
replacement_function: "Notification.Name()"
languages: ["swift"]
deprecated_since: "Swift 3.0+"
---

# [Solution] Deprecated Function Migration: NSNotification to Notification.Name

The `NSNotification.Name(rawValue: "event")` has been deprecated in favor of `Notification.Name("event")`.

## Migration Guide

Notification.Name is type-safe and follows naming conventions

NSNotification.Name with rawValue is verbose. Notification.Name extension provides type-safe names.

## Before (Deprecated)

```swift
NotificationCenter.default.addObserver(
    self,
    selector: #selector(handle),
    name: NSNotification.Name("MyEvent"),
    object: nil
)
```

## After (Modern)

```swift
extension Notification.Name {
    static let myEvent = Notification.Name("MyEvent")
}

NotificationCenter.default.addObserver(
    self,
    selector: #selector(handle),
    name: .myEvent,
    object: nil
)
```

## Key Differences

- Notification.Name extension for type safety
- Less error-prone than raw strings
- Better IDE autocomplete
- Follows Swift naming conventions
