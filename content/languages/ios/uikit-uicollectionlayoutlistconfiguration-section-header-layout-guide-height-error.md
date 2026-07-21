---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Height Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide height constraint errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Height Error

Layout guide height errors occur when the height constraint is not properly configured, when the constraint conflicts with the header layout, or when the constraint does not match the design.

## Common Causes
- Height constraint not configured
- Constraint conflicts with layout
- Constraint not matching design
- Constraint not updating with size changes

## How to Fix
1. Configure height constraint properly
2. Ensure constraint is compatible with layout
3. Match design specifications
4. Update constraint with size changes

```swift
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)
NSLayoutConstraint.activate([
    contentGuide.heightAnchor.constraint(equalToConstant: 60)
])
```

## Examples
```swift
// Fixed height
contentGuide.heightAnchor.constraint(equalToConstant: 60).isActive = true

// Proportional height
contentGuide.heightAnchor.constraint(equalTo: header.heightAnchor, multiplier: 0.5).isActive = true

// Min/max height
contentGuide.heightAnchor.constraint(greaterThanOrEqualToConstant: 44).isActive = true
contentGuide.heightAnchor.constraint(lessThanOrEqualToConstant: 100).isActive = true
```
