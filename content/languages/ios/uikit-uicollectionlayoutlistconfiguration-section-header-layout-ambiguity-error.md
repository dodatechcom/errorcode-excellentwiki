---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Ambiguity Error"
description: "Fix UICollectionLayoutListConfiguration section header layout ambiguity errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Ambiguity Error

Layout ambiguity errors occur when the layout is ambiguous, when the layout is not properly defined, or when the layout does not match the design.

## Common Causes
- Layout ambiguous
- Layout not properly defined
- Layout not matching design
- Layout not updating with size changes

## How to Fix
1. Resolve layout ambiguity
2. Define layout properly
3. Match design specifications
4. Update layout with size changes

```swift
header.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    header.topAnchor.constraint(equalTo: view.topAnchor),
    header.leadingAnchor.constraint(equalTo: view.leadingAnchor),
    header.trailingAnchor.constraint(equalTo: view.trailingAnchor),
    header.heightAnchor.constraint(equalToConstant: 60)
])
```

## Examples
```swift
// Resolve ambiguity:
header.setContentHuggingPriority(.required, for: .vertical)
header.setContentCompressionResistancePriority(.required, for: .vertical)

// Check for ambiguity:
let ambiguousConstraints = header.constraints.filter { $0.firstItem == nil || $0.secondItem == nil }
print("Ambiguous: \(ambiguousConstraints.count)")
```
