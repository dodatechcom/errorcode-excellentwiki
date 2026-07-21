---
title: "[Solution] Deprecated Function Migration: DispatchQoS to TaskPriority"
description: "Migrate from deprecated DispatchQoS to TaskPriority."
deprecated_function: "DispatchQueue.global(qos: .userInitiated)"
replacement_function: "Task(priority: .userInitiated)"
languages: ["swift"]
deprecated_since: "Swift 5.5+"
---

# [Solution] Deprecated Function Migration: DispatchQoS to TaskPriority

The `DispatchQueue.global(qos: .userInitiated)` has been deprecated in favor of `Task(priority: .userInitiated)`.

## Migration Guide

TaskPriority is simpler.

## Before (Deprecated)

```swift
DispatchQueue.global(qos: .userInitiated).async {
    await fetchData()
}
```

## After (Modern)

```swift
Task(priority: .userInitiated) {
    await fetchData()
}
```

## Key Differences

- TaskPriority is simpler
