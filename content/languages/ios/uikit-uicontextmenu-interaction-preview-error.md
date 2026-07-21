---
title: "[Solution] UIKit UIContextMenu Interaction Preview Error"
description: "Fix UIContextMenuInteraction custom preview sizing and positioning errors."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Preview Error

Custom preview errors occur when the preview size is not set, when the preview is positioned incorrectly relative to the interaction point, or when the preview conflicts with the menu.

## Common Causes
- Preview preferredContentSize not configured
- Preview positioned incorrectly
- Preview conflicts with menu layout
- Preview not updating for different items

## How to Fix
1. Set preferredContentSize on preview controller
2. Configure preview position relative to interaction
3. Ensure preview does not conflict with menu
4. Update preview for different content items

```swift
func interaction(_ interaction: UIContextMenuInteraction, previewForHighlightingWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    let parameters = UIPreviewParameters()
    parameters.backgroundColor = .clear
    return UITargetedPreview(view: interaction.view!, parameters: parameters)
}
```

## Examples
```swift
// Targeted preview with custom shape:
func interaction(_ interaction: UIContextMenuInteraction, previewForHighlightingWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    let parameters = UIPreviewParameters()
    parameters.visiblePath = UIBezierPath(ovalIn: interaction.view!.bounds)
    parameters.backgroundColor = .clear
    return UITargetedPreview(view: interaction.view!, parameters: parameters)
}
```
