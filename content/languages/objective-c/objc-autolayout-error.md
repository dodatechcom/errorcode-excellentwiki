---
title: "[Solution] Objective-C Auto Layout Error"
description: "Auto Layout constraint errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Auto Layout Error

Auto Layout constraint errors.

### Common Causes
Ambiguous; conflicting constraints

### How to Fix
```objc
NSLayoutConstraint *constraint = [NSLayoutConstraint constraintWithItem:view1
    attribute:NSLayoutAttributeLeading
    relatedBy:NSLayoutRelationEqual
    toItem:view2
    attribute:NSLayoutAttributeLeading
    multiplier:1.0
    constant:0];
[view1 addConstraint:constraint];
```

### Examples
```objc
[view1 setTranslatesAutoresizingMaskIntoConstraints:NO];
```
