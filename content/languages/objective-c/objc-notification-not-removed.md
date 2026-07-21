---
title: "Objective-C NSNotificationCenter Observer Not Removed"
description: "Fix Objective-C NSNotificationCenter errors when notification observers are not removed before deallocation."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Observer not removed in dealloc
- Adding observer with wrong selector signature
- Removing observer for notification never registered
- Using instance selector but notification sent from different thread
- Posting notification with wrong object type in userInfo

## How to Fix

```objc
// WRONG: Not removing notification observer
- (void)viewDidLoad {
    [super viewDidLoad];
    [[NSNotificationCenter defaultCenter]
        addObserver:self selector:@selector(handleNotification:)
        name:@"DataUpdated" object:nil];
}
// Crash if notification posted after dealloc

// CORRECT: Remove in dealloc
- (void)dealloc {
    [[NSNotificationCenter defaultCenter] removeObserver:self];
}
```

```objc
// WRONG: Selector signature mismatch
- (void)handleNotification { // missing parameter!
    // Notification handler expects: (NSNotification *)notification
}

// CORRECT: Match selector signature
- (void)handleNotification:(NSNotification *)notification {
    NSDictionary *userInfo = notification.userInfo;
    // process userInfo
}
```

## Examples

```objc
// Example 1: Basic observer pattern
- (void)viewDidLoad {
    [super viewDidLoad];
    [[NSNotificationCenter defaultCenter]
        addObserver:self
           selector:@selector(appDidBecomeActive:)
               name:UIApplicationDidBecomeActiveNotification
             object:nil];
}

- (void)appDidBecomeActive:(NSNotification *)notification {
    [self refreshData];
}

- (void)dealloc {
    [[NSNotificationCenter defaultCenter] removeObserver:self];
}

// Example 2: Custom notification with userInfo
- (void)postUpdate {
    NSDictionary *data = @{@"key": @"value"};
    [[NSNotificationCenter defaultCenter]
        postNotificationName:@"DataUpdated"
                      object:self
                    userInfo:data];
}
```

## Related Errors

- [Notification error](objc-nsnotification-error) -- notification issues
- [Notification leak](objc-notification-leak) -- observer memory leaks
