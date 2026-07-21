---
title: "[Solution] SwiftUI .scrollPosition ID Error"
description: "Fix SwiftUI .scrollPosition with id-based scroll tracking errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .scrollPosition ID Error

ScrollPosition ID errors occur when the id does not match any visible content, when the scroll does not reach the target, or when the position does not update.

## Common Causes
- ID does not match content
- Scroll does not reach target
- Position does not update
- ID not unique

## How to Fix
1. Ensure ID matches content
2. Scroll to target properly
3. Update position
4. Use unique IDs

```swift
struct ContentView: View {
    @State private var selectedID: String?

    var body: some View {
        ScrollViewReader { proxy in
            ScrollView {
                LazyVStack {
                    ForEach(items) { item in
                        Text(item.name)
                            .id(item.id)
                    }
                }
            }
            .scrollPosition(id: $selectedID)
        }
    }
}
```

## Examples
```swift
// Scroll to ID
.scrollPosition(id: $selectedID)

// Programmatic scroll
ScrollViewReader { proxy in
    Button("Go to Item 50") {
        withAnimation {
            proxy.scrollTo("item-50", anchor: .top)
        }
    }
}

// With anchor
.scrollPosition(id: $selectedID, anchor: .center)
```
