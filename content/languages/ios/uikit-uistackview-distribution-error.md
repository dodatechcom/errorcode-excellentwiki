---
title: "[Solution] UIKit UIStackView Distribution Error"
description: "Fix UIStackView arrangement and distribution layout errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIStackView Distribution Error

Stack view distribution errors cause views to overlap, not appear, or have incorrect spacing when distribution is set incorrectly or arranged views have conflicting constraints.

## Common Causes
- Distribution setting incompatible with arranged subview sizes
- Arranged subviews have conflicting intrinsic content size
- Spacing too large for available space
- Arranged subview hidden but not removed from stack

## How to Fix
1. Match distribution to your layout needs
2. Set hugging and compression priorities correctly
3. Remove or hide arranged subviews properly
4. Test with different content sizes

```swift
// Stack view configuration:
let stackView = UIStackView()
stackView.axis = .horizontal
stackView.distribution = .fillEqually
stackView.spacing = 8
stackView.addArrangedSubview(label)
stackView.addArrangedSubview(button)
```

## Examples
```swift
// Distribution options:
stackView.distribution = .fill // Fill available space
stackView.distribution = .fillEqually // Equal widths
stackView.distribution = .fillProportionally // Proportional to intrinsic size
stackView.distribution = .equalSpacing // Equal spacing between views
stackView.distribution = .equalCentering // Equal center-to-center spacing

// Remove arranged subview properly:
stackView.removeArrangedSubview(view)
view.removeFromSuperview()
```
