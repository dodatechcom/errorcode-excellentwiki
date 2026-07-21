---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Configuration Error"
description: "Fix UICollectionLayoutListConfiguration section header configuration and setup errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Configuration Error

Section header configuration errors occur when the header is not properly set up, when the configuration conflicts with the list appearance, or when the header does not display correctly.

## Common Causes
- Header not properly configured
- Configuration conflicts with list appearance
- Header not displaying
- Configuration not matching design

## How to Fix
1. Set up header configuration properly
2. Ensure configuration is compatible with list
3. Verify header display
4. Match configuration to design

```swift
var config = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
config.headerMode = .supplementary
config.headerTopPadding = 16

let layout = UICollectionViewCompositionalLayout.list(using: config)
collectionView.collectionViewLayout = layout
```

## Examples
```swift
// Full header configuration:
var config = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
config.headerMode = .supplementary
config.headerTopPadding = 0
config.separatorConfiguration.color = .separator
config.separatorConfiguration.topSeparatorVisibility = .automatic
config.separatorConfiguration.bottomSeparatorVisibility = .automatic
```
