---
title: "[Solution] SwiftUI @Namespace Animation Error"
description: "Fix SwiftUI @Namespace matchedGeometryEffect animation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @Namespace Animation Error

Namespace animation errors occur when the namespace is not properly shared, when the animation does not match, or when the animation does not trigger.

## Common Causes
- Namespace not shared
- Animation does not match
- Animation does not trigger
- Animation not matching design

## How to Fix
1. Share namespace properly
2. Ensure animation matches
3. Trigger animation correctly
4. Match design specifications

```swift
struct ContentView: View {
    @Namespace var animation
    @State private var isExpanded = false

    var body: some View {
        if isExpanded {
            RoundedRectangle(cornerRadius: 20)
                .matchedGeometryEffect(id: "shape", in: animation)
        } else {
            Circle()
                .matchedGeometryEffect(id: "shape", in: animation)
        }
    }
}
```

## Examples
```swift
// Tab bar animation:
@Namespace var animation

TabView(selection: $selectedTab) {
    HomeView()
        .tabItem {
            Label("Home", systemImage: "house")
                .matchedGeometryEffect(id: "tab", in: animation)
        }
        .tag(0)
}

// List to detail animation:
matchedGeometryEffect(id: item.id, in: animation)
```
