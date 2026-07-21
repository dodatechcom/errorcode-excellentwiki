---
title: "[Solution] UIKit UIStackView Custom Spacing Error"
description: "Fix UIStackView custom spacing between arranged subviews in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIStackView Custom Spacing Error

Custom spacing errors occur when the spacing value is too large for the available space, when spacing is not applied correctly between specific views, or when the spacing conflicts with auto layout.

## Common Causes
- Spacing too large for available space
- setCustomSpacing not applied to correct pair
- Spacing conflicts with auto layout constraints
- Spacing reset after layout updates

## How to Fix
1. Ensure spacing fits within available bounds
2. Apply custom spacing between specific arranged subviews
3. Check for auto layout conflicts
4. Reapply spacing after layout updates if needed

```swift
let stackView = UIStackView(arrangedSubviews: [view1, view2, view3])
stackView.spacing = 10 // Default spacing
stackView.setCustomSpacing(20, after: view1) // Custom after view1
stackView.setCustomSpacing(5, after: view2) // Custom after view2
```

## Examples
```swift
// Stack view with mixed spacing:
let stack = UIStackView()
stack.axis = .vertical
stack.addArrangedSubview(titleLabel)
stack.setCustomSpacing(4, after: titleLabel)
stack.addArrangedSubview(subtitleLabel)
stack.setCustomSpacing(16, after: subtitleLabel)
stack.addArrangedSubview(contentView)
stack.spacing = 8 // Default for remaining gaps
```
