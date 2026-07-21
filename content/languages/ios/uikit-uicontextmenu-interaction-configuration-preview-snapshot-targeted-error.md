---
title: "[Solution] UIKit UIContextMenu Interaction Configuration Preview Snapshot Targeted Error"
description: "Fix UIContextMenuInteraction preview snapshot targeted preview configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Configuration Preview Snapshot Targeted Error

Targeted snapshot errors occur when the snapshot is not properly targeted, when the snapshot parameters are incorrect, or when the snapshot conflicts with the live preview.

## Common Causes
- Snapshot not properly targeted
- Parameters incorrect
- Snapshot conflicts with live preview
- Snapshot not updating for different items

## How to Fix
1. Target snapshot to correct view
2. Set correct parameters
3. Ensure snapshot does not conflict with preview
4. Update snapshot for different items

```swift
func interaction(_ interaction: UIContextMenuInteraction, previewForDismissingWithMenuConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    let parameters = UIPreviewParameters()
    parameters.backgroundColor = .clear
    return UITargetedPreview(view: interaction.view!, parameters: parameters)
}
```

## Examples
```swift
// Targeted snapshot with shape:
func interaction(_ interaction: UIContextMenuInteraction, previewForDismissingWithMenuConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    guard let view = interaction.view else { return nil }
    let parameters = UIPreviewParameters()
    parameters.visiblePath = UIBezierPath(roundedRect: view.bounds, cornerRadius: 8)
    parameters.backgroundColor = UIColor.systemBackground.withAlphaComponent(0.9)
    return UITargetedPreview(view: view, parameters: parameters)
}
```
