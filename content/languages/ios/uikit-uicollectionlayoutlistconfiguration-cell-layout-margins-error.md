---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Cell Layout Margins Error"
description: "Fix UICollectionLayoutListConfiguration cell layout margins configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Cell Layout Margins Error

Cell layout margins errors occur when the margins are not properly configured, when the margins conflict with the cell content, or when the margins do not match the design.

## Common Causes
- Margins not configured
- Margins conflict with cell content
- Margins not matching design
- Margins not updating with layout changes

## How to Fix
1. Configure margins properly
2. Ensure margins complement cell content
3. Match design specifications
4. Update margins with layout changes

```swift
var config = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
config.itemLayout = UICollectionLayoutListConfiguration.ItemLayout(separatorOptions: .init(top: 0, leading: 0, bottom: 0, trailing: 0))
```

## Examples
```swift
// Custom cell margins:
var content = UIListContentConfiguration.cell()
content.text = "Cell"
content.textToSecondaryTextVerticalPadding = 8
content.textToTextVerticalPadding = 4
cell.contentConfiguration = content
```
