---
title: "[Solution] App Groups Container Access Error"
description: "Fix App Groups shared container access errors between iOS app and extensions."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# App Groups Container Access Error

App Groups container access fails when the group identifier does not match, the entitlement is not configured, or the group is not enabled in the developer portal.

## Common Causes
- App Groups entitlement not added to both targets
- Group identifier mismatch between app and extension
- App Group not enabled in developer portal
- Container URL returns nil

## How to Fix
1. Add App Groups capability to both targets
2. Ensure group identifier matches exactly
3. Enable App Group in developer portal
4. Verify container URL is not nil before using

```swift
// Access shared container:
if let sharedContainer = FileManager.default.containerURL(forSecurityApplicationGroupIdentifier: "group.com.app.shared") {
    let fileURL = sharedContainer.appendingPathComponent("data.json")
    // Use sharedContainer for file operations
}
```

## Examples
```swift
// Shared data between app and widget:
struct SharedDefaults {
    static let shared = UserDefaults(suiteName: "group.com.app.shared")

    static func save(_ value: String, forKey key: String) {
        shared?.set(value, forKey: key)
        shared?.synchronize()
    }

    static func load(forKey key: String) -> String? {
        return shared?.string(forKey: key)
    }
}
```
