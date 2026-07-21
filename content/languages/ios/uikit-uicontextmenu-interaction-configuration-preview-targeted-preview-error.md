---
title: "[Solution] UIKit UIContextMenu Interaction Configuration Preview Targeted Preview Error"
description: "Fix UIContextMenuInteraction configuration preview targeted preview positioning errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Configuration Preview Targeted Preview Error

Targeted preview positioning errors occur when the preview is not positioned correctly, when the preview overlaps with the interaction point, or when the preview conflicts with safe area.

## Common Causes
- Preview not positioned correctly
- Preview overlaps interaction point
- Preview conflicts with safe area
- Preview not updating with content changes

## How to Fix
1. Position preview correctly relative to interaction
2. Avoid overlap with interaction point
3. Account for safe area
4. Update preview for content changes

```swift
func interaction(_ interaction: UIContextMenuInteraction, previewForHighlightingWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    let parameters = UIPreviewParameters()
    parameters.backgroundColor = .clear
    return UITargetedPreview(view: interaction.view!, parameters: parameters)
}
```

## Examples
```swift
// Preview with custom positioning:
func interaction(_ interaction: UIContextMenuInteraction, previewForHighlightingWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    guard let view = interaction.view else { return nil }
    let parameters = UIPreviewParameters()
    parameters.visiblePath = UIBezierPath(ovalIn: view.bounds)
    parameters.backgroundColor = .clear
    return UITargetedPreview(view: view, parameters: parameters)
}
```
