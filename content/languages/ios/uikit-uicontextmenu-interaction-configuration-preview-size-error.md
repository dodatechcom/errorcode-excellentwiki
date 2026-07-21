---
title: "[Solution] UIKit UIContextMenu Interaction Configuration Preview Size Error"
description: "Fix UIContextMenuInteraction configuration preview size and preferredContentSize errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Configuration Preview Size Error

Preview size errors occur when the preferredContentSize is not set, when the size conflicts with the available space, or when the size does not match the content.

## Common Causes
- preferredContentSize not configured
- Size conflicts with available space
- Size not matching content
- Size not updating with content changes

## How to Fix
1. Set preferredContentSize on preview controller
2. Ensure size fits within available space
3. Match size to content requirements
4. Update size with content changes

```swift
let preview: UIContextMenuContentPreviewProvider = {
    let vc = UIViewController()
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
    let height = self.selectedItem?.content.count ?? 0 > 100 ? 300 : 200
    vc.preferredContentSize = CGSize(width: 250, height: CGFloat(height))
    return vc
}
```
