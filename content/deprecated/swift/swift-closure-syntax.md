---
title: "[Solution] Deprecated Function Migration: verbose closures to trailing closure syntax"
description: "Migrate from verbose closures to trailing closure and shorthand."
deprecated_function: "sort({ (a, b) -> Bool in a < b })"
replacement_function: "sort { $0 < $1 }"
languages: ["swift"]
deprecated_since: "Swift 2.0+"
---

# [Solution] Deprecated Function Migration: verbose closures to trailing closure syntax

The `sort({ (a, b) -> Bool in a < b })` has been deprecated in favor of `sort { $0 < $1 }`.

## Migration Guide

Trailing closure syntax is more concise

Trailing closure and shorthand arguments make closures concise.

## Before (Deprecated)

```swift
let sorted = names.sort({ (a: String, b: String) -> Bool in
    return a < b
})
```

## After (Modern)

```swift
let sorted = names.sort { $0 < $1 }

UIView.animate(withDuration: 0.3) {
    view.alpha = 1
}
```

## Key Differences

- Trailing closure moves {} outside ()
- $0, $1 for shorthand arguments
- Type inference removes annotations
