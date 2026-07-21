---
title: "[Solution] SwiftUI .containerBackground Modifier Error"
description: "Fix SwiftUI .containerBackground modifier widget container background errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .containerBackground Modifier Error

ContainerBackground modifier errors occur when the background is not properly configured, when the background conflicts with the content, or when the background does not match the design.

## Common Causes
- Background not configured
- Background conflicts with content
- Background not matching design
- Background not updating with content

## How to Fix
1. Configure background properly
2. Ensure background does not conflict with content
3. Match design specifications
4. Update background with content

```swift
struct MyWidget: Widget {
    var body: some WidgetConfiguration {
        StaticConfiguration(kind: "com.app.widget", provider: Provider()) { entry in
            MyWidgetView(entry: entry)
                .containerBackground(for: .widget) {
                    Color.blue
                }
        }
    }
}
```

## Examples
```swift
// Gradient background
.containerBackground(for: .widget) {
    LinearGradient(colors: [.blue, .purple], startPoint: .topLeading, endPoint: .bottomTrailing)
}

// Image background
.containerBackground(for: .widget) {
    Image("background")
        .resizable()
        .scaledToFill()
}

// Clear background
.containerBackground(for: .widget) {
    Color.clear
}
```
