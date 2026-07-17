---
title: "[Solution] Objective-C Notification Error"
description: "Fix Objective-C NSNotificationCenter errors and observer issues"
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["low"]
weight: 5
---

## What This Error Means
Notification errors occur when posting, observing, or handling NSNotification messages incorrectly, often leading to crashes or memory issues.

## Common Causes
- Posting notification from wrong thread
- Not removing observers (pre-iOS 9)
- Posting notifications with incorrect userInfo format
- Observer deallocated but still registered
- Typo in notification name

## How to Fix
```objectivec
// Remove observers in dealloc (pre-iOS 9)
- (void)dealloc {
    [[NSNotificationCenter defaultCenter] removeObserver:self];
}

// Post notification on main thread
[[NSNotificationCenter defaultCenter] postNotificationName:@"MyNotification"
                                                object:nil
                                              userInfo:@{@"key": @"value"}];

// Register for notifications
[[NSNotificationCenter defaultCenter]
    addObserver:self
       selector:@selector(handleNotification:)
           name:@"MyNotification"
         object:nil];

// Handle notification safely
- (void)handleNotification:(NSNotification *)notification {
    NSDictionary *userInfo = notification.userInfo;
    if (userInfo) {
        NSString *value = userInfo[@"key"];
    }
}
```