---
title: "[Solution] SwiftUI @Environment Values Custom Key Error"
description: "Fix SwiftUI @EnvironmentValues custom environment key and value errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @Environment Values Custom Key Error

Custom environment key errors occur when the key does not conform to EnvironmentKey, when the default value is not set, or when the value does not update across views.

## Common Causes
- Key does not conform to EnvironmentKey
- Default value not set
- Value not updating
- Access path incorrect

## How to Fix
1. Conform key to EnvironmentKey
2. Set default value
3. Ensure value updates
4. Use correct access path

```swift
struct AppThemeKey: EnvironmentKey {
    static let defaultValue = "light"
}

extension EnvironmentValues {
    var appTheme: String {
        get { self[AppThemeKey.self] }
        set { self[AppThemeKey.self] = newValue }
    }
}

struct ContentView: View {
    @Environment(\.appTheme) var theme

    var body: some View {
        Text("Theme: \(theme)")
    }
}
```

## Examples
```swift
// Environment key with custom type
struct AccentColorKey: EnvironmentKey {
    static let defaultValue = Color.blue
}

// Environment action key
struct DismissActionKey: EnvironmentKey {
    static let defaultValue = DismissAction {}
}

// Environment values extension
extension EnvironmentValues {
    var isPremium: Bool {
        get { self[IsPremiumKey.self] }
        set { self[IsPremiumKey.self] = newValue }
    }
}
```
