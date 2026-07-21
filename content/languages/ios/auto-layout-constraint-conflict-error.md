---
title: "[Solution] Auto Layout Constraint Conflict Error"
description: "Fix Auto Layout ambiguous layout and constraint conflict errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Auto Layout Constraint Conflict Error

Constraint conflicts occur when two or more constraints cannot be simultaneously satisfied, leading to runtime layout issues.

## Common Causes
- Conflicting height and width constraints
- Missing constraints leaving view with ambiguous position
- Constraints referencing wrong views or anchors
- System layout size calculator failing due to ambiguous layout

## How to Fix
1. Check the constraint conflict description in the console
2. Identify which constraints are conflicting
3. Remove or modify one of the conflicting constraints
4. Use priority to allow constraint breaking

```swift
// Use constraint priorities:
heightAnchor.constraint(equalToConstant: 100).priority = .defaultHigh
widthAnchor.constraint(equalToConstant: 200).priority = .required

// Resolve conflicts with lower priority:
view.heightAnchor.constraint(greaterThanOrEqualToConstant: 50).priority = UILayoutPriority(999)
```

## Examples
```swift
// Example: Resolving constraint conflict
let subview = UIView()
view.addSubview(subview)
subview.translatesAutoresizingMaskIntoConstraints = false

NSLayoutConstraint.activate([
    subview.topAnchor.constraint(equalTo: view.topAnchor, constant: 20),
    subview.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),
    subview.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20),
    subview.heightAnchor.constraint(equalToConstant: 100) // Fixed height
])
```
