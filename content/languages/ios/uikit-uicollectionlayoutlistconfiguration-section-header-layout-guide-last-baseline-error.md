---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Last Baseline Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide lastBaseline constraint errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Last Baseline Error

Layout guide lastBaseline errors occur when the lastBaseline constraint is not properly configured, when the constraint conflicts with the header layout, or when the constraint does not match the design.

## Common Causes
- lastBaseline constraint not configured
- Constraint conflicts with layout
- Constraint not matching design
- Constraint not updating with content changes

## How to Fix
1. Configure lastBaseline constraint properly
2. Ensure constraint is compatible with layout
3. Match design specifications
4. Update constraint with content changes

```swift
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)
NSLayoutConstraint.activate([
    contentGuide.lastBaselineAnchor.constraint(equalTo: header.lastBaselineAnchor)
])
```

## Examples
```swift
// Last baseline alignment
contentGuide.lastBaselineAnchor.constraint(equalTo: label.lastBaselineAnchor).isActive = true

// Last baseline with offset
contentGuide.lastBaselineAnchor.constraint(equalTo: label.lastBaselineAnchor, constant: -4).isActive = true
```
