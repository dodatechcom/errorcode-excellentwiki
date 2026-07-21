---
title: "[Solution] UIKit UIContextMenu Interaction Configuration Preview Highlight Color Error"
description: "Fix UIContextMenuInteraction preview highlight color configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Configuration Preview Highlight Color Error

Preview highlight color errors occur when the color is not properly set, when the color conflicts with the preview content, or when the color does not update with theme changes.

## Common Causes
- Highlight color not set
- Color conflicts with preview content
- Color not updating with theme
- Color not matching design

## How to Fix
1. Set highlight color properly
2. Ensure color complements preview content
3. Update color with theme changes
4. Match design specifications

```swift
func interaction(_ interaction: UIContextMenuInteraction, previewForHighlightingWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    let parameters = UIPreviewParameters()
    parameters.backgroundColor = UIColor.systemBlue.withAlphaComponent(0.2)
    return UITargetedPreview(view: interaction.view!, parameters: parameters)
}
```

## Examples
```swift
// Custom highlight colors:
func interaction(_ interaction: UIContextMenuInteraction, previewForHighlightingWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    let parameters = UIPreviewParameters()
    parameters.backgroundColor = UIColor.systemGreen.withAlphaComponent(0.15)
    parameters.visiblePath = UIBezierPath(roundedRect: interaction.view!.bounds, cornerRadius: 10)
    return UITargetedPreview(view: interaction.view!, parameters: parameters)
}
```
