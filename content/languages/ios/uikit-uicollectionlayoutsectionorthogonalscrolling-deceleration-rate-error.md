---
title: "[Solution] UIKit UICollectionLayoutSectionOrthogonalScrolling Deceleration Rate Error"
description: "Fix orthogonal scrolling deceleration rate configuration errors in collection view sections."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutSectionOrthogonalScrolling Deceleration Rate Error

Deceleration rate errors occur when the rate is set too high or too low, when the rate conflicts with the orthogonal scrolling behavior, or when the rate is not properly applied.

## Common Causes
- Deceleration rate too fast or too slow
- Rate incompatible with scrolling behavior
- Rate reset after layout updates
- Rate not matching user expectation

## How to Fix
1. Set appropriate deceleration rate for content
2. Ensure rate is compatible with scrolling behavior
3. Reapply rate after layout changes
4. Test with actual content scroll speed

```swift
var section = NSCollectionLayoutSection(group: group)
section.orthogonalScrollingBehavior = .continuous
section.visibleItemsInvalidationHandler = { _, _, point in
    // Adjust based on scroll position
}
```

## Examples
```swift
// Section with custom scrolling behavior:
var section = NSCollectionLayoutSection(group: group)
section.orthogonalScrollingBehavior = .groupPagingCentered
section.interGroupSpacing = 10
section.contentInsets = NSDirectionalEdgeInsets(top: 0, leading: 20, bottom: 0, trailing: 20)
```
