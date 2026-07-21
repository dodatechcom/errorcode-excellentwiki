---
title: "[Solution] Deprecated Function Migration: DispatchQueue.main.async to @MainActor"
description: "Migrate from deprecated DispatchQueue.main.async to @MainActor."
deprecated_function: "DispatchQueue.main.async { }"
replacement_function: "@MainActor func update()"
languages: ["swift"]
deprecated_since: "Swift 5.5+"
---

# [Solution] Deprecated Function Migration: DispatchQueue.main.async to @MainActor

The `DispatchQueue.main.async { }` has been deprecated in favor of `@MainActor func update()`.

## Migration Guide

@MainActor ensures main thread.

## Before (Deprecated)

```swift
DispatchQueue.main.async {
    self.updateUI()
}
```

## After (Modern)

```swift
@MainActor
func updateUI() {
    // already on main thread
}
```

## Key Differences

- @MainActor ensures main thread
