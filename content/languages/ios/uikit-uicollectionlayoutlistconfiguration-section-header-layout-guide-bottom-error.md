---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Bottom Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide bottom constraint errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Bottom Error

Layout guide bottom errors occur when the bottom constraint is not properly configured, when the constraint conflicts with the header layout, or when the constraint does not match the design.

## Common Causes
- Bottom constraint not configured
- Constraint conflicts with layout
- Constraint not matching design
- Constraint not updating with size changes

## How to Fix
1. Configure bottom constraint properly
2. Ensure constraint is compatible with layout
3. Match design specifications
4. Update constraint with size changes

```swift
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)
NSLayoutConstraint.activate([
    contentGuide.bottomAnchor.constraint(equalTo: header.bottomAnchor, constant: -8)
])
```

## Examples
```swift
// Bottom to superview
contentGuide.bottomAnchor.constraint(equalTo: header.bottomAnchor, constant: -8).isActive = true

// Bottom to another view
contentGuide.bottomAnchor.constraint(equalTo: label.topAnchor, constant: -8).isActive = true

// Bottom to layout guide
contentGuide.bottomAnchor.constraint(equalTo: header.safeAreaLayoutGuide.bottomAnchor, constant: -8).isActive = true
```
