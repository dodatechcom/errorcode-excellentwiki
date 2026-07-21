---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Disclosure Error"
description: "Fix UICollectionLayoutListConfiguration section header disclosure indicator configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Disclosure Error

Section header disclosure errors occur when the disclosure indicator is not properly configured, when the indicator conflicts with the header content, or when the indicator is not visible.

## Common Causes
- Disclosure indicator not configured
- Indicator conflicts with header content
- Indicator not visible
- Indicator not updating with state changes

## How to Fix
1. Configure disclosure indicator on header
2. Ensure indicator does not conflict with content
3. Verify indicator visibility
4. Update indicator with state changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section Title"
header.contentConfiguration = content
header.accessories = [.outlineDisclosure(options: .init(style: .header))]
```

## Examples
```swift
// Header with custom disclosure:
header.accessories = [
    .outlineDisclosure(options: .init(
        style: .header,
        tintColor: .systemBlue
    ))
]
```
