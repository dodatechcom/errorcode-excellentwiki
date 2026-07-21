---
title: "[Solution] UIKit UIStatusBarStyle Error"
description: "Fix UIStatusBarStyle configuration and appearance errors in iOS apps."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIStatusBarStyle Error

Status bar style errors occur when the view controller does not override preferredStatusBarStyle, when the navigation controller does not forward the request, or when Info.plist conflicts with code.

## Common Causes
- preferredStatusBarStyle not overridden in view controller
- Navigation bar overrides status bar style
- Info.plist UIStatusBarStyle conflicts with code
- UIViewControllerBasedStatusBarAppearance set incorrectly

## How to Fix
1. Override preferredStatusBarStyle in view controllers
2. Set UIViewControllerBasedStatusBarAppearance to YES in Info.plist
3. Call setNeedsStatusBarAppearanceUpdate after style change
4. Ensure navigation controller does not override child style

```swift
// Override status bar style:
override var preferredStatusBarStyle: UIStatusBarStyle {
    return .lightContent
}

// Update status bar:
setNeedsStatusBarAppearanceUpdate()
```

## Examples
```swift
// Status bar per view controller:
class DarkViewController: UIViewController {
    override var preferredStatusBarStyle: UIStatusBarStyle { .lightContent }
}

class LightViewController: UIViewController {
    override var preferredStatusBarStyle: UIStatusBarStyle { .darkContent }
}

// In UINavigationController:
class CustomNavCtrl: UINavigationController {
    override var childForStatusBarStyle: UIViewController? { topViewController }
}
```
