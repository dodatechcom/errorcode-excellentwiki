---
title: "[Solution] SwiftUI .sensoryFeedback Trigger Error"
description: "Fix SwiftUI .sensoryFeedback modifier trigger-based haptic feedback errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .sensoryFeedback Trigger Error

SensoryFeedback trigger errors occur when the trigger does not properly fire, when the feedback type does not match the interaction, or when the feedback does not update.

## Common Causes
- Trigger does not fire
- Feedback type mismatch
- Feedback not updating
- Trigger not matching content

## How to Fix
1. Ensure trigger fires properly
2. Match feedback type to interaction
3. Update feedback
4. Match trigger to content

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
// Selection feedback on change
.sensoryFeedback(.selection, trigger: selectedItem)

// Impact on action
.sensoryFeedback(.impact(weight: .heavy), trigger: performAction)

// Success on completion
.sensoryFeedback(.success, trigger: isComplete)

// Warning on error
.sensoryFeedback(.warning, trigger: hasError)
```
