---
title: "[Solution] SwiftUI @Environment Value Error"
description: "Fix SwiftUI @Environment property wrapper not reflecting expected values."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @Environment Value Error

@Environment values may not update when the environment changes if the property is not properly declared or if the view does not respond to environment changes.

## Common Causes
- Environment key not properly defined
- View hierarchy does not provide the environment value
- Property wrapper type does not match environment key
- View cached and not re-evaluated on change

## How to Fix
1. Use correct EnvironmentKey type
2. Ensure parent view provides the environment value
3. Verify property wrapper type matches key Value type
4. Use environmentObject for reference types

```swift
// Custom environment key:
struct ThemeKey: EnvironmentKey {
    static let defaultValue = "light"
}

extension EnvironmentValues {
    var theme: String {
        get { self[ThemeKey.self] }
        set { self[ThemeKey.self] = newValue }
    }
}

// Usage:
@Environment(\.theme) var theme
```

## Examples
```swift
// Environment-based theming:
struct ContentView: View {
    @Environment(\.colorScheme) var colorScheme

    var body: some View {
        Text("Hello")
            .foregroundColor(colorScheme == .dark ? .white : .black)
    }
}

// Provide environment value:
ContentView()
    .environment(\.theme, "dark")
```
