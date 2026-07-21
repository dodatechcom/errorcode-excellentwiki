---
title: "[Solution] UIKit UIImpactFeedbackGenerator Error"
description: "Fix UIImpactFeedbackGenerator haptic feedback configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIImpactFeedbackGenerator Error

Haptic feedback fails when the feedback type is not supported on the device, when the generator is not properly prepared, or when feedback is triggered too rapidly.

## Common Causes
- Feedback type not supported on older devices
- Generator not prepared before impact
- Multiple rapid impacts without preparation
- Generator deallocated before feedback

## How to Fix
1. Check device support before using haptics
2. Prepare the generator before triggering
3. Allow time between rapid feedback triggers
4. Keep a strong reference to the generator

```swift
// Haptic feedback:
let feedback = UIImpactFeedbackGenerator(style: .medium)
feedback.prepare()
feedback.impactOccurred()

// With custom intensity:
feedback.impactOccurred(intensity: 0.7)
```

## Examples
```swift
// Selection feedback:
let selection = UISelectionFeedbackGenerator()
selection.prepare()
selection.selectionChanged()

// Notification feedback:
let notification = UINotificationFeedbackGenerator()
notification.prepare()
notification.notificationOccurred(.success)

// Impact with intensity:
let impact = UIImpactFeedbackGenerator(style: .heavy)
impact.prepare()
impact.impactOccurred(intensity: 1.0)
```
