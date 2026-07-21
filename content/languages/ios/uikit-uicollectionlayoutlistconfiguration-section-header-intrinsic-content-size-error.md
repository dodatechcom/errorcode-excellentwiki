---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Intrinsic Content Size Error"
description: "Fix UICollectionLayoutListConfiguration section header intrinsic content size calculation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Intrinsic Content Size Error

Intrinsic content size errors occur when the size is not properly calculated, when the size conflicts with the header content, or when the size does not match the design.

## Common Causes
- Size not calculated properly
- Size conflicts with header content
- Size not matching design
- Size not updating with content changes

## How to Fix
1. Calculate size based on content
2. Ensure size fits header content
3. Match design specifications
4. Update size with content changes

```swift
header.invalidateIntrinsicContentSize()
let size = header.systemLayoutSizeFitting(UIView.layoutFittingCompressedSize)
```

## Examples
```swift
// Calculate intrinsic size:
let size = header.systemLayoutSizeFitting(
    CGSize(width: collectionView.bounds.width, height: CGFloat.infinity),
    withHorizontalFittingPriority: .required,
    verticalFittingPriority: .fittingSizeLevel
)

// Invalidate when content changes:
header.invalidateIntrinsicContentSize()
```
