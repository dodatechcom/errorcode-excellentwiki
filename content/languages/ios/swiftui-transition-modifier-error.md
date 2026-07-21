---
title: "[Solution] SwiftUI .transition Modifier Error"
description: "Fix SwiftUI .transition modifier view insertion and removal animation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .transition Modifier Error

Transition modifier errors occur when the transition is not properly configured, when the transition does not trigger, or when the transition does not match the design.

## Common Causes
- Transition not configured
- Transition not triggering
- Transition not matching design
- Transition not updating

## How to Fix
1. Configure transition properly
2. Ensure transition triggers
3. Match design specifications
4. Update transition

```swift
struct ContentView: View {
    @State private var showDetail = false

    var body: some View {
        VStack {
            Button("Toggle") { showDetail.toggle() }
            if showDetail {
                Text("Detail")
                    .transition(.slide)
            }
        }
        .animation(.easeInOut, value: showDetail)
    }
}
```

## Examples
```swift
// Built-in transitions
.transition(.slide)
.transition(.opacity)
.transition(.scale)

// Asymmetric transition
.transition(.asymmetric(
    insertion: .slide.combined(with: .opacity),
    removal: .scale.combined(with: .opacity)
))

// Custom transition
.transition(.modifier(
    active: { $0.offset(x: 100).opacity(0) },
    identity: { $0.offset(x: 0).opacity(1) }
))
```
