---
title: "[Solution] UIKit UIContextMenu Interaction Configuration Preview Override Targeted Preview Error"
description: "Fix UIContextMenuInteraction preview override targeted preview configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Configuration Preview Override Targeted Preview Error

Targeted preview errors occur when the preview is not properly targeted, when the preview parameters are incorrect, or when the preview conflicts with the interaction location.

## Common Causes
- Preview not properly targeted
- Preview parameters incorrect
- Preview conflicts with interaction location
- Preview not updating for different items

## How to Fix
1. Target preview to the correct view
2. Set correct preview parameters
3. Ensure preview does not conflict with interaction
4. Update preview for different items

```swift
func interaction(_ interaction: UIContextMenuInteraction, previewForHighlightingWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    let parameters = UIPreviewParameters()
    parameters.backgroundColor = .clear
    return UITargetedPreview(view: interaction.view!, parameters: parameters)
}
```

## Examples
```swift
// Targeted preview with shape:
func interaction(_ interaction: UIContextMenuInteraction, previewForHighlightingWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    guard let view = interaction.view else { return nil }
    let parameters = UIPreviewParameters()
    parameters.visiblePath = UIBezierPath(roundedRect: view.bounds, cornerRadius: 12)
    parameters.backgroundColor = UIColor.systemBackground.withAlphaComponent(0.95)
    return UITargetedPreview(view: view, parameters: parameters)
}
```
