---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Tap Action Error"
description: "Fix UICollectionLayoutListConfiguration section header tap action handling errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Tap Action Error

Section header tap action errors occur when the tap gesture is not properly configured, when the tap conflicts with the header display, or when the tap action is not triggered.

## Common Causes
- Tap gesture not configured on header
- Tap conflicts with header display
- Tap action not triggered
- Tap gesture conflicting with other gestures

## How to Fix
1. Configure tap gesture on header
2. Ensure tap does not conflict with display
3. Implement tap action handler
4. Test gesture conflicts

```swift
let headerTap = UITapGestureRecognizer(target: self, action: #selector(headerTapped(_:)))
header.addGestureRecognizer(headerTap)
header.isUserInteractionEnabled = true

@objc func headerTapped(_ gesture: UITapGestureRecognizer) {
    guard let section = gesture.view?.tag else { return }
    toggleSection(section)
}
```

## Examples
```swift
// Header with expand/collapse:
@objc func headerTapped(_ gesture: UITapGestureRecognizer) {
    guard let section = gesture.view?.tag else { return }
    withAnimation {
        expandedSections.toggle(section)
    }
}
```
