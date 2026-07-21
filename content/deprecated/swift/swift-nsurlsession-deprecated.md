---
title: "[Solution] Deprecated Function Migration: old NSURLSession delegate to async/await"
description: "Migrate from deprecated NSURLSession delegate to async/await."
deprecated_function: "URLSession.shared.dataTask"
replacement_function: "URLSession.shared.data(for:)"
languages: ["swift"]
deprecated_since: "iOS 15+"
---

# [Solution] Deprecated Function Migration: old NSURLSession delegate to async/await

The `URLSession.shared.dataTask` has been deprecated in favor of `URLSession.shared.data(for:)`.

## Migration Guide

async/await is cleaner.

## Before (Deprecated)

```swift
let task = URLSession.shared.dataTask(with: url) {
    data, response, error in
}
task.resume()
```

## After (Modern)

```swift
let (data, response) = try await URLSession.shared.data(from: url)
```

## Key Differences

- async/await is much cleaner
