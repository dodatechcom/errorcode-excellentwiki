---
title: "[Solution] SwiftUI .scrollPosition Anchor Error"
description: "Fix SwiftUI .scrollPosition modifier scroll position tracking errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .scrollPosition Anchor Error

ScrollPosition modifier errors occur when the position is not properly tracked, when the position does not update, or when the position does not match the visible content.

## Common Causes
- Position not tracked
- Position not updating
- Position does not match content
- Position not matching design

## How to Fix
1. Track position properly
2. Ensure position updates
3. Match position to content
4. Match design specifications

```swift
struct ContentView: View {
    @State private var scrollPosition: CGFloat = 0

    var body: some View {
        ScrollView {
            LazyVStack {
                ForEach(items) { item in
                    ItemRow(item: item)
                }
            }
            .scrollPosition($scrollPosition)
        }
    }
}
```

## Examples
```swift
// Track scroll position
.scrollPosition($scrollPosition)

// Scroll to position
.scrollPosition(id: $selectedItem)

// With anchor
.scrollPosition(id: $selectedItem, anchor: .top)

// Programmatic scroll
ScrollViewReader { proxy in
    Button("Scroll to top") {
        withAnimation {
            proxy.scrollTo(topID, anchor: .top)
        }
    }
}
```
