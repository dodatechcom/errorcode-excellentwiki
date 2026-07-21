---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Width Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide width constraint errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Width Error

Layout guide width errors occur when the width constraint is not properly configured, when the constraint conflicts with the header layout, or when the constraint does not match the design.

## Common Causes
- Width constraint not configured
- Constraint conflicts with layout
- Constraint not matching design
- Constraint not updating with size changes

## How to Fix
1. Configure width constraint properly
2. Ensure constraint is compatible with layout
3. Match design specifications
4. Update constraint with size changes

```swift
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)
NSLayoutConstraint.activate([
    contentGuide.widthAnchor.constraint(equalToConstant: 200)
])
```

## Examples
```swift
// Fixed width
contentGuide.widthAnchor.constraint(equalToConstant: 200).isActive = true

// Proportional width
contentGuide.widthAnchor.constraint(equalTo: header.widthAnchor, multiplier: 0.8).isActive = true

// Min/max width
contentGuide.widthAnchor.constraint(greaterThanOrEqualToConstant: 100).isActive = true
contentGuide.widthAnchor.constraint(lessThanOrEqualToConstant: 300).isActive = true
```
