---
title: "[Solution] Objective-C Retain Cycle in Block Strong Reference"
description: "Fix Objective-C retain cycles in blocks. Use weak references and avoid strong self captures in blocks."
languages: ["objective-c"]
error-types: ["memory-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Retain cycles in blocks occur when a block captures self strongly, and self retains the block. This creates a circular reference preventing deallocation and causing memory leaks.

## Why It Happens

- Block captures self without __weak: The block holds a strong reference to self.
- Block stored as property on capturing object: The object owns the block that owns the object.
- Cyclic reference between parent and child objects: Parent retains child, child retains parent.
- Timer retains block that captures controller: NSTimer holds strong reference to its block.
- Notification block captures self strongly: Block-based notification observers capture self.

## How to Fix It

Use weak-strong dance in blocks:

```objectivec
__weak typeof(self) weakSelf = self;

self.completionBlock = ^{
    __strong typeof(weakSelf) strongSelf = weakSelf;
    if (strongSelf) {
        [strongSelf doSomething];
    }
};
```

Break cycles in dealloc:

```objectivec
- (void)dealloc {
    self.completionBlock = nil;
    [self.timer invalidate];
}
```

Use NSTimer carefully:

```objectivec
__weak typeof(self) weakSelf = self;
self.timer = [NSTimer scheduledTimerWithTimeInterval:1.0
    repeats:YES
    block:^(NSTimer *timer) {
        [weakSelf fire:timer];
    }];
```

Use proxy objects for delegate patterns:

```objectivec
// Weak reference proxy for delegates
@interface WeakDelegateProxy : NSProxy
@property (nonatomic, weak) id delegate;
@end
```

Analyze with Instruments:

```
// Use Leaks instrument to find retain cycles
// Use Allocations instrument to track memory usage
```

Analyze with Instruments:

```
// Use Leaks instrument to find retain cycles
// Use Allocations instrument to track memory usage
```

Use Xcode's Memory Graph Debugger:

```
// Click Debug Memory Graph in Xcode
// This visualizes object relationships and retain cycles
```

## Common Mistakes

- Using __weak without nil check in block. Always check for nil before using weak references.
- Creating strong reference cycle in child-to-parent. Use weak delegates.
- Forgetting that collections retain their elements. Arrays and dictionaries hold strong references.
- Not invalidating timers in dealloc. Timers retain their target.
- Not considering that blocks captured by GCD retain their captures. dispatch_async retains its block.
- Not cleaning up notification observers in dealloc. Notifications can cause retain cycles.
- Using unsafe_unretained instead of weak. unsafe_unretained does not zero out on dealloc.

## Related Pages

- [objc-notification-leak]({{< relref "/languages/objective-c/objc-notification-leak" >}}) - notification leak
- [objc-memory-error]({{< relref "/languages/objective-c/objc-memory-error" >}}) - memory errors
- [objc-excbadaccess]({{< relref "/languages/objective-c/objc-excbad-access" >}}) - EXC_BAD_ACCESS
- [objc-coreanimation-error]({{< relref "/languages/objective-c/objc-coreanimation-error" >}}) - Core Animation errors
