---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Alignment Error"
description: "Fix UICollectionLayoutListConfiguration section header layout alignment configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Alignment Error

Layout alignment errors occur when the alignment is not properly configured, when the alignment conflicts with the header content, or when the alignment does not match the design.

## Common Causes
- Alignment not configured
- Alignment conflicts with content
- Alignment not matching design
- Alignment not updating with content changes

## How to Fix
1. Configure alignment properly
2. Ensure alignment complements content
3. Match design specifications
4. Update alignment with content changes

```swift
header.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    header.centerXAnchor.constraint(equalTo: view.centerXAnchor),
    header.centerYAnchor.constraint(equalTo: view.centerYAnchor)
])
```

## Examples
```swift
// Center aligned header:
header.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true

// Leading aligned header:
header.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 16).isActive = true

// Trailing aligned header:
header.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -16).isActive = true
```
