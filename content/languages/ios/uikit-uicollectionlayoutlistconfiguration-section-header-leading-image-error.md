---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Leading Image Error"
description: "Fix UICollectionLayoutListConfiguration section header leading image configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Leading Image Error

Section header leading image errors occur when the image is not properly configured, when the image conflicts with the header content, or when the image does not match the design.

## Common Causes
- Image not configured
- Image conflicts with header content
- Image not matching design
- Image not updating with content changes

## How to Fix
1. Configure image properly
2. Ensure image complements header content
3. Match design specifications
4. Update image with content changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.image = UIImage(systemName: "folder.fill")
content.imageProperties.tintColor = .systemBlue
header.contentConfiguration = content
```

## Examples
```swift
// Header with leading image:
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Recent"
content.image = UIImage(systemName: "clock")
content.imageProperties.cornerRadius = 4
content.imageToTextPadding = 8
header.contentConfiguration = content
```
