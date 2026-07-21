---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Vertical Alignment Error"
description: "Fix UICollectionLayoutListConfiguration section header vertical alignment configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Vertical Alignment Error

Section header vertical alignment errors occur when the content is not properly aligned, when the alignment conflicts with the header layout, or when the alignment does not match the design.

## Common Causes
- Content not properly aligned
- Alignment conflicts with layout
- Alignment not matching design
- Alignment not updating with content changes

## How to Fix
1. Align content properly
2. Ensure alignment is compatible with layout
3. Match design specifications
4. Update alignment with content changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.textProperties.alignment = .natural
content.axesPreservingSuperviewLayoutMargins = .horizontal
header.contentConfiguration = content
```

## Examples
```swift
// Centered header content:
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.textProperties.alignment = .center
header.contentConfiguration = content

// Left-aligned with image:
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.image = UIImage(systemName: "folder")
content.textProperties.alignment = .natural
header.contentConfiguration = content
```
