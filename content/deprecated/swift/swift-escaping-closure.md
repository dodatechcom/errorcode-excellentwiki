---
title: "[Solution] Deprecated Function Migration: @escaping with manual management to async"
description: "Migrate from deprecated @escaping closure patterns to async."
deprecated_function: "@escaping closure"
replacement_function: "async functions"
languages: ["swift"]
deprecated_since: "Swift 5.5+"
---

# [Solution] Deprecated Function Migration: @escaping with manual management to async

The `@escaping closure` has been deprecated in favor of `async functions`.

## Migration Guide

async/await reduces need for @escaping.

## Before (Deprecated)

```swift
func fetchData(completion: @escaping (Data) -> Void) {
    URLSession.shared.dataTask(with: url) { data, _, _ in
        completion(data!)
    }.resume()
}
```

## After (Modern)

```swift
func fetchData() async throws -> Data {
    let (data, _) = try await URLSession.shared.data(from: url)
    return data
}
```

## Key Differences

- async/await replaces most @escaping
