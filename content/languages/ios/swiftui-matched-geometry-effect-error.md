---
title: "[Solution] SwiftUI Matched Geometry Effect Error"
description: "Fix SwiftUI matchedGeometryEffect transition errors between views."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI Matched Geometry Effect Error

matchedGeometryEffect fails when the namespace is not shared between source and destination, when IDs conflict, or when the animation timing is incorrect.

## Common Causes
- Namespace not shared between views
- Duplicate geometry IDs in the view hierarchy
- Animation not triggered during transition
- Views not in the same view hierarchy

## How to Fix
1. Share @Namespace between source and destination views
2. Use unique IDs for each geometry effect
3. Trigger animation with withAnimation block
4. Ensure both views are in the same view tree

```swift
// Shared namespace:
@Namespace private var animation

// Source:
Circle()
    .matchedGeometryEffect(id: "circle", in: animation)

// Destination:
Rectangle()
    .matchedGeometryEffect(id: "circle", in: animation)
```

## Examples
```swift
// Tab transition with matchedGeometryEffect:
struct TabView: View {
    @Namespace private var animation
    @State private var selectedTab = 0

    var body: some View {
        VStack {
            HStack {
                ForEach(0..<3) { index in
                    Button("Tab \(index)") { selectedTab = index }
                        .overlay(
                            selectedTab == index ? Capsule()
                                .matchedGeometryEffect(id: "tab", in: animation)
                                .frame(height: 3) : nil, alignment: .bottom
                        )
                }
            }
        }
    }
}
```
