---
title: "[Solution] UIKit UINavigationBar Standard Appearance Error"
description: "Fix UINavigationBar standard appearance configuration conflicts in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UINavigationBar Standard Appearance Error

Standard appearance errors occur when the appearance conflicts with scroll edge appearance, when the background configuration is not properly set, or when the appearance is not applied to the correct navigation bar.

## Common Causes
- Standard and scroll edge appearances conflicting
- Background effect not properly configured
- Appearance not applied to correct navigation bar
- Appearance reset during lifecycle events

## How to Fix
1. Configure standard and scroll edge appearances consistently
2. Set background effect and color properly
3. Apply appearance to the correct navigation bar instance
4. Reapply appearance after view lifecycle events

```swift
let appearance = UINavigationBarAppearance()
appearance.configureWithOpaqueBackground()
appearance.backgroundColor = .systemBackground
appearance.titleTextAttributes = [.foregroundColor: UIColor.label]
appearance.largeTitleTextAttributes = [.foregroundColor: UIColor.label]

navigationController?.navigationBar.standardAppearance = appearance
navigationController?.navigationBar.scrollEdgeAppearance = appearance
```

## Examples
```swift
// Custom navigation bar appearance:
let navBarAppearance = UINavigationBarAppearance()
navBarAppearance.configureWithTransparentBackground()
navBarAppearance.titleTextAttributes = [.foregroundColor: UIColor.white]
navBarAppearance.largeTitleTextAttributes = [.foregroundColor: UIColor.white, .font: UIFont.systemFont(ofSize: 34, weight: .bold)]

UINavigationBar.appearance().standardAppearance = navBarAppearance
UINavigationBar.appearance().scrollEdgeAppearance = navBarAppearance
```
