---
title: "Objective-C Autolayout Constraint Conflict Error"
description: "Fix Objective-C Autolayout constraint conflict errors when ambiguous or conflicting constraints are detected."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Two constraints specify different values for same attribute
- Missing constraint for at least one dimension (x, y, width, height)
- Constraints reference views not in the same hierarchy
- Priority conflict where required constraints contradict
- TranslatesAutoresizingMaskIntoConstraints conflicts

## How to Fix

```objc
// WRONG: Conflicting constraints
[viewA.widthAnchor constraintEqualToAnchor:viewB.widthAnchor].active = YES;
[viewA.widthAnchor constraintEqualToConstant:200].active = YES;
// If viewB.width != 200, conflict!

// CORRECT: Use priorities
NSLayoutConstraint *widthConstraint =
    [viewA.widthAnchor constraintEqualToConstant:200];
widthConstraint.priority = UILayoutPriorityDefaultHigh;
widthConstraint.active = YES;
```

```objc
// WRONG: Missing constraints
NSLayoutConstraint *x = [view.leftAnchor constraintEqualToAnchor:superview.leftAnchor];
NSLayoutConstraint *y = [view.topAnchor constraintEqualToAnchor:superview.topAnchor];
// Missing width and height -- ambiguous layout

// CORRECT: Provide all required constraints
NSLayoutConstraint *x = [view.leftAnchor constraintEqualToAnchor:superview.leftAnchor];
NSLayoutConstraint *y = [view.topAnchor constraintEqualToAnchor:superview.topAnchor];
NSLayoutConstraint *w = [view.widthAnchor constraintEqualToConstant:100];
NSLayoutConstraint *h = [view.heightAnchor constraintEqualToConstant:50];
```

## Examples

```objc
// Example 1: Programmatic constraints
view.translatesAutoresizingMaskIntoConstraints = NO;
[NSLayoutConstraint activateConstraints:@[
    [view.centerXAnchor constraintEqualToAnchor:superview.centerXAnchor],
    [view.centerYAnchor constraintEqualToAnchor:superview.centerYAnchor],
    [view.widthAnchor constraintEqualToConstant:200],
    [view.heightAnchor constraintEqualToConstant:100]
]];

// Example 2: Breaking constraints with priority
NSLayoutConstraint *height = [view.heightAnchor constraintEqualToConstant:44];
height.priority = UILayoutPriorityRequired - 1;
height.active = YES;

// Example 3: Content hugging and compression
[view setContentHuggingPriority:UILayoutPriorityDefaultHigh
    forAxis:UILayoutConstraintAxisHorizontal];
[view setContentCompressionResistancePriority:UILayoutPriorityRequired
    forAxis:UILayoutConstraintAxisVertical];
```

## Related Errors

- [AutoLayout error](objc-autolayout-error) -- layout constraint issues
- [UIView error](objc-uikit-error) -- UIKit view problems
