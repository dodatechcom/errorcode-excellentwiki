---
title: "[Solution] UIKit UIContextMenu Interaction Menu Image Error"
description: "Fix UIContextMenuInteraction menu image and icon configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Menu Image Error

Menu image errors occur when the image does not load, when the image conflicts with the title, or when the image is not properly sized for the menu.

## Common Causes
- Image not loading from system or bundle
- Image conflicts with title text
- Image not properly sized
- Image tintColor not matching design

## How to Fix
1. Verify image exists in bundle or system
2. Ensure image does not conflict with title
3. Set proper image size
4. Configure image tintColor

```swift
let share = UIAction(title: "Share", image: UIImage(systemName: "square.and.arrow.up")) { _ in }
let delete = UIAction(title: "Delete", image: UIImage(systemName: "trash")) { _ in }
```

## Examples
```swift
// Actions with custom images:
let heart = UIAction(title: "Favorite", image: UIImage(systemName: "heart.fill")) { _ in }
let star = UIAction(title: "Rate", image: UIImage(systemName: "star.fill")) { _ in }
let bookmark = UIAction(title: "Save", image: UIImage(systemName: "bookmark.fill")) { _ in }
```
