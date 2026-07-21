---
title: "Objective-C Block Circular Reference Error"
description: "Fix Objective-C block retain cycles when blocks capture self strongly creating memory leaks."
languages: ["objective-c"]
error-types: ["memory-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Block captures `self` strongly in property assignment
- Nested blocks each retaining self creating deep cycles
- Block stored in property of self
- GCD block captures self without __weak reference
- Completion block retains view controller indefinitely

## How to Fix

```objc
// WRONG: Block captures self strongly
self.completionBlock = ^{
    [self doSomething]; // retain cycle: self -> block -> self
};

// CORRECT: Use __weak reference
__weak typeof(self) weakSelf = self;
self.completionBlock = ^{
    __strong typeof(weakSelf) strongSelf = weakSelf;
    if (strongSelf) {
        [strongSelf doSomething];
    }
};
```

```objc
// WRONG: Nested blocks both capturing self
self.handler = ^{
    dispatch_async(dispatch_get_main_queue(), ^{
        [self updateUI]; // strong capture in nested block
    });
};

// CORRECT: Weak reference in outer block
__weak typeof(self) weakSelf = self;
self.handler = ^{
    dispatch_async(dispatch_get_main_queue(), ^{
        [weakSelf updateUI];
    });
};
```

## Examples

```objc
// Example 1: Network completion block
__weak typeof(self) weakSelf = self;
[[NSURLSession sharedSession] dataTaskWithRequest:request
    completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
        __strong typeof(weakSelf) self = weakSelf;
        if (!self) return;
        [self processData:data];
    }];

// Example 2: Timer block
__weak typeof(self) weakSelf = self;
self.timer = [NSTimer scheduledTimerWithTimeInterval:1.0 repeats:YES block:^(NSTimer *timer) {
    [weakSelf tick];
}];

// Example 3: Property with block
typedef void(^VoidBlock)(void);
@property (nonatomic, copy) VoidBlock onAction;
```

## Related Errors

- [Memory leak error](objc-memory-leak) -- retain cycle detection
- [Block cycle error](objc-block-cycle) -- block-specific cycles
