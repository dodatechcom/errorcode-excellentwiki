---
title: "[Solution] SwiftUI MatchedGeometryEffect Namespace Missing"
description: "Fix SwiftUI matchedGeometryEffect namespace not found error in view transitions."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI MatchedGeometryEffect Namespace Missing

Namespace is not found when @Namespace is not declared in the view using matchedGeometryEffect or when it is not shared between source and destination views.

## Common Causes
- @Namespace not declared in the view
- Namespace not shared between views
- Namespace declared in child instead of parent
- Duplicate IDs across different namespaces

## How to Fix
1. Declare @Namespace in the common ancestor view
2. Pass namespace to child views via environment or parameter
3. Use unique IDs within each namespace
4. Ensure source and destination share the same namespace

```swift
struct ParentView: View {
    @Namespace private var animation

    var body: some View {
        ChildView(namespace: animation)
    }
}
```

## Examples
```swift
struct ChildView: View {
    var animation: Namespace.ID
    @State private var expanded = false

    var body: some View {
        if expanded {
            Rectangle().matchedGeometryEffect(id: "box", in: animation)
        } else {
            Circle().matchedGeometryEffect(id: "box", in: animation)
        }
    }
}
```
