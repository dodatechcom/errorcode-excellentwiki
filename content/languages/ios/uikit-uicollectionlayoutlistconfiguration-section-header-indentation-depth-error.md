---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Indentation Depth Error"
description: "Fix UICollectionLayoutListConfiguration section header indentation depth configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Indentation Depth Error

Section header indentation depth errors occur when the depth is not properly configured, when the depth conflicts with the header content, or when the depth does not match the design specifications.

## Common Causes
- Indentation depth not configured
- Depth conflicts with header content
- Depth not matching design specs
- Depth not updating with content changes

## How to Fix
1. Configure indentation depth properly
2. Ensure depth complements header content
3. Match design specifications
4. Update depth with content changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.axesPreservingSuperviewLayoutMargins = .horizontal
cell.indentationLevel = 1
cell.indentationWidth = 20
```

## Examples
```swift
// Section with different indentation levels:
for (index, item) in items.enumerated() {
    let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
    cell.indentationLevel = item.level
    cell.indentationWidth = 20.0
}
```
