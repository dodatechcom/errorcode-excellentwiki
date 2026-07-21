---
title: "[Solution] UIKit UIContextMenu Interaction Configuration Preview Highlight Shape Error"
description: "Fix UIContextMenuInteraction preview highlight shape configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Configuration Preview Highlight Shape Error

Preview highlight shape errors occur when the shape is not properly configured, when the shape conflicts with the preview content, or when the shape does not match the design.

## Common Causes
- Shape not configured
- Shape conflicts with preview content
- Shape not matching design
- Shape not updating with content changes

## How to Fix
1. Configure shape properly
2. Ensure shape complements preview content
3. Match design specifications
4. Update shape with content changes

```swift
func interaction(_ interaction: UIContextMenuInteraction, previewForHighlightingWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    let parameters = UIPreviewParameters()
    parameters.visiblePath = UIBezierPath(roundedRect: interaction.view!.bounds, cornerRadius: 12)
    parameters.backgroundColor = UIColor.systemBlue.withAlphaComponent(0.15)
    return UITargetedPreview(view: interaction.view!, parameters: parameters)
}
```

## Examples
```swift
// Oval highlight:
func interaction(_ interaction: UIContextMenuInteraction, previewForHighlightingWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    let parameters = UIPreviewParameters()
    parameters.visiblePath = UIBezierPath(ovalIn: interaction.view!.bounds)
    parameters.backgroundColor = UIColor.systemGreen.withAlphaComponent(0.2)
    return UITargetedPreview(view: interaction.view!, parameters: parameters)
}
```
