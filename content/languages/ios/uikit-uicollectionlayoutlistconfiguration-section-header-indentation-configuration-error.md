---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Indentation Configuration Error"
description: "Fix UICollectionLayoutListConfiguration section header indentation configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Indentation Configuration Error

Section header indentation configuration errors occur when the indentation is not properly set, when the indentation conflicts with the header content, or when the indentation does not match the design.

## Common Causes
- Indentation not set
- Indentation conflicts with header content
- Indentation not matching design
- Indentation not updating with layout changes

## How to Fix
1. Set indentation properly
2. Ensure indentation complements header content
3. Match design specifications
4. Update indentation with layout changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.axesPreservingSuperviewLayoutMargins = .horizontal
content.directionalLayoutMargins = NSDirectionalEdgeInsets(top: 0, leading: 16, bottom: 0, trailing: 0)
header.contentConfiguration = content
```

## Examples
```swift
// Indented header:
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.image = UIImage(systemName: "folder")
content.imageToTextPadding = 8
content.directionalLayoutMargins = NSDirectionalEdgeInsets(top: 8, leading: 20, bottom: 8, trailing: 16)
header.contentConfiguration = content
```
