---
title: "[Solution] Deprecated Function Migration: String(describing:) to string interpolation"
description: "Migrate from deprecated String(describing:) to string interpolation."
deprecated_function: "String(describing: value)"
replacement_function: '\(value)'
languages: ["swift"]
deprecated_since: "Swift 4.0+"
---

# [Solution] Deprecated Function Migration: String(describing:) to string interpolation

The `String(describing: value)` has been deprecated in favor of `\(value)`.

## Migration Guide

String interpolation is simpler.

## Before (Deprecated)

```swift
let s = String(describing: value)
```

## After (Modern)

```swift
let s = "\(value)"
```

## Key Differences

- String interpolation is simpler
