---
title: "[Solution] Swift UserDefaults Error — Type Mismatch & Suite"
description: "Fix Swift UserDefaults errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 119
---

`UserDefaults` errors occur when type mismatches happen during retrieval, suite names are invalid, or keys don't exist.

## Common Causes

```swift
// Type mismatch on retrieval
let count = UserDefaults.standard.integer(forKey: "count") // Returns 0 if missing
let name = UserDefaults.standard.string(forKey: "name") // Returns nil if missing

// Invalid suite name
let suite = UserDefaults(suiteName: "invalid..suite")
```

## How to Fix

**1. Safe type casting**

```swift
if let name = UserDefaults.standard.string(forKey: "name") {
    print(name)
} else {
    print("Name not found")
}
```

**2. Use AppStorage for SwiftUI**

```swift
struct SettingsView: View {
    @AppStorage("volume") private var volume = 50
    @AppStorage("theme") private var theme = "light"
    
    var body: some View {
        Form {
            Slider(value: $volume, in: 0...100)
        }
    }
}
```

**3. Custom UserDefaults wrapper**

```swift
@propertyWrapper
struct UserDefault<T> {
    let key: String
    let defaultValue: T
    
    var wrappedValue: T {
        get { UserDefaults.standard.object(forKey: key) as? T ?? defaultValue }
        set { UserDefaults.standard.set(newValue, forKey: key) }
    }
}

struct Settings {
    @UserDefault(key: "volume", defaultValue: 50)
    static var volume: Int
}
```

**4. Handle suite not found**

```swift
guard let defaults = UserDefaults(suiteName: "group.com.app.shared") else {
    print("Suite not available")
    return
}
```

**5. Observe UserDefaults changes**

```swift
let observer = UserDefaults.standard.observe(\.volume) { defaults, change in
    print("Volume changed: \(change.newValue ?? 0)")
}
```

## Examples

Complete UserDefaults setup:
```swift
enum Storage {
    @UserDefault(key: "first_launch", defaultValue: true)
    static var isFirstLaunch: Bool
    
    @UserDefault(key: "last_sync", defaultValue: Date.distantPast)
    static var lastSyncDate: Date
    
    @UserDefault(key: "user_token", defaultValue: nil)
    static var userToken: String?
}

// Reset
Storage.isFirstLaunch = false
```

## Related Errors

- [Property List Error](/languages/swift/swift-property-list-error)
- [JSONDecoder Error](/languages/swift/swift-jsondecoder-error)
- [Codable Custom Error](/languages/swift/swift-codable-custom-error)
