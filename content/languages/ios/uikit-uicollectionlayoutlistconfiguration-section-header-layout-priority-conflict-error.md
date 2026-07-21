---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Priority Conflict Error"
description: "Fix UICollectionLayoutListConfiguration section header layout priority conflict errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Priority Conflict Error

Layout priority conflict errors occur when there are conflicting priorities, when the priorities are not properly resolved, or when the priorities do not match the design.

## Common Causes
- Conflicting priorities
- Priorities not resolved
- Priorities not matching design
- Priorities not updating with size changes

## How to Fix
1. Remove conflicting priorities
2. Resolve priority issues
3. Match design specifications
4. Update priorities with size changes

```swift
header.translatesAutoresizingMaskIntoConstraints = false
let heightConstraint = header.heightAnchor.constraint(equalToConstant: 60)
heightConstraint.priority = UILayoutPriority(999)
heightConstraint.isActive = true
```

## Examples
```swift
// Priority conflict resolution:
header.contentCompressionResistancePriority(for: .vertical) = .required
header.contentHuggingPriority(for: .vertical) = .defaultHigh

// Remove priority conflicts:
header.contentCompressionResistancePriority(for: .horizontal) = .defaultLow
```
