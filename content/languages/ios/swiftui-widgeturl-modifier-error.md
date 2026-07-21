---
title: "[Solution] SwiftUI .widgetURL Modifier Error"
description: "Fix SwiftUI .widgetURL modifier widget deep link URL errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .widgetURL Modifier Error

WidgetURL modifier errors occur when the URL is not properly configured, when the URL scheme is not registered, or when the URL does not match the design.

## Common Causes
- URL not configured
- URL scheme not registered
- URL not matching design
- URL not updating with content

## How to Fix
1. Configure URL properly
2. Register URL scheme
3. Match design specifications
4. Update URL with content

```swift
struct MyWidget: Widget {
    var body: some WidgetConfiguration {
        StaticConfiguration(kind: "com.app.widget", provider: Provider()) { entry in
            MyWidgetView(entry: entry)
                .widgetURL(URL(string: "myapp://home")!)
        }
    }
}
```

## Examples
```swift
// Deep link URL
.widgetURL(URL(string: "myapp://item/123")!)

// Web URL
.widgetURL(URL(string: "https://example.com")!)

// Conditional URL
.widgetURL(isPremium ? URL(string: "myapp://premium")! : URL(string: "myapp://free")!)
```
