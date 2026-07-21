---
title: "[Solution] UIKit UIContextMenu Interaction Configuration Preview Highlighting Error"
description: "Fix UIContextMenuInteraction preview highlighting configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Configuration Preview Highlighting Error

Preview highlighting errors occur when the highlight is not properly applied, when the highlight conflicts with the preview content, or when the highlight does not update with interaction state.

## Common Causes
- Highlight not properly applied
- Highlight conflicts with preview content
- Highlight not updating with interaction state
- Highlight not matching design specifications

## How to Fix
1. Apply highlight properly to preview
2. Ensure highlight does not conflict with content
3. Update highlight with interaction state
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
// Highlight with custom shape:
func interaction(_ interaction: UIContextMenuInteraction, previewForHighlightingWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    guard let view = interaction.view else { return nil }
    let parameters = UIPreviewParameters()
    parameters.visiblePath = UIBezierPath(roundedRect: view.bounds, cornerRadius: 8)
    parameters.backgroundColor = UIColor.systemBlue.withAlphaComponent(0.15)
    return UITargetedPreview(view: view, parameters: parameters)
}
```
