---
title: "[Solution] SwiftUI .contentMarginsDisabled Modifier Error"
description: "Fix SwiftUI .contentMarginsDisabled modifier content margin override errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .contentMarginsDisabled Modifier Error

ContentMarginsDisabled modifier errors occur when the margins are not properly disabled, when the disabling conflicts with the layout, or when the disabling does not match the design.

## Common Causes
- Margins not disabled
- Disabling conflicts with layout
- Disabling not matching design
- Disabling not updating with content

## How to Fix
1. Disable margins properly
2. Ensure disabling is compatible with layout
3. Match design specifications
4. Update disabling with content

```swift
struct ContentView: View {
    var body: some View {
        List {
            Text("Item")
        }
        .contentMarginsDisabled()
    }
}
```

## Examples
```swift
// Disable all margins
.contentMarginsDisabled()

// Disable specific margins
.contentMarginsDisabled([.horizontal])

// Conditional disable
.contentMarginsDisabled(isCompact ? [] : [.all])
```
