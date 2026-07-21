---
title: "[Solution] SwiftUI .handWidgetShortcut Modifier Error"
description: "Fix SwiftUI .handWidgetShortcut modifier widget shortcut errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .handWidgetShortcut Modifier Error

WidgetShortcut modifier errors occur when the shortcut is not properly configured, when the shortcut conflicts with the widget, or when the shortcut does not match the design.

## Common Causes
- Shortcut not configured
- Shortcut conflicts with widget
- Shortcut not matching design
- Shortcut not updating with content

## How to Fix
1. Configure shortcut properly
2. Ensure shortcut is compatible with widget
3. Match design specifications
4. Update shortcut with content

```swift
struct MyWidget: Widget {
    var body: some WidgetConfiguration {
        StaticConfiguration(kind: "com.app.widget", provider: Provider()) { entry in
            MyWidgetView(entry: entry)
                .handWidgetShortcut(.custom("action"))
        }
    }
}
```

## Examples
```swift
// Standard shortcuts
.handWidgetShortcut(.playMedia)
.handWidgetShortcut(.search)
.handWidgetShortcut(.settings)

// Custom shortcuts
.handWidgetShortcut(.custom("myAction"))
```
