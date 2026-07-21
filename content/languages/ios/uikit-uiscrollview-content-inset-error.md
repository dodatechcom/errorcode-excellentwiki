---
title: "[Solution] UIKit UIScrollView Content Inset Error"
description: "Fix UIScrollView content inset adjustment errors in iOS apps."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIScrollView Content Inset Error

Content insets conflict when automatic content inset adjustment is enabled, when safe areas are not properly accounted for, or when custom insets override system insets.

## Common Causes
- Automatic content inset adjustment conflicts with manual insets
- Safe area insets not accounted for in content calculation
- Navigation bar or tab bar hiding not reflected
- contentInsetAdjustmentBehavior set incorrectly

## How to Fix
1. Check contentInsetAdjustmentBehavior setting
2. Account for safe area in manual inset calculations
3. Update insets when navigation bar visibility changes
4. Use additionalSafeAreaInsets for custom view controllers

```swift
// Configure scroll view insets:
scrollView.contentInsetAdjustmentBehavior = .automatic
scrollView.contentInset = UIEdgeInsets(top: 0, left: 0, bottom: 80, right: 0)
scrollView.verticalScrollIndicatorInsets = UIEdgeInsets(top: 0, left: 0, bottom: 80, right: 0)
```

## Examples
```swift
// Table view with custom insets:
class ViewController: UITableViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.contentInsetAdjustmentBehavior = .never
        tableView.contentInset = UIEdgeInsets(top: 200, left: 0, bottom: 0, right: 0)
        tableView.verticalScrollIndicatorInsets = UIEdgeInsets(top: 200, left: 0, bottom: 0, right: 0)
    }
}
```
