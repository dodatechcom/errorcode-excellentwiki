---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Indentation Error"
description: "Fix UICollectionLayoutListConfiguration section header indentation configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Indentation Error

Section header indentation errors occur when the header is not properly indented, when the indentation conflicts with the section insets, or when the indentation does not match the design.

## Common Causes
- Header not properly indented
- Indentation conflicts with section insets
- Indentation not matching design
- Indentation not updating with layout changes

## How to Fix
1. Set proper header indentation
2. Ensure indentation does not conflict with insets
3. Match design specifications
4. Update indentation with layout changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.axesPreservingSuperviewLayoutMargins = .horizontal
content.directionalLayoutMargins = NSDirectionalEdgeInsets(top: 0, leading: 16, bottom: 0, trailing: 16)
header.contentConfiguration = content
```

## Examples
```swift
// Header with custom indentation:
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.textProperties.font = .preferredFont(forTextStyle: .headline)
content.directionalLayoutMargins = NSDirectionalEdgeInsets(top: 8, leading: 20, bottom: 8, trailing: 20)
header.contentConfiguration = content
```
