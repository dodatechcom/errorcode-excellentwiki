---
title: "[Solution] UIKit UIContextMenu Interaction Preview Occlusion Error"
description: "Fix UIContextMenuInteraction preview occlusion and overlap errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Preview Occlusion Error

Preview occlusion errors occur when the preview is occluded by other views, when the preview overlaps with the menu, or when the preview is not properly positioned relative to the interaction point.

## Common Causes
- Preview occluded by other views
- Preview overlaps with menu
- Preview not positioned correctly
- Preview conflicts with safe area

## How to Fix
1. Ensure preview is not occluded
2. Position preview to not overlap with menu
3. Account for safe area in preview positioning
4. Test preview on different screen sizes

```swift
func interaction(_ interaction: UIContextMenuInteraction, previewForHighlightingWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    let parameters = UIPreviewParameters()
    parameters.backgroundColor = .clear
    return UITargetedPreview(view: interaction.view!, parameters: parameters)
}
```

## Examples
```swift
// Preview with proper positioning:
func interaction(_ interaction: UIContextMenuInteraction, previewForHighlightingWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    guard let view = interaction.view else { return nil }
    let parameters = UIPreviewParameters()
    parameters.backgroundColor = .clear
    parameters.visiblePath = UIBezierPath(roundedRect: view.bounds, cornerRadius: 8)
    return UITargetedPreview(view: view, parameters: parameters)
}
```
