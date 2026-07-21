---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Leading Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide leading constraint errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Leading Error

Layout guide leading errors occur when the leading constraint is not properly configured, when the constraint conflicts with the header layout, or when the constraint does not match the design.

## Common Causes
- Leading constraint not configured
- Constraint conflicts with layout
- Constraint not matching design
- Constraint not updating with size changes

## How to Fix
1. Configure leading constraint properly
2. Ensure constraint is compatible with layout
3. Match design specifications
4. Update constraint with size changes

```swift
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)
NSLayoutConstraint.activate([
    contentGuide.leadingAnchor.constraint(equalTo: header.leadingAnchor, constant: 16)
])
```

## Examples
```swift
// Leading to superview
contentGuide.leadingAnchor.constraint(equalTo: header.leadingAnchor, constant: 16).isActive = true

// Leading to another view
contentGuide.leadingAnchor.constraint(equalTo: icon.trailingAnchor, constant: 8).isActive = true

// Leading to layout guide
contentGuide.leadingAnchor.constraint(equalTo: header.safeAreaLayoutGuide.leadingAnchor, constant: 16).isActive = true
```
