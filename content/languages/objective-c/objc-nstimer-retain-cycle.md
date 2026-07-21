---
title: "Objective-C NSTimer Retain Cycle Error"
description: "Fix Objective-C NSTimer retain cycle errors when timer retains its target creating memory leaks."
languages: ["objective-c"]
error-types: ["memory-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- NSTimer retains its target, preventing dealloc
- Invalidating timer in dealloc (which is never called due to retain)
- Not invalidating timer when view controller is dismissed
- Repeating timer creates strong reference chain
- Scheduled timer not added to run loop properly

## How to Fix

```objc
// WRONG: Timer retains self, dealloc never called
- (void)viewDidLoad {
    [super viewDidLoad];
    self.timer = [NSTimer scheduledTimerWithTimeInterval:1.0
        target:self selector:@selector(tick) userInfo:nil repeats:YES];
}
// dealloc never called because timer retains self

// CORRECT: Use block-based timer or weak proxy
__weak typeof(self) weakSelf = self;
self.timer = [NSTimer scheduledTimerWithTimeInterval:1.0
    repeats:YES block:^(NSTimer *timer) {
        [weakSelf tick];
    }];
```

```objc
// WRONG: Forgetting to invalidate
- (void)viewDidDisappear:(BOOL)animated {
    [super viewDidDisappear:animated];
    // Timer keeps running!
}

// CORRECT: Invalidate in viewDidDisappear
- (void)viewDidDisappear:(BOOL)animated {
    [super viewDidDisappear:animated];
    [self.timer invalidate];
    self.timer = nil;
}
```

## Examples

```objc
// Example 1: Safe timer with weak proxy
@interface WeakProxy : NSProxy
@property (nonatomic, weak) id target;
@end

@implementation WeakProxy
- (void)forwardInvocation:(NSInvocation *)invocation {
    [invocation invokeWithTarget:self.target];
}
- (NSMethodSignature *)methodSignatureForSelector:(SEL)sel {
    return [(NSObject *)self.target methodSignatureForSelector:sel];
}
@end

// Example 2: Block-based timer
__weak typeof(self) weakSelf = self;
self.timer = [NSTimer scheduledTimerWithTimeInterval:5.0
    repeats:YES block:^(NSTimer *t) {
        [weakSelf doPeriodicWork];
    }];

// Example 3: Clean invalidation
- (void)dealloc {
    [self.timer invalidate];
    self.timer = nil;
}
```

## Related Errors

- [Memory leak error](objc-memory-leak) -- general memory leaks
- [Timer error](objc-runloop-error) -- run loop timer issues
