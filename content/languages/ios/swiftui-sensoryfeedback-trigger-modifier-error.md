---
title: "[Solution] SwiftUI .sensoryFeedback Trigger Modifier Error"
description: "Fix SwiftUI .sensoryFeedback trigger-based haptic feedback configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .sensoryFeedback Trigger Modifier Error

SensoryFeedback trigger errors occur when the trigger does not properly fire the feedback, when the feedback type does not match the action, or when the feedback does not update.

## Common Causes
- Trigger does not fire
- Feedback type mismatch
- Feedback not updating
- Feedback not matching action

## How to Fix
1. Ensure trigger fires properly
2. Match feedback type to action
3. Update feedback
4. Match feedback to action

```swift
struct ContentView: View {
    @State private var didSave = false

    var body: some View {
        Button("Save") { didSave = true }
            .sensoryFeedback(.success, trigger: didSave)
    }
}
```

## Examples
```swift
// Success on save
.sensoryFeedback(.success, trigger: didSave)

// Warning on error
.sensoryFeedback(.warning, trigger: hasError)

// Selection on change
.sensoryFeedback(.selection, trigger: selectedItem)

// Impact on delete
.sensoryFeedback(.impact(weight: .heavy), trigger: didDelete)
```
