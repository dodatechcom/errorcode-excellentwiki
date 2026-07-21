---
title: "[Solution] UIKit UIContextMenu Interaction Configuration Error"
description: "Fix UIContextMenuInteraction configuration creation and customization errors."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Configuration Error

Interaction configuration fails when the configuration is created with incompatible options, when the preview provider returns an incompatible view controller, or when the configuration conflicts with existing interactions.

## Common Causes
- Configuration created with incompatible options
- Preview provider returns nil
- Configuration conflicts with existing interactions
- Menu action handler not properly connected

## How to Fix
1. Create configuration with compatible options
2. Return valid view controller from preview provider
3. Ensure configuration is unique per interaction
4. Connect menu action handlers properly

```swift
let interaction = UIContextMenuInteraction(delegate: self)
view.addInteraction(interaction)

// Preview with proper configuration:
func interaction(_ interaction: UIContextMenuInteraction, configurationForMenuAtLocation location: CGPoint) -> UIContextMenuConfiguration? {
    let preview: UIContextMenuContentPreviewProvider = {
        let vc = UIViewController()
        vc.view.backgroundColor = .systemBackground
        return vc
    }
    return UIContextMenuConfiguration(identifier: nil, previewProvider: preview) { _ in
        UIMenu(children: [UIAction(title: "Action") { _ in }])
    }
}
```

## Examples
```swift
// Configuration with commit style:
func interaction(_ interaction: UIContextMenuInteraction, configurationForMenuAtLocation location: CGPoint) -> UIContextMenuConfiguration? {
    return UIContextMenuConfiguration(identifier: nil, previewProvider: {
        let vc = PreviewViewController()
        vc.preferredContentSize = CGSize(width: 200, height: 200)
        return vc
    }, actionProvider: { _ in
        let action = UIAction(title: "Share", image: UIImage(systemName: "square.and.arrow.up")) { _ in }
        return UIMenu(children: [action])
    })
}
```
