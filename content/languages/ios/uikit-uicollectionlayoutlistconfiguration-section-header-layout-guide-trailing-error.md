---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Trailing Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide trailing constraint errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Trailing Error

Layout guide trailing errors occur when the trailing constraint is not properly configured, when the constraint conflicts with the header layout, or when the constraint does not match the design.

## Common Causes
- Trailing constraint not configured
- Constraint conflicts with layout
- Constraint not matching design
- Constraint not updating with size changes

## How to Fix
1. Configure trailing constraint properly
2. Ensure constraint is compatible with layout
3. Match design specifications
4. Update constraint with size changes

```swift
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)
NSLayoutConstraint.activate([
    contentGuide.trailingAnchor.constraint(equalTo: header.trailingAnchor, constant: -16)
])
```

## Examples
```swift
// Trailing to superview
contentGuide.trailingAnchor.constraint(equalTo: header.trailingAnchor, constant: -16).isActive = true

// Trailing to another view
contentGuide.trailingAnchor.constraint(equalTo: label.leadingAnchor, constant: -8).isActive = true

// Trailing to layout guide
contentGuide.trailingAnchor.constraint(equalTo: header.safeAreaLayoutGuide.trailingAnchor, constant: -16).isActive = true
```
