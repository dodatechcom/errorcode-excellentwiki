---
title: "[Solution] Deprecated Function Migration: NotificationCenter to Combine"
description: "Migrate from deprecated NotificationCenter to Combine."
deprecated_function: "NotificationCenter.default.addObserver"
replacement_function: "NotificationCenter.default.publisher(for:)"
languages: ["swift"]
deprecated_since: "iOS 13+"
---

# [Solution] Deprecated Function Migration: NotificationCenter to Combine

The `NotificationCenter.default.addObserver` has been deprecated in favor of `NotificationCenter.default.publisher(for:)`.

## Migration Guide

Combine is more modern.

## Before (Deprecated)

```swift
NotificationCenter.default.addObserver(self, selector: #selector(handle), name: .myNotification, object: nil)
```

## After (Modern)

```swift
let cancellable = NotificationCenter.default.publisher(for: .myNotification)
    .sink { notification in
        self.handle(notification)
    }
```

## Key Differences

- Combine is more modern
