---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Trailing Accessory Error"
description: "Fix UICollectionLayoutListConfiguration section header trailing accessory configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Trailing Accessory Error

Section header trailing accessory errors occur when the accessory is not properly configured, when the accessory conflicts with the header content, or when the accessory does not match the design.

## Common Causes
- Accessory not configured
- Accessory conflicts with header content
- Accessory not matching design
- Accessory not updating with content changes

## How to Fix
1. Configure accessory properly
2. Ensure accessory complements header content
3. Match design specifications
4. Update accessory with content changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.accessories = [.outlineDisclosure(options: .init())]
header.contentConfiguration = content
```

## Examples
```swift
// Header with disclosure accessory:
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.accessories = [
    .outlineDisclosure(options: UIListContentConfiguration.OutlineDisclosureOptions.accessories.customView(
        UIListContentConfiguration.AccessoryView.customView(
            UIActivityIndicatorView(style: .medium)
        )
    ))
]
header.contentConfiguration = content
```
