---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Safe Area Error"
description: "Fix UICollectionLayoutListConfiguration section header safe area configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Safe Area Error

Safe area errors occur when the header is not properly respecting the safe area, when the safe area insets are incorrect, or when the safe area conflicts with the header content.

## Common Causes
- Safe area not respected
- Insets incorrect
- Safe area conflicts with content
- Safe area not updating with rotation

## How to Fix
1. Respect safe area properly
2. Calculate correct insets
3. Ensure safe area does not conflict with content
4. Update safe area with rotation

```swift
header.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    header.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
    header.leadingAnchor.constraint(equalTo: view.leadingAnchor),
    header.trailingAnchor.constraint(equalTo: view.trailingAnchor)
])
```

## Examples
```swift
// Safe area aware header:
header.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor).isActive = true
header.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor).isActive = true
```
