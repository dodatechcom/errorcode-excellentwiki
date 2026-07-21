---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Opacity Error"
description: "Fix UICollectionLayoutListConfiguration section header opacity configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Opacity Error

Opacity errors occur when the opacity is not properly configured, when the opacity conflicts with the header content, or when the opacity does not match the design.

## Common Causes
- Opacity not configured
- Opacity conflicts with header content
- Opacity not matching design
- Opacity not updating with state changes

## How to Fix
1. Configure opacity properly
2. Ensure opacity complements header content
3. Match design specifications
4. Update opacity with state changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
header.alpha = 0.8
header.contentConfiguration = content
```

## Examples
```swift
// Header with animated opacity:
UIView.animate(withDuration: 0.3) {
    header.alpha = 0.5
}

// Header with full opacity:
header.alpha = 1.0
```
