---
title: "[Solution] SwiftUI Gesture Error — Priority & Conflicts"
description: "Fix SwiftUI gesture errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 112
---

SwiftUI gesture errors occur when gesture priorities conflict, simultaneous gestures aren't handled correctly, or gesture sequences produce unexpected behavior.

## Common Causes

```swift
// Gesture priority conflict
Text("Tap me")
    .onTapGesture { print("Tap 1") }
    .onTapGesture { print("Tap 2") } // Never fires

// Simultaneous gesture conflict
Text("Pinch")
    .gesture(
        MagnificationGesture()
            .simultaneously(with: RotationGesture())
    )
```

## How to Fix

**1. Use .simultaneousGesture for independent gestures**

```swift
Text("Both fire")
    .onTapGesture { print("Tap") }
    .simultaneousGesture(
        LongPressGesture()
            .onEnded { _ in print("Long press") }
    )
```

**2. Set gesture priority with .highPriorityGesture**

```swift
VStack {
    Text("Parent tap")
        .onTapGesture { print("Parent") }
}
.highPriorityGesture(
    TapGesture()
        .onEnded { print("Child high priority") }
)
```

**3. Handle gesture sequences**

```swift
struct MyGesture: Gesture {
    @State private var isTapped = false
    
    var body: some Gesture {
        TapGesture()
            .onEnded { isTapped.toggle() }
            .sequenced(before: LongPressGesture())
            .onEnded { value in
                switch value {
                case .first(true):
                    print("Long press started")
                case .second(true, let succeeded):
                    print("Long press \(succeeded ? "completed" : "cancelled")")
                default:
                    break
                }
            }
    }
}
```

**4. Exclusive gesture recognition**

```swift
Text("Exclusive")
    .gesture(
        TapGesture()
            .onEnded { print("Tap") }
            .exclusively(before: LongPressGesture())
    )
```

**5. Custom gesture with state**

```swift
struct DragGestureView: View {
    @GestureState private var offset = CGSize.zero
    
    var body: some View {
        Circle()
            .frame(width: 100, height: 100)
            .offset(offset)
            .gesture(
                DragGesture()
                    .updating($offset) { value, state, _ in
                        state = value.translation
                    }
                    .onEnded { value in
                        withAnimation { offset = .zero }
                    }
            )
    }
}
```

## Examples

Multi-touch gesture handling:
```swift
struct ContentView: View {
    @State private var scale: CGFloat = 1.0
    @State private var rotation: Angle = .zero
    
    var body: some View {
        Image(systemName: "star.fill")
            .font(.system(size: 100))
            .scaleEffect(scale)
            .rotationEffect(rotation)
            .gesture(
                MagnificationGesture()
                    .simultaneously(with: RotationGesture())
                    .onChanged { value in
                        scale = value.first ?? 1.0
                        rotation = value.second ?? .zero
                    }
            )
    }
}
```

## Related Errors

- [Animation Error](/languages/swift/swiftui-animation-error)
- [Binding Error](/languages/swift/swiftui-binding-error)
- [Preference Error](/languages/swift/swiftui-preference-error)
