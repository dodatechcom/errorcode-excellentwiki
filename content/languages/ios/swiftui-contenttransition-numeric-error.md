---
title: "[Solution] SwiftUI .contentTransition Numeric Error"
description: "Fix SwiftUI .contentTransition numeric text animation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .contentTransition Numeric Error

ContentTransition numeric errors occur when the numeric transition is not properly animated, when the transition does not match the change, or when the transition does not update.

## Common Causes
- Transition not animated
- Transition does not match change
- Transition not updating
- Missing animation modifier

## How to Fix
1. Animate transition properly
2. Match transition to change
3. Update transition
4. Add animation modifier

```swift
struct ContentView: View {
    @State private var count = 0

    var body: some View {
        Button("Count: \(count)") { count += 1 }
            .contentTransition(.numericText())
            .animation(.easeInOut, value: count)
    }
}
```

## Examples
```swift
// Standard numeric transition
.contentTransition(.numericText())

// Countdown numeric
.contentTransition(.numericText(countsDown: true))

// Interpolate
.contentTransition(.interpolate)

// With animation
.animation(.spring(), value: count)
.contentTransition(.numericText())
```
