---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Distribution Error"
description: "Fix UICollectionLayoutListConfiguration section header layout distribution configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Distribution Error

Layout distribution errors occur when the distribution is not properly configured, when the distribution conflicts with the header layout, or when the distribution does not match the design.

## Common Causes
- Distribution not configured
- Distribution conflicts with layout
- Distribution not matching design
- Distribution not updating with content changes

## How to Fix
1. Configure distribution properly
2. Ensure distribution complements layout
3. Match design specifications
4. Update distribution with content changes

```swift
header.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    header.leadingAnchor.constraint(equalTo: view.leadingAnchor),
    header.trailingAnchor.constraint(equalTo: view.trailingAnchor)
])
```

## Examples
```swift
// Equal distribution:
let stackView = UIStackView(arrangedSubviews: [label1, label2, label3])
stackView.distribution = .fillEqually
stackView.spacing = 8

// Proportional distribution:
stackView.distribution = .fillProportionally
```
