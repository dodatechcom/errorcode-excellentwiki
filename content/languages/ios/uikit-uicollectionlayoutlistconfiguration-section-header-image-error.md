---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Image Error"
description: "Fix UICollectionLayoutListConfiguration section header image configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Image Error

Section header image errors occur when the image is not properly loaded, when the image conflicts with the header text, or when the image is not properly sized.

## Common Causes
- Image not loaded from bundle or system
- Image conflicts with header text
- Image not properly sized
- Image tint color not matching design

## How to Fix
1. Load image from correct source
2. Ensure image does not overlap text
3. Set proper image size
4. Configure image tint color

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.image = UIImage(systemName: "folder.fill")
content.imageProperties.tintColor = .systemBlue
header.contentConfiguration = content
```

## Examples
```swift
// Header with custom image:
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Favorites"
content.image = UIImage(systemName: "heart.fill")
content.imageProperties.tintColor = .systemRed
content.imageProperties.cornerRadius = 4
cell.contentConfiguration = content
```
