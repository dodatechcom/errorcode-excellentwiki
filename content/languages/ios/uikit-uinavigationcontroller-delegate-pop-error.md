---
title: "[Solution] UIKit UINavigationController Delegate Pop Error"
description: "Fix UINavigationController delegate pop gesture recognizer errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UINavigationController Delegate Pop Error

Pop gesture errors occur when the delegate method returns false, preventing the interactive back gesture, or when the gesture recognizer conflicts with other interactive elements.

## Common Causes
- Delegate returns false for shouldPopViewController
- Pop gesture conflicts with scroll view gestures
- Navigation controller delegate not set
- Pop gesture recognizer not properly configured

## How to Fix
1. Implement navigationController(_:shouldPop:by:) correctly
2. Handle gesture conflicts with scroll views
3. Set navigation controller delegate
4. Configure gesture recognizer priority

```swift
func navigationController(_ navigationController: UINavigationController, shouldPop viewController: UIViewController, by popGestureRecognizer: Bool) -> Bool {
    if popGestureRecognizer {
        // Handle interactive back gesture
        return true
    }
    return true
}
```

## Examples
```swift
// Interactive pop with custom logic:
func navigationController(_ navigationController: UINavigationController, shouldPop viewController: UIViewController, by popGestureRecognizer: Bool) -> Bool {
    if popGestureRecognizer, let vc = viewController as? EditableViewController, vc.hasUnsavedChanges {
        showDiscardChangesAlert()
        return false
    }
    return true
}
```
