---
title: "Objective-C GCD Dispatch Queue Deadlock Error"
description: "Fix Objective-C GCD dispatch queue deadlocks when synchronously dispatching to current queue."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Dispatching synchronously to the same serial queue blocks forever
- Using dispatch_sync on main queue from main thread
- Barrier block on wrong queue type
- Nested dispatch_sync creating deadlock chain
- Not using dispatch_async when result needed on main thread

## How to Fix

```objc
// WRONG: Deadlock -- sync to current serial queue
dispatch_queue_t queue = dispatch_queue_create("com.app.serial", DISPATCH_QUEUE_SERIAL);
dispatch_sync(queue, ^{
    dispatch_sync(queue, ^{
        // DEADLOCK: waiting for block to complete while on same queue
    });
});

// CORRECT: Use async for nested dispatch
dispatch_queue_t queue = dispatch_queue_create("com.app.serial", DISPATCH_QUEUE_SERIAL);
dispatch_sync(queue, ^{
    dispatch_async(queue, ^{
        // no deadlock
    });
});
```

```objc
// WRONG: Sync to main queue from main thread
dispatch_sync(dispatch_get_main_queue(), ^{
    self.label.text = @"Updated"; // deadlock if called from main
});

// CORRECT: Check if already on main thread
if ([NSThread isMainThread]) {
    self.label.text = @"Updated";
} else {
    dispatch_sync(dispatch_get_main_queue(), ^{
        self.label.text = @"Updated";
    });
}
```

## Examples

```objc
// Example 1: Async to avoid deadlock
dispatch_async(queue, ^{
    // safe nested dispatch
    dispatch_async(queue, ^{
        // works fine
    });
});

// Example 2: Barrier for reader-writer pattern
dispatch_queue_t concurrentQueue = dispatch_queue_create("com.app.concurrent",
    DISPATCH_QUEUE_CONCURRENT);
dispatch_barrier_async(concurrentQueue, ^{
    // exclusive write
});
dispatch_async(concurrentQueue, ^{
    // concurrent reads
});

// Example 3: Dispatch group for synchronization
dispatch_group_t group = dispatch_group_create();
dispatch_group_enter(group);
[someService fetchWithCompletion:^(NSData *data) {
    // process data
    dispatch_group_leave(group);
}];
dispatch_group_notify(group, dispatch_get_main_queue(), ^{
    // all done
});
```

## Related Errors

- [GCD error](objc-gcd-error) -- Grand Central Dispatch issues
- [Thread error](objc-thread-error) -- threading problems
