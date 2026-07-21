---
title: "Objective-C UIViewController View Hierarchy Error"
description: "Fix Objective-C UIViewController view hierarchy errors when adding or removing views incorrectly."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Adding subview before view is loaded (view == nil)
- Removing view from wrong superview
- Not using auto-layout constraints when adding subviews
- Adding views in wrong lifecycle method (e.g., init instead of viewDidLoad)
- Retaining views that should be weak references

## How to Fix

```objc
// WRONG: Adding subview before view is loaded
- (instancetype)init {
    self = [super init];
    if (self) {
        [self.view addSubview:customView]; // view is nil!
    }
    return self;
}

// CORRECT: Add subviews in viewDidLoad
- (void)viewDidLoad {
    [super viewDidLoad];
    [self.view addSubview:customView];
}
```

```enrl
// WRONG: Not setting translatesAutoresizingMaskIntoConstraints
UIView *box = [[UIView alloc] init];
[self.view addSubview:box];
// Uses autoresizing mask, may conflict with constraints

// CORRECT: Disable autoresizing mask
UIView *box = [[UIView alloc] init];
box.translatesAutoresizingMaskIntoConstraints = NO;
[self.view addSubview:box];
```

## Examples

```objc
// Example 1: Proper view setup
- (void)viewDidLoad {
    [super viewDidLoad];
    
    self.customLabel = [[UILabel alloc] init];
    self.customLabel.translatesAutoresizingMaskIntoConstraints = NO;
    self.customLabel.text = @"Hello";
    [self.view addSubview:self.customLabel];
    
    [NSLayoutConstraint activateConstraints:@[
        [self.customLabel.centerXAnchor constraintEqualToAnchor:self.view.centerXAnchor],
        [self.customLabel.centerYAnchor constraintEqualToAnchor:self.view.centerYAnchor]
    ]];
}

// Example 2: Safe view removal
- (void)removeOverlay {
    [self.overlayView removeFromSuperview];
    self.overlayView = nil;
}

// Example 3: View tag-based lookup
UIView *overlay = [self.view viewWithTag:1001];
if (overlay) {
    [overlay removeFromSuperview];
}
```

## Related Errors

- [View controller lifecycle](objc-view-controller-lifecycle) -- VC lifecycle issues
- [AutoLayout error](objc-autolayout-error) -- layout problems
