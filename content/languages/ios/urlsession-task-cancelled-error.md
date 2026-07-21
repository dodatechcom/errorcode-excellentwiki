---
title: "[Solution] URLSession Task Cancelled Error"
description: "Fix URLSession task cancelled errors during network requests in iOS apps."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# URLSession Task Cancelled Error

Cancelled errors occur when a URLSessionTask is cancelled before completion or when the session is invalidated.

## Common Causes
- Task cancelled explicitly with .cancel()
- Session invalidated while tasks are running
- View controller deallocated before request completes
- App backgrounded during active download

## How to Fix
1. Check for .cancelled error code before handling other errors
2. Keep strong references to tasks until completion
3. Use weak self in completion handlers
4. Manage session lifecycle properly

```swift
// Handle cancellation:
let task = session.dataTask(with: url) { data, response, error in
    if let error = error as? URLError, error.code == .cancelled {
        print("Request was cancelled")
        return
    }
    // Handle other cases
}
task.resume()
```

## Examples
```swift
// Cancellation-aware networking:
class NetworkManager {
    private var currentTask: URLSessionDataTask?

    func fetchData(from url: URL) {
        currentTask?.cancel()
        currentTask = URLSession.shared.dataTask(with: url) { [weak self] data, _, error in
            guard let self = self else { return }
            if let error = error as? URLError, error.code == .cancelled { return }
            // Process data
        }
        currentTask?.resume()
    }
}
```
