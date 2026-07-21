---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Accessibility Configuration Error"
description: "Fix UICollectionLayoutListConfiguration section header accessibility configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Accessibility Configuration Error

Section header accessibility configuration errors occur when the accessibility properties are not properly set, when the properties conflict with the header content, or when the properties do not match the design.

## Common Causes
- Accessibility properties not set
- Properties conflict with header content
- Properties not matching design
- Properties not updating with content changes

## How to Fix
1. Set accessibility properties properly
2. Ensure properties complement header content
3. Match design specifications
4. Update properties with content changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
header.isAccessibilityElement = true
header.accessibilityLabel = "Section header"
header.accessibilityTraits = .header
header.contentConfiguration = content
```

## Examples
```swift
// Accessible header:
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.secondaryText = "5 items"
header.accessibilityLabel = "Section header, 5 items"
header.accessibilityHint = "Double tap to expand"
header.accessibilityTraits = .header
header.contentConfiguration = content
```
