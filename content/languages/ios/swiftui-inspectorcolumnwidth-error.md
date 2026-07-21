---
title: "[Solution] SwiftUI .inspectorColumnWidth Error"
description: "Fix SwiftUI inspector column width configuration for sidebar and inspector layouts."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .inspectorColumnWidth Error

Inspector column width errors occur when the width range is invalid, when the ideal width exceeds available space, or when the column width conflicts with the navigation split view configuration.

## Common Causes
- Minimum width greater than ideal width
- Width range exceeding screen bounds
- Conflict with NavigationSplitView column widths
- Inspector width not updating on rotation

## How to Fix
1. Ensure min is less than or equal to ideal
2. Keep widths within screen bounds
3. Coordinate with navigation split view widths
4. Test width changes on device rotation

```swift
NavigationSplitView {
    List(items, selection: $selected) { item in
        Text(item.name)
    }
    .navigationSplitViewColumnWidth(min: 200, ideal: 300)
} detail: {
    DetailView(item: selected)
}
```

## Examples
```swift
// Navigation split view with column widths:
NavigationSplitView(columnVisibility: $columnVisibility) {
    SidebarView()
        .navigationSplitViewColumnWidth(min: 150, ideal: 200, max: 300)
} content: {
    ContentView()
        .navigationSplitViewColumnWidth(min: 200, ideal: 300)
} detail: {
    DetailView()
}
```
