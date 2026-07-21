---
title: "[Solution] SwiftUI @AppStorage Custom Default Error"
description: "Fix SwiftUI @AppStorage custom default value configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @AppStorage Custom Default Error

AppStorage custom default errors occur when the default value is not properly set, when the default does not match the type, or when the default does not persist.

## Common Causes
- Default value not set
- Default does not match type
- Default does not persist
- Storage not shared

## How to Fix
1. Set default value properly
2. Match type correctly
3. Ensure persistence
4. Share storage if needed

```swift
struct SettingsView: View {
    @AppStorage("theme") private var theme = "light"
    @AppStorage("fontSize") private var fontSize = 16.0
    @AppStorage("notifications") private var notifications = true

    var body: some View {
        Form {
            Picker("Theme", selection: $theme) {
                Text("Light").tag("light")
                Text("Dark").tag("dark")
            }
        }
    }
}
```

## Examples
```swift
// String default
@AppStorage("theme") private var theme = "light"

// Double default
@AppStorage("score") private var score = 0.0

// Bool default
@AppStorage("isOn") private var isOn = false

// Data default
@AppStorage("data") private var data = Data()
```
