---
title: "[Solution] Deprecated Function Migration: UIScreen.main to window scene"
description: "Migrate from deprecated UIScreen.main to scene-based approach."
deprecated_function: "UIScreen.main.bounds"
replacement_function: "UIWindowScene geometry"
languages: ["swift"]
deprecated_since: "iOS 13+"
---

# [Solution] Deprecated Function Migration: UIScreen.main to window scene

The `UIScreen.main.bounds` has been deprecated in favor of `UIWindowScene geometry`.

## Migration Guide

UIScreen.main is deprecated in iOS 16.

## Before (Deprecated)

```swift
let bounds = UIScreen.main.bounds
```

## After (Modern)

```swift
let scene = UIApplication.shared.connectedScenes.first as! UIWindowScene
let bounds = scene.screen.bounds
```

## Key Differences

- Use UIWindowScene instead
