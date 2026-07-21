---
title: "Objective-C NSNotificationCenter Thread Safety Error"
description: "Fix Objective-C NSNotificationCenter thread safety errors when posting or observing notifications from multiple threads."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Posting notification from background thread while observer expects main thread
- Observer removed on one thread while notification posted on another
- Not using queueWithMainBlock for UI updates in observer
- Posting notification with same name from multiple objects
- Notification center not thread-safe for add/remove during post

## How to Fix

```objc
// WRONG: Updating UI from notification on background thread
- (void)handleDataNotification:(NSNotification *)notification {
    self.label.text = notification.userInfo[@"data"]; // crash!
}

// CORRECT: Dispatch to main thread
- (void)handleDataNotification:(NSNotification *)notification {
    dispatch_async(dispatch_get_main_queue(), ^{
        self.label.text = notification.userInfo[@"data"];
    });
}
```

```objc
// WRONG: Removing observer during notification delivery
- (void)handleNotification:(NSNotification *)notification {
    [[NSNotificationCenter defaultCenter] removeObserver:self];
    // May crash if notification center is iterating observers
}

// CORRECT: Defer removal
- (void)handleNotification:(NSNotification *)notification {
    dispatch_async(dispatch_get_main_queue(), ^{
        [[NSNotificationCenter defaultCenter] removeObserver:self];
    });
}
```

## Examples

```objc
// Example 1: Thread-safe observer
[[NSNotificationCenter defaultCenter]
    addObserverForName:@"DataUpdated"
    object:nil
    queue:[NSOperationQueue mainQueue]
    usingBlock:^(NSNotification *note) {
        [self updateUIWithPayload:note.userInfo];
    }];

// Example 2: Post from background thread
dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
    NSData *data = [self fetchData];
    dispatch_async(dispatch_get_main_queue(), ^{
        [[NSNotificationCenter defaultCenter]
            postNotificationName:@"DataReady"
                          object:self
                        userInfo:@{@"data": data}];
    });
});

// Example 3: Conditional observer
- (void)registerIfNeeded {
    if (!self.isObserving) {
        [[NSNotificationCenter defaultCenter]
            addObserver:self
               selector:@selector(handleEvent:)
                   name:@"Event"
                 object:nil];
        self.isObserving = YES;
    }
}
```

## Related Errors

- [Notification error](objc-notification-leak) -- observer lifecycle issues
- [Thread error](objc-thread-error) -- threading problems
