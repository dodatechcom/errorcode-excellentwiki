---
title: "[Solution] Deprecated Function Migration: GCD DispatchQueue to Swift concurrency"
description: "Migrate from deprecated GCD patterns to Swift async/await concurrency."
deprecated_function: "DispatchQueue.global().async"
replacement_function: "Task { }"
languages: ["swift"]
deprecated_since: "Swift 5.5+"
---

# [Solution] Deprecated Function Migration: GCD DispatchQueue to Swift concurrency

The `DispatchQueue.global().async` has been deprecated in favor of `Task { }`.

## Migration Guide

Swift concurrency provides structured concurrency with better readability and safety.

## Before (Deprecated)

```swift
DispatchQueue.global().async {
    let data = self.fetchData()
    DispatchQueue.main.async {
        self.updateUI(with: data)
    }
}
```

## After (Modern)

```swift
Task {
    let data = await fetchData()
    await MainActor.run {
        updateUI(with: data)
    }
}

// Or with async/await directly
func loadData() async {
    let data = await fetchData()
    updateUI(with: data)
}
```

## Key Differences

- Task creates structured concurrency
- await pauses until async operation completes
- @MainActor ensures UI updates on main thread
