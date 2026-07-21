---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Safe Area Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide safe area constraint errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Safe Area Error

Layout guide safe area errors occur when the layout guide does not properly respect the safe area, when the safe area insets are incorrect, or when the safe area conflicts with the header content.

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
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)
NSLayoutConstraint.activate([
    contentGuide.topAnchor.constraint(equalTo: header.safeAreaLayoutGuide.topAnchor, constant: 8),
    contentGuide.leadingAnchor.constraint(equalTo: header.safeAreaLayoutGuide.leadingAnchor, constant: 16)
])
```

## Examples
```swift
// Safe area layout guide
NSLayoutConstraint.activate([
    contentGuide.topAnchor.constraint(equalTo: header.safeAreaLayoutGuide.topAnchor),
    contentGuide.bottomAnchor.constraint(equalTo: header.safeAreaLayoutGuide.bottomAnchor),
    contentGuide.leadingAnchor.constraint(equalTo: header.safeAreaLayoutGuide.leadingAnchor),
    contentGuide.trailingAnchor.constraint(equalTo: header.safeAreaLayoutGuide.trailingAnchor)
])
```
