---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Priority Error"
description: "Fix UICollectionLayoutListConfiguration section header layout priority configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Priority Error

Layout priority errors occur when the priority is not properly configured, when the priority conflicts with the header layout, or when the priority does not match the design.

## Common Causes
- Priority not configured
- Priority conflicts with layout
- Priority not matching design
- Priority not updating with size changes

## How to Fix
1. Configure priority properly
2. Ensure priority is compatible with layout
3. Match design specifications
4. Update priority with size changes

```swift
header.translatesAutoresizingMaskIntoConstraints = false
let heightConstraint = header.heightAnchor.constraint(equalToConstant: 60)
heightConstraint.priority = .defaultHigh
heightConstraint.isActive = true
```

## Examples
```swift
// High priority constraint:
let heightConstraint = header.heightAnchor.constraint(greaterThanOrEqualToConstant: 44)
heightConstraint.priority = UILayoutPriority(999)

// Low priority constraint:
let heightConstraint = header.heightAnchor.constraint(equalToConstant: 60)
heightConstraint.priority = UILayoutPriority(250)
```
