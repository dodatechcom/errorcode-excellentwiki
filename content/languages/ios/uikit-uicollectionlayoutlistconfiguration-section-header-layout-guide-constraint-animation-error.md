---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Animation Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide constraint animation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Animation Error

Layout guide constraint animation errors occur when the animation is not properly configured, when the animation conflicts with the constraint changes, or when the animation does not match the design.

## Common Causes
- Animation not configured
- Animation conflicts with constraints
- Animation not matching design
- Animation not updating with content changes

## How to Fix
1. Configure animation properly
2. Ensure animation is compatible with constraints
3. Match design specifications
4. Update animation with content changes

```swift
UIView.animate(withDuration: 0.3) {
    self.headerConstraint?.constant = 80
    self.view.layoutIfNeeded()
}
```

## Examples
```swift
// Animate constraint changes
UIView.animate(withDuration: 0.3, delay: 0, options: .curveEaseInOut) {
    self.headerHeightConstraint?.constant = self.isExpanded ? 120 : 60
    self.view.layoutIfNeeded()
} completion: { _ in
    // Animation completed
}

// Spring animation
UIView.animate(withDuration: 0.5, delay: 0, usingSpringWithDamping: 0.5, initialSpringVelocity: 0.5) {
    self.headerConstraint?.constant = 100
    self.view.layoutIfNeeded()
}
```
