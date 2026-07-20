---
title: "[Solution] SwiftUI Animation Error — withAnimation & Context"
description: "Fix SwiftUI animation errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 113
---

SwiftUI animation errors occur when `withAnimation` context is misused, implicit animations conflict with explicit ones, or animation values aren't properly triggered.

## Common Causes

```swift
// withAnimation context issues
withAnimation {
    isExpanded.toggle()
    // Multiple state changes animate unexpectedly
}

// Implicit animation conflict
Text("Hello")
    .opacity(fadeIn ? 1 : 0)
    .animation(.easeIn, value: fadeIn)
    .animation(.spring(), value: isExpanded) // Conflicts
```

## How to Fix

**1. Use explicit animation blocks**

```swift
withAnimation(.spring(response: 0.3)) {
    isExpanded.toggle()
}
```

**2. Separate animation contexts**

```swift
VStack {
    HeaderView()
        .animation(.easeIn, value: fadeIn)
    ContentView()
        .animation(.spring(), value: isExpanded)
}
```

**3. Use animation modifiers properly**

```swift
Text("Hello")
    .opacity(fadeIn ? 1 : 0)
    .animation(.easeIn(duration: 0.3), value: fadeIn)
```

**4. Transaction-based animation**

```swift
Button("Toggle") {
    withTransaction(Transaction(animation: .spring())) {
        isExpanded.toggle()
    }
}
```

**5. Conditional animation**

```swift
Text("Hello")
    .offset(y: isExpanded ? 100 : 0)
    .animation(
        isExpanded ? .spring() : .easeOut(duration: 0.5),
        value: isExpanded
    )
```

## Examples

Complete animation pattern:
```swift
struct AnimatedView: View {
    @State private var show = false
    
    var body: some View {
        VStack {
            Circle()
                .fill(show ? .blue : .red)
                .frame(width: show ? 200 : 100)
            
            Button("Toggle") {
                withAnimation(.interpolatingSpring(
                    stiffness: 170,
                    damping: 15
                )) {
                    show.toggle()
                }
            }
        }
    }
}
```

## Related Errors

- [Gesture Error](/languages/swift/swiftui-gesture-error)
- [Binding Error](/languages/swift/swiftui-binding-error)
- [Observable Error](/languages/swift/swiftui-observable-error)
