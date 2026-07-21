---
title: "[Solution] UIKit UITabBarController Badge Error"
description: "Fix UITab bar badge value display and positioning errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UITabBarController Badge Error

Tab bar badges fail to display when the badge value is set before the tab bar controller is loaded, when the badge is hidden by the system, or when the badge is positioned incorrectly.

## Common Causes
- Badge value set before tab bar is in hierarchy
- System badges conflicting with custom badges
- Badge not visible due to tab bar style
- Badge positioning affected by large content size

## How to Fix
1. Set badge value after tab bar is loaded
2. Use custom badge views for more control
3. Check badge appears correctly with different accessibility settings
4. Update badge on viewDidAppear

```swift
// Set badge value:
tabBarController?.tabBar.items?[1].badgeValue = "3"
tabBarController?.tabBar.items?[1].badgeColor = .systemRed

// Remove badge:
tabBarController?.tabBar.items?[1].badgeValue = nil
```

## Examples
```swift
// Custom badge view:
extension UITabBar {
    func setBadge(_ count: Int, at index: Int) {
        guard let items = items, index < items.count else { return }
        items[index].badgeValue = count > 0 ? "\(count)" : nil
    }
}

// Badge with colors:
tabBarItem.badgeValue = "5"
tabBarItem.badgeColor = .systemRed
```
