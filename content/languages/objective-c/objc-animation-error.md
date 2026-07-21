---
title: "[Solution] Objective-C Animation Error"
description: "UIView animation errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Animation Error

UIView animation errors.

### Common Causes
Wrong block syntax; missing commit

### How to Fix
```objc
[UIView animateWithDuration:0.3 animations:^{
    self.view.alpha = 0.0;
} completion:^(BOOL finished) {
    [self.view removeFromSuperview];
}];
```

### Examples
```objc
[UIView transitionWithView:self.view
    duration:0.3
    options:UIViewAnimationOptionTransitionCrossDissolve
    animations:^{
        self.view.hidden = YES;
    }
    completion:nil];
```
