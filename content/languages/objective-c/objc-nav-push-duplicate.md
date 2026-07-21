---
title: "Objective-C UINavigationController Push Duplicate Error"
description: "Fix Objective-C UINavigationController push errors when pushing the same view controller instance twice."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Same view controller instance pushed multiple times
- Pushing during existing push animation
- View controller does not have a valid nib or storyboard
- Pushing modal view controller on navigation controller
- Navigation stack grows too deep causing memory pressure

## How to Fix

```objc
// WRONG: Pushing same instance twice
MyDetailController *detail = [[MyDetailController alloc] init];
[self.navigationController pushViewController:detail animated:YES];
// Later...
[self.navigationController pushViewController:detail animated:YES]; // crash

// CORRECT: Check if already in navigation stack
- (void)pushViewController:(UIViewController *)vc {
    if (![self.navigationController.viewControllers containsObject:vc]) {
        [self.navigationController pushViewController:vc animated:YES];
    }
}
```

```objc
// WRONG: Push during existing push animation
if (animating) {
    [self.navigationController pushViewController:newVC animated:YES];
    // Animation conflict!
}

// CORRECT: Wait for animation to complete
[CATransaction begin];
[CATransaction setCompletionBlock:^{
    [self.navigationController pushViewController:newVC animated:YES];
}];
[self.navigationController pushViewController:intermediateVC animated:YES];
[CATransaction commit];
```

## Examples

```objc
// Example 1: Safe push
if (self.navigationController) {
    DetailController *vc = [[DetailController alloc] initWithItem:item];
    [self.navigationController pushViewController:vc animated:YES];
}

// Example 2: Push or present fallback
- (void)showDetail:(Item *)item {
    DetailController *vc = [[DetailController alloc] initWithItem:item];
    if (self.navigationController) {
        [self.navigationController pushViewController:vc animated:YES];
    } else {
        UINavigationController *nav = [[UINavigationController alloc]
            initWithRootViewController:vc];
        [self presentViewController:nav animated:YES completion:nil];
    }
}

// Example 3: Pop to root safely
[self.navigationController popToRootViewControllerAnimated:YES];
```

## Related Errors

- [Navigation controller error](objc-uinavigationcontroller) -- nav stack issues
- [View controller lifecycle](objc-view-controller-lifecycle) -- VC lifecycle problems
