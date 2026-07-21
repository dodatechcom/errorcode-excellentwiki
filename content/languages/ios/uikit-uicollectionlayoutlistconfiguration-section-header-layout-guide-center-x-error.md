---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Center X Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide centerX constraint errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Center X Error

Layout guide centerX errors occur when the centerX constraint is not properly configured, when the constraint conflicts with the header layout, or when the constraint does not match the design.

## Common Causes
- centerX constraint not configured
- Constraint conflicts with layout
- Constraint not matching design
- Constraint not updating with size changes

## How to Fix
1. Configure centerX constraint properly
2. Ensure constraint is compatible with layout
3. Match design specifications
4. Update constraint with size changes

```swift
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)
NSLayoutConstraint.activate([
    contentGuide.centerXAnchor.constraint(equalTo: header.centerXAnchor)
])
```

## Examples
```swift
// Center to superview
contentGuide.centerXAnchor.constraint(equalTo: header.centerXAnchor).isActive = true

// Center to another view
contentGuide.centerXAnchor.constraint(equalTo: icon.centerXAnchor).isActive = true

// Center with offset
contentGuide.centerXAnchor.constraint(equalTo: header.centerXAnchor, constant: 10).isActive = true
```
