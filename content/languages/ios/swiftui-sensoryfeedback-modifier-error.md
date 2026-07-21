---
title: "[Solution] SwiftUI .sensoryFeedback Modifier Error"
description: "Fix SwiftUI .sensoryFeedback modifier haptic feedback errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .sensoryFeedback Modifier Error

SensoryFeedback modifier errors occur when the feedback is not properly triggered, when the feedback type is incorrect, or when the feedback does not match the design.

## Common Causes
- Feedback not triggered
- Feedback type incorrect
- Feedback not matching design
- Feedback not updating with content

## How to Fix
1. Trigger feedback properly
2. Use correct feedback type
3. Match design specifications
4. Update feedback with content

```swift
struct ContentView: View {
    @State private var count = 0

    var body: some View {
        Button("Count: \(count)") { count += 1 }
            .sensoryFeedback(.selection, trigger: count)
    }
}
```

## Examples
```swift
// Selection feedback
.sensoryFeedback(.selection, trigger: selected)

// Impact feedback
.sensoryFeedback(.impact(weight: .heavy), trigger: impact)

// Success feedback
.sensoryFeedback(.success, trigger: success)

// Custom feedback
.sensoryFeedback(.warning, trigger: warning)
```
