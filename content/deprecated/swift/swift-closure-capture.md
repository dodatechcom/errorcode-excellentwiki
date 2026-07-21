---
title: "[Solution] Deprecated Function Migration: strong reference capture to weak/unowned"
description: "Migrate from deprecated strong capture to weak/unowned."
deprecated_function: "[self] in"
replacement_function: "[weak self] in"
languages: ["swift"]
deprecated_since: "Swift 4.2+"
---

# [Solution] Deprecated Function Migration: strong reference capture to weak/unowned

The `[self] in` has been deprecated in favor of `[weak self] in`.

## Migration Guide

Weak capture prevents retain cycles.

## Before (Deprecated)

```swift
completion = { [self] in
    self.update()
}
```

## After (Modern)

```swift
completion = { [weak self] in
    self?.update()
}
```

## Key Differences

- Weak capture prevents retain cycles
