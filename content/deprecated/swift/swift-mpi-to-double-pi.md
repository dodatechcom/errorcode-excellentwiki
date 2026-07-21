---
title: "[Solution] Deprecated Function Migration: M_PI to Double.pi"
description: "Migrate from deprecated M_PI constant to Double.pi in Swift."
deprecated_function: "M_PI"
replacement_function: "Double.pi"
languages: ["swift"]
deprecated_since: "Swift 3.0+"
---

# [Solution] Deprecated Function Migration: M_PI to Double.pi

The `M_PI` has been deprecated in favor of `Double.pi`.

## Migration Guide

Double.pi is type-safe and follows Swift naming conventions.

## Before (Deprecated)

```swift
let radius = 5.0
let area = M_PI * radius * radius
let circumference = 2 * M_PI * radius
```

## After (Modern)

```swift
let radius = 5.0
let area = Double.pi * radius * radius
let circumference = 2 * Double.pi * radius

// Also available as Float.pi
let floatPi: Float = .pi
```

## Key Differences

- Double.pi replaces M_PI
- Float.pi for Float type
- Type-safe -- no type casting needed
- Follows Swift naming conventions
