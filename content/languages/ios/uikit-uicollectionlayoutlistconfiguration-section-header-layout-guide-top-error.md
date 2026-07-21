---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Top Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide top constraint errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Top Error

Layout guide top errors occur when the top constraint is not properly configured, when the constraint conflicts with the header layout, or when the constraint does not match the design.

## Common Causes
- Top constraint not configured
- Constraint conflicts with layout
- Constraint not matching design
- Constraint not updating with size changes

## How to Fix
1. Configure top constraint properly
2. Ensure constraint is compatible with layout
3. Match design specifications
4. Update constraint with size changes

```swift
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)
NSLayoutConstraint.activate([
    contentGuide.topAnchor.constraint(equalTo: header.topAnchor, constant: 8)
])
```

## Examples
```swift
// Top to superview
contentGuide.topAnchor.constraint(equalTo: header.topAnchor, constant: 8).isActive = true

// Top to another view
contentGuide.topAnchor.constraint(equalTo: icon.bottomAnchor, constant: 8).isActive = true

// Top to layout guide
contentGuide.topAnchor.constraint(equalTo: header.safeAreaLayoutGuide.topAnchor, constant: 8).isActive = true
```
