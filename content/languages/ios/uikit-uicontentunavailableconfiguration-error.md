---
title: "[Solution] UIKit UIContentUnavailableConfiguration Error"
description: "Fix UIContentUnavailableConfiguration empty state display errors in iOS 17+."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContentUnavailableConfiguration Error

Content unavailable configuration fails when the configuration is not properly applied, when the image or text is not set, or when the configuration conflicts with the existing content.

## Common Causes
- Configuration not applied to content view
- Image or text not configured
- Configuration conflicts with existing data
- Button actions not connected

## How to Fix
1. Apply configuration when content is empty
2. Set image, text, and secondary text
3. Connect button actions
4. Remove configuration when content loads

```swift
// Empty state configuration:
var emptyConfig = UIContentUnavailableConfiguration.empty()
emptyConfig.image = UIImage(systemName: "tray")
emptyConfig.text = "No Items"
emptyConfig.secondaryText = "Add items to get started"
emptyConfig.button = UIContentUnavailableConfiguration.Button(title: "Add Item", primaryAction: UIAction { _ in self.addItem() })
collectionView.contentUnavailableConfiguration = emptyConfig
```

## Examples
```swift
// Search empty state:
if filteredItems.isEmpty {
    var config = UIContentUnavailableConfiguration.search()
    config.text = "No Results"
    config.secondaryText = "Try a different search term"
    collectionView.contentUnavailableConfiguration = config
} else {
    collectionView.contentUnavailableConfiguration = nil
}
```
