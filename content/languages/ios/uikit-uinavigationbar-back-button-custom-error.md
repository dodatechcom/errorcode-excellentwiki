---
title: "[Solution] UIKit UINavigationBar Back Button Custom Error"
description: "Fix custom back button configuration and appearance errors in UINavigationBar."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UINavigationBar Back Button Custom Error

Custom back button errors occur when the back button image is not properly configured, when the back title is not hidden, or when the navigation bar appearance conflicts with the custom button.

## Common Causes
- Custom back button image not set
- Back button title not hidden when using custom image
- Navigation bar appearance overriding custom styling
- Back button action not properly wired

## How to Fix
1. Set custom back button image with appearance
2. Hide back title when using custom image
3. Configure navigation bar appearance consistently
4. Use custom back button item instead of default

```swift
// Custom back button:
let backButton = UIBarButtonItem()
backButton.title = ""
backButton.customView = UIImageView(image: UIImage(systemName: "chevron.left"))
navigationItem.leftBarButtonItem = backButton
navigationController?.navigationBar.topItem?.backButtonDisplayMode = .minimal
```

## Examples
```swift
// Back button with custom appearance:
let appearance = UINavigationBarAppearance()
appearance.setBackIndicatorImage(UIImage(systemName: "arrow.left"), transitionMaskImage: UIImage(systemName: "arrow.left"))
appearance.backgroundColor = .systemBackground

navigationController?.navigationBar.standardAppearance = appearance
navigationController?.navigationBar.scrollEdgeAppearance = appearance

// Hide back title:
if #available(iOS 14.0, *) {
    navigationItem.backButtonDisplayMode = .minimal
}
```
