---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Outline Disclosure Error"
description: "Fix UICollectionLayoutListConfiguration section header outline disclosure configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Outline Disclosure Error

Outline disclosure errors occur when the disclosure indicator is not properly configured, when the disclosure conflicts with the header content, or when the disclosure does not update with section state.

## Common Causes
- Disclosure indicator not configured
- Disclosure conflicts with header content
- Disclosure not visible
- Disclosure state not updating

## How to Fix
1. Configure outline disclosure on header
2. Ensure disclosure does not conflict with content
3. Verify disclosure visibility
4. Update disclosure state with section changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
header.contentConfiguration = content
header.accessories = [.outlineDisclosure(options: .init(style: .header))]
```

## Examples
```swift
// Outline disclosure with custom tint:
header.accessories = [
    .outlineDisclosure(options: .init(
        style: .header,
        tintColor: .systemBlue
    ))
]

// Manual disclosure update:
if isExpanded {
    header.accessories = [.outlineDisclosure(options: .init(style: .header, state: .on))]
} else {
    header.accessories = [.outlineDisclosure(options: .init(style: .header, state: .off))]
}
```
