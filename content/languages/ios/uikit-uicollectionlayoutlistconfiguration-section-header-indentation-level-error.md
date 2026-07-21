---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Indentation Level Error"
description: "Fix UICollectionLayoutListConfiguration section header indentation level configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Indentation Level Error

Section header indentation level errors occur when the indentation level is not properly set, when the indentation conflicts with the header content, or when the indentation does not match the design.

## Common Causes
- Indentation level not set
- Indentation conflicts with content
- Indentation not matching design
- Indentation not updating with layout changes

## How to Fix
1. Set proper indentation level
2. Ensure indentation complements content
3. Match design specifications
4. Update indentation with layout changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.directionalLayoutMargins = NSDirectionalEdgeInsets(top: 0, leading: 32, bottom: 0, trailing: 0)
header.contentConfiguration = content
```

## Examples
```swift
// Nested sections with indentation:
struct SectionItem: Identifiable {
    let id = UUID()
    let title: String
    let level: Int
}

// In cell configuration:
let indent = CGFloat(item.level) * 20
cell.indentationLevel = item.level
cell.indentationWidth = 20
```
