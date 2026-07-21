---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Separator Style Error"
description: "Fix UICollectionLayoutListConfiguration separator style and inset errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Separator Style Error

Separator style errors occur when the separator is not visible, when the separator inset does not match the design, or when the separator style conflicts with the list appearance.

## Common Causes
- Separator not configured properly
- Separator inset not matching design
- Separator style conflicts with list appearance
- Separator not updating after layout changes

## How to Fix
1. Configure separator in list configuration
2. Set separator inset to match design
3. Ensure separator style is compatible with appearance
4. Update separator after layout changes

```swift
var config = UICollectionLayoutListConfiguration(appearance: .plain)
config.separatorConfiguration.color = .separator
config.separatorConfiguration.topSeparatorVisibility = .automatic
config.separatorConfiguration.bottomSeparatorVisibility = .automatic
```

## Examples
```swift
// Custom separator configuration:
var separatorConfig = UIListSeparatorConfiguration(listAppearance: .plain)
separatorConfig.color = .systemGray4
separatorConfig.topSeparatorVisibility = .hidden
separatorConfig.bottomSeparatorVisibility = .automatic
separatorConfig.bottomSeparatorInsets = NSDirectionalEdgeInsets(top: 0, leading: 16, bottom: 0, trailing: 0)

var config = UICollectionLayoutListConfiguration(appearance: .plain)
config.separatorConfiguration = separatorConfig
```
