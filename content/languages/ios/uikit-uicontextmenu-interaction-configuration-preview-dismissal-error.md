---
title: "[Solution] UIKit UIContextMenu Interaction Configuration Preview Dismissal Error"
description: "Fix UIContextMenuInteraction preview dismissal configuration and animation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Configuration Preview Dismissal Error

Preview dismissal errors occur when the dismissal animation is not properly configured, when the dismissal conflicts with the menu, or when the dismissal does not complete properly.

## Common Causes
- Dismissal animation not configured
- Dismissal conflicts with menu
- Dismissal not completing
- Dismissal not properly handled

## How to Fix
1. Configure dismissal animation properly
2. Ensure dismissal does not conflict with menu
3. Handle dismissal completion
4. Implement dismissal handler

```swift
func interaction(_ interaction: UIContextMenuInteraction, previewForDismissingWithMenuConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    let parameters = UIPreviewParameters()
    parameters.backgroundColor = .clear
    return UITargetedPreview(view: interaction.view!, parameters: parameters)
}
```

## Examples
```swift
// Dismissal with custom animation:
func interaction(_ interaction: UIContextMenuInteraction, previewForDismissingWithMenuConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    guard let view = interaction.view else { return nil }
    let parameters = UIPreviewParameters()
    parameters.visiblePath = UIBezierPath(roundedRect: view.bounds.insetBy(dx: 2, dy: 2), cornerRadius: 8)
    parameters.backgroundColor = UIColor.systemBackground.withAlphaComponent(0.8)
    return UITargetedPreview(view: view, parameters: parameters)
}
```
