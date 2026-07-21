---
title: "[Solution] Deprecated Function Migration: optional return to Result type"
description: "Migrate from deprecated optional returns to Result type for error reporting in Swift."
deprecated_function: "func doWork() -> T?"
replacement_function: "func doWork() -> Result<T, Error>"
languages: ["swift"]
deprecated_since: "Swift 5.0+"
---

# [Solution] Deprecated Function Migration: optional return to Result type

The `func doWork() -> T?` has been deprecated in favor of `func doWork() -> Result<T, Error>`.

## Migration Guide

Result type explicitly communicates success or failure with an error.

## Before (Deprecated)

```swift
func fetchData() -> Data? {
    guard let url = URL(string: apiEndpoint) else {
        return nil
    }
    guard let data = try? Data(contentsOf: url) else {
        return nil
    }
    return data
}
```

## After (Modern)

```swift
func fetchData() -> Result<Data, Error> {
    guard let url = URL(string: apiEndpoint) else {
        return .failure(AppError.invalidURL)
    }
    do {
        let data = try Data(contentsOf: url)
        return .success(data)
    } catch {
        return .failure(error)
    }
}

// Usage
switch fetchData() {
case .success(let data):
    process(data)
case .failure(let error):
    handleError(error)
}
```

## Key Differences

- Result type explicitly shows success/failure
- No need to check for nil
- Error information is preserved
- switch/case for pattern matching
