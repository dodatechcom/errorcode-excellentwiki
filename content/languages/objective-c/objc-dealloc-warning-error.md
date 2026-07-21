---
title: "Objective-C UIViewController Dealloc Warning Error"
description: "Fix Objective-C UIViewController dealloc warnings when dealloc is not properly implemented or is missing."
languages: ["objective-c"]
error-types: ["compile-error"]
severities: ["warning"]
weight: 5
---

## Common Causes

- Dealloc called but not calling [super dealloc] (pre-ARC)
- Property observers accessing deallocated objects
- Performing UI operations in dealloc
- Not removing KVO observers or notification observers in dealloc
- Circular strong references prevent dealloc from being called

## How to Fix

```objc
// WRONG: UI operations in dealloc
- (void)dealloc {
    [self.view removeFromSuperview]; // avoid
    self.delegate = nil;
}

// CORRECT: Minimal dealloc
- (void)dealloc {
    [[NSNotificationCenter defaultCenter] removeObserver:self];
}
```

```objc
// WRONG: Missing dealloc leads to observer leak
- (void)viewDidLoad {
    [super viewDidLoad];
    [self.model addObserver:self forKeyPath:@"status" options:0 context:nil];
}
// No dealloc -- observer never removed

// CORRECT: Clean up in dealloc
- (void)dealloc {
    [self.model removeObserver:self forKeyPath:@"status"];
}
```

## Examples

```objc
// Example 1: Proper dealloc with observers
- (void)dealloc {
    [[NSNotificationCenter defaultCenter] removeObserver:self];
    [self.model removeObserver:self forKeyPath:@"status"];
    [self.timer invalidate];
}

// Example 2: ARC dealloc (no [super dealloc])
- (void)dealloc {
    // ARC handles [super dealloc] automatically
    // Just clean up non-memory resources
    [self.urlSession invalidateAndCancel];
}

// Example 3: Debug dealloc
#ifdef DEBUG
- (void)dealloc {
    NSLog(@"%@ dealloced", NSStringFromClass([self class]));
}
#endif
```

## Related Errors

- [Memory leak error](objc-memory-leak) -- memory management issues
- [Memory warning](memory-warning) -- memory pressure
