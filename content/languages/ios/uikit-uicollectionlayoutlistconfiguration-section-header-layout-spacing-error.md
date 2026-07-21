---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Spacing Error"
description: "Fix UICollectionLayoutListConfiguration section header layout spacing configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Spacing Error

Layout spacing errors occur when the spacing is not properly configured, when the spacing conflicts with the header content, or when the spacing does not match the design.

## Common Causes
- Spacing not configured
- Spacing conflicts with content
- Spacing not matching design
- Spacing not updating with content changes

## How to Fix
1. Configure spacing properly
2. Ensure spacing complements content
3. Match design specifications
4. Update spacing with content changes

```swift
let stackView = UIStackView(arrangedSubviews: [imageView, titleLabel])
stackView.spacing = 8
stackView.alignment = .center
header.addSubview(stackView)
```

## Examples
```swift
// Custom spacing:
stackView.spacing = 12
stackView.layoutMargins = UIEdgeInsets(top: 8, left: 16, bottom: 8, right: 16)
stackView.isLayoutMarginsRelativeArrangement = true

// Dynamic spacing:
stackView.spacing = 8
stackView.setCustomSpacing(16, after: imageView)
```
