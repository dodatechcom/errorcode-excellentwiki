---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide First Baseline Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide firstBaseline constraint errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide First Baseline Error

Layout guide firstBaseline errors occur when the firstBaseline constraint is not properly configured, when the constraint conflicts with the header layout, or when the constraint does not match the design.

## Common Causes
- firstBaseline constraint not configured
- Constraint conflicts with layout
- Constraint not matching design
- Constraint not updating with content changes

## How to Fix
1. Configure firstBaseline constraint properly
2. Ensure constraint is compatible with layout
3. Match design specifications
4. Update constraint with content changes

```swift
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)
NSLayoutConstraint.activate([
    contentGuide.firstBaselineAnchor.constraint(equalTo: header.firstBaselineAnchor)
])
```

## Examples
```swift
// First baseline alignment
contentGuide.firstBaselineAnchor.constraint(equalTo: label.firstBaselineAnchor).isActive = true

// First baseline with offset
contentGuide.firstBaselineAnchor.constraint(equalTo: label.firstBaselineAnchor, constant: 4).isActive = true
```
