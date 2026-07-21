---
title: "[Solution] SwiftUI Gesture State Reset Error"
description: "Fix SwiftUI gesture state not resetting properly between interactions."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI Gesture State Reset Error

Gesture state variables may not reset between gesture interactions if @GestureState is not used or if the state management is incorrect.

## Common Causes
- Using @State instead of @GestureState for gesture values
- Gesture state not reset in gestureEnded callback
- Multiple gestures interfering with each other
- Animation blocking state reset

## How to Fix
1. Use @GestureState for gesture-driven values
2. Implement gestureEnded to reset state
3. Isolate gesture states with separate variables
4. Use .updating and .onEnded modifiers properly

```swift
// Correct gesture state:
@GestureState private var dragOffset = CGSize.zero

let dragGesture = DragGesture()
    .updating($dragOffset) { value, state, _ in
        state = value.translation
    }
    .onEnded { _ in
        // State automatically resets
    }

Text("Drag me").offset(dragOffset)
```

## Examples
```swift
// Gesture with state management:
struct ContentView: View {
    @State private var offset = CGSize.zero
    @GestureState private var gestureOffset = CGSize.zero

    var body: some View {
        let drag = DragGesture()
            .updating($gestureOffset) { value, _, _ in
                offset = CGSize(width: value.translation.width + offset.width,
                                height: value.translation.height + offset.height)
            }
            .onEnded { value in
                offset = .zero
            }
        Circle().frame(width: 100, height: 100).offset(offset).gesture(drag)
    }
}
```
