---
title: "[Solution] UIKit UIContextMenu Interaction Configuration Preview Size Calculation Error"
description: "Fix UIContextMenuInteraction preview size calculation and preferredContentSize errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Configuration Preview Size Calculation Error

Preview size calculation errors occur when the size is not properly calculated, when the size conflicts with the available space, or when the size does not match the content.

## Common Causes
- Size not calculated correctly
- Size conflicts with available space
- Size not matching content
- Size not updating with content changes

## How to Fix
1. Calculate size based on content
2. Ensure size fits within available space
3. Match size to content requirements
4. Update size with content changes

```swift
let preview: UIContextMenuContentPreviewProvider = {
    let vc = DetailViewController()
    vc.preferredContentSize = CGSize(width: 250, height: 200)
    return vc
}
```

## Examples
```swift
// Dynamic preview size:
let preview: UIContextMenuContentPreviewProvider = { [weak self] in
    guard let self = self else { return UIViewController() }
    let vc = ItemPreviewController()
    vc.item = self.selectedItem
    let height: CGFloat = self.selectedItem?.content.count ?? 0 > 100 ? 300 : 200
    vc.preferredContentSize = CGSize(width: 250, height: height)
    return vc
}
```
