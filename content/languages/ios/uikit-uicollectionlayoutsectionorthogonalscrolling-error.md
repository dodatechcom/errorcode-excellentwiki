---
title: "[Solution] UIKit UICollectionLayoutSectionOrthogonalScrolling Error"
description: "Fix collection view orthogonal scrolling section configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutSectionOrthogonalScrolling Error

Orthogonal scrolling fails when the section configuration is incompatible, when the item size does not match the orthogonal scroll behavior, or when the section insets cause unexpected behavior.

## Common Causes
- Orthogonal scrolling not configured on section
- Item size not appropriate for continuous scrolling
- Section insets conflicting with scroll bounds
- Paging behavior not matching item width

## How to Fix
1. Set orthogonalScrollingBehavior on the section
2. Size items appropriately for the scrolling mode
3. Configure section insets for proper padding
4. Match paging behavior with item size

```swift
var section = NSCollectionLayoutSection(group: group)
section.orthogonalScrollingBehavior = .continuous
section.contentInsets = NSDirectionalEdgeInsets(top: 0, leading: 20, bottom: 0, trailing: 20)
```

## Examples
```swift
// Different orthogonal scrolling behaviors:
section.orthogonalScrollingBehavior = .none // No orthogonal scrolling
section.orthogonalScrollingBehavior = .continuous // Continuous scroll
section.orthogonalScrollingBehavior = .continuousGroupLeadingBoundary // Group boundary
section.orthogonalScrollingBehavior = .paging // Page by group
section.orthogonalScrollingBehavior = .groupPaging // Page by group with boundary
section.orthogonalScrollingBehavior = .groupPagingCentered // Centered group paging
```
