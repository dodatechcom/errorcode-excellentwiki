---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Center Y Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide centerY constraint errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Center Y Error

Layout guide centerY errors occur when the centerY constraint is not properly configured, when the constraint conflicts with the header layout, or when the constraint does not match the design.

## Common Causes
- centerY constraint not configured
- Constraint conflicts with layout
- Constraint not matching design
- Constraint not updating with size changes

## How to Fix
1. Configure centerY constraint properly
2. Ensure constraint is compatible with layout
3. Match design specifications
4. Update constraint with size changes

```swift
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)
NSLayoutConstraint.activate([
    contentGuide.centerYAnchor.constraint(equalTo: header.centerYAnchor)
])
```

## Examples
```swift
// Center to superview
contentGuide.centerYAnchor.constraint(equalTo: header.centerYAnchor).isActive = true

// Center to another view
contentGuide.centerYAnchor.constraint(equalTo: label.centerYAnchor).isActive = true

// Center with offset
contentGuide.centerYAnchor.constraint(equalTo: header.centerYAnchor, constant: -10).isActive = true
```
