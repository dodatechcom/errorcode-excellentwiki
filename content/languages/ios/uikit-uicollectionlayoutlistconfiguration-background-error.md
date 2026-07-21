---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Background Error"
description: "Fix UICollectionLayoutListConfiguration background appearance configuration errors."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Background Error

Background configuration errors occur when the background color conflicts with the cell background, when the background is not properly applied, or when the background does not update with theme changes.

## Common Causes
- Background color conflicts with cell color
- Background not updating with theme
- Background applied to wrong configuration
- Background effect not properly configured

## How to Fix
1. Set background color that complements cell color
2. Update background with theme changes
3. Apply background to correct configuration
4. Use system background colors for compatibility

```swift
var config = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
var background = UIBackgroundConfiguration.listGroupedHeaderFooter()
background.backgroundColor = .secondarySystemGroupedBackground
collectionView.backgroundColor = .systemGroupedBackground
```

## Examples
```swift
// Custom background configuration:
var backgroundConfig = UIBackgroundConfiguration.listGroupedCell()
backgroundConfig.backgroundColor = .systemBackground
backgroundConfig.strokeColor = .separator
backgroundConfig.strokeWidth = 0.5
backgroundConfig.cornerRadius = 10

var content = UIListContentConfiguration.subtitleCell()
cell.backgroundConfiguration = backgroundConfig
```
