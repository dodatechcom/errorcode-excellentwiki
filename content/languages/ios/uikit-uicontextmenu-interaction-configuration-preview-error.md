---
title: "[Solution] UIKit UIContextMenu Interaction Configuration Preview Error"
description: "Fix UIContextMenuInteraction configuration preview provider and action provider coordination errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Configuration Preview Error

Preview and action provider coordination errors occur when the preview and action providers conflict, when the preview does not match the actions, or when the providers return incompatible configurations.

## Common Causes
- Preview and action providers conflict
- Preview does not match actions
- Providers return incompatible configurations
- Providers not properly connected

## How to Fix
1. Ensure preview matches action content
2. Coordinate preview and action providers
3. Return compatible configurations
4. Connect providers properly

```swift
return UIContextMenuConfiguration(identifier: indexPath, previewProvider: {
    let vc = DetailViewController()
    vc.item = self.items[indexPath.item]
    return vc
}, actionProvider: { _ in
    let item = self.items[indexPath.item]
    let share = UIAction(title: "Share") { _ in }
    let delete = UIAction(title: "Delete", attributes: .destructive) { _ in }
    return UIMenu(children: [share, delete])
})
```

## Examples
```swift
// Coordinated preview and actions:
return UIContextMenuConfiguration(identifier: indexPath, previewProvider: {
    let preview = ItemPreviewController()
    preview.item = self.items[indexPath.item]
    preview.preferredContentSize = CGSize(width: 250, height: 200)
    return preview
}, actionProvider: { [weak self] _ in
    guard let self = self else { return nil }
    let item = self.items[indexPath.item]
    return UIMenu(children: [
        UIAction(title: "View Details") { _ in self.viewDetails(item) },
        UIAction(title: "Share") { _ in self.share(item) },
        UIAction(title: "Delete", attributes: .destructive) { _ in self.delete(item) }
    ])
})
```
