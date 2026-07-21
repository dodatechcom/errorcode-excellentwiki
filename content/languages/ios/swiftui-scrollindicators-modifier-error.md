---
title: "[Solution] SwiftUI .scrollIndicators Modifier Error"
description: "Fix SwiftUI .scrollIndicators modifier scroll indicator display errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .scrollIndicators Modifier Error

ScrollIndicators modifier errors occur when the indicators are not properly configured, when the indicators conflict with the scroll content, or when the indicators do not match the design.

## Common Causes
- Indicators not configured
- Indicators conflict with content
- Indicators not matching design
- Indicators not updating with content

## How to Fix
1. Configure indicators properly
2. Ensure indicators do not conflict with content
3. Match design specifications
4. Update indicators with content

```swift
struct ContentView: View {
    var body: some View {
        ScrollView {
            Text("Content")
        }
        .scrollIndicators(.hidden)
    }
}
```

## Examples
```swift
// Show indicators
.scrollIndicators(.visible)

// Hide indicators
.scrollIndicators(.hidden)

// Automatic
.scrollIndicators(.automatic)
```
