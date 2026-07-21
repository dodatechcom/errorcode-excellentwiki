---
title: "[Solution] SwiftUI .scrollPositionModifier Error"
description: "Fix SwiftUI .scrollPosition modifier programmatic scroll position setting errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .scrollPositionModifier Error

ScrollPosition modifier errors occur when the position is not properly set programmatically, when the position does not match the content, or when the position does not update.

## Common Causes
- Position not set
- Position does not match content
- Position not updating
- Position not triggering

## How to Fix
1. Set position properly
2. Match position to content
3. Ensure position updates
4. Trigger position correctly

```swift
struct ContentView: View {
    @State private var scrollPosition: ScrollPosition = .init(idType: String.self)

    var body: some View {
        ScrollView {
            LazyVStack {
                ForEach(items) { item in
                    Text(item.name)
                        .id(item.id)
                }
            }
            .scrollPosition($scrollPosition)
        }
    }
}
```

## Examples
```swift
// Scroll to specific position
scrollPosition.scrollTo(id: "item-10", anchor: .top)

// Scroll to top
scrollPosition.scrollTo(id: items.first?.id, anchor: .top)

// Scroll to bottom
scrollPosition.scrollTo(id: items.last?.id, anchor: .bottom)
```
