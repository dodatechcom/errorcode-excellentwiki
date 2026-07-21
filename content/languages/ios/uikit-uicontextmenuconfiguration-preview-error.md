---
title: "[Solution] UIKit UIContextMenuConfiguration Preview Error"
description: "Fix UIContextMenuConfiguration preview provider errors in UIKit context menus."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenuConfiguration Preview Error

Preview provider errors occur when the preview view controller is not properly configured, when the preview size does not match expectations, or when the preview is deallocated before display.

## Common Causes
- Preview view controller not properly initialized
- Preview size conflicts with container
- Preview released before display
- Preview not updating for different items

## How to Fix
1. Initialize preview view controller properly
2. Set preferredContentSize for preview
3. Hold strong reference to preview
4. Update preview content for each item

```swift
// Context menu with preview:
func interaction(_ interaction: UIContextMenuInteraction, configurationForMenuAtLocation location: CGPoint) -> UIContextMenuConfiguration? {
    let previewProvider: UIContextMenuContentPreviewProvider = {
        let vc = UIViewController()
        vc.view.backgroundColor = .systemBackground
        vc.preferredContentSize = CGSize(width: 200, height: 200)
        return vc
    }
    return UIContextMenuConfiguration(identifier: nil, previewProvider: previewProvider) { _ in
        UIMenu(children: [UIAction(title: "Action") { _ in }])
    }
}
```

## Examples
```swift
// Dynamic preview based on content:
let previewProvider: UIContextMenuContentPreviewProvider = { [weak self] in
    let preview = ItemPreviewViewController()
    preview.item = self?.selectedItem
    preview.preferredContentSize = CGSize(width: 300, height: 400)
    return preview
}
```
