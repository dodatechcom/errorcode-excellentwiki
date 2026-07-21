---
title: "[Solution] SwiftUI .task Modifier Error"
description: "Fix SwiftUI .task modifier async work lifecycle issues in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .task Modifier Error

The .task modifier may cancel work unexpectedly when the view disappears, or may not start when the view first appears due to lifecycle timing.

## Common Causes
- Task cancelled when view disappears during async work
- Task not restarted after cancellation
- Multiple tasks running concurrently
- Task not properly handling cancellation

## How to Fix
1. Handle Task cancellation with isCancelled check
2. Use .task(id:) to restart when dependencies change
3. Structure async work to support cancellation
4. Use async let for concurrent tasks

```swift
// Task with cancellation handling:
.task {
    do {
        let data = try await fetchData()
        self.data = data
    } catch is CancellationError {
        // Handle cancellation
    } catch {
        self.error = error
    }
}
```

## Examples
```swift
// Task with dependency:
.task(id: searchText) {
    guard !searchText.isEmpty else { return }
    try? await Task.sleep(for: .milliseconds(300)) // Debounce
    results = await searchService.search(searchText)
}

// Multiple concurrent tasks:
.async let users = fetchUsers()
.async let posts = fetchPosts()
let (fetchedUsers, fetchedPosts) = try await (users, posts)
```
