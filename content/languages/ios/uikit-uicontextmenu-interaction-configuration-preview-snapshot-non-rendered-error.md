---
title: "[Solution] UIKit UIContextMenu Interaction Configuration Preview Snapshot Non Rendered Error"
description: "Fix UIContextMenuInteraction preview snapshot non-rendered view configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Configuration Preview Snapshot Non Rendered Error

Non-rendered snapshot errors occur when the snapshot of a non-rendered view is not properly configured, when the view is not in the hierarchy, or when the view's layer is not rendered.

## Common Causes
- View not in hierarchy
- View layer not rendered
- Snapshot parameters incorrect
- View not visible at snapshot time

## How to Fix
1. Ensure view is in hierarchy
2. Verify view layer is rendered
3. Set correct parameters
4. Check view visibility

```swift
// Ensure view is in hierarchy before creating preview
func interaction(_ interaction: UIContextMenuInteraction, previewForHighlightingWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    guard let view = interaction.view, view.window != nil else { return nil }
    return UITargetedPreview(view: view)
}
```

## Examples
```swift
// Safely create preview for view:
func interaction(_ interaction: UIContextMenuInteraction, previewForHighlightingWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview? {
    guard let view = interaction.view,
          let window = view.window,
          window.bounds.contains(view.frame) else {
        return nil
    }
    let parameters = UIPreviewParameters()
    parameters.backgroundColor = .clear
    return UITargetedPreview(view: view, parameters: parameters)
}
```
