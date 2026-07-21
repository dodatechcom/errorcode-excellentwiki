---
title: "[Solution] UIKit UIListContentConfiguration Image Error"
description: "Fix UIListContentConfiguration image sizing and rendering errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIListContentConfiguration Image Error

Image configuration errors occur when the image is not properly sized, when the image tintColor conflicts with the design, or when the image placement does not match expectations.

## Common Causes
- Image not matching expected size
- TintColor not applied correctly
- Image placement (leading/trailing) incorrect
- Image not loading from system or bundle

## How to Fix
1. Ensure image is properly sized or uses system image
2. Set imageProperties.tintColor explicitly
3. Configure image placement correctly
4. Verify image exists in bundle or system

```swift
var content = cell.defaultContentConfiguration()
content.image = UIImage(systemName: "star.fill")
content.imageProperties.tintColor = .systemYellow
content.imageProperties.cornerRadius = 8
cell.contentConfiguration = content
```

## Examples
```swift
// Cell with custom image:
var content = UIListContentConfiguration.subtitleCell()
content.text = "User Name"
content.secondaryText = "user@example.com"
content.image = UIImage(named: "avatar")
content.imageProperties.maximumSize = CGSize(width: 40, height: 40)
content.imageProperties.cornerRadius = 20
cell.contentConfiguration = content
```
