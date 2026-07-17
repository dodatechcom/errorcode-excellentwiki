---
title: "[Solution] Objective-C RunLoop Error"
description: "Fix Objective-C NSRunLoop errors and event loop issues"
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["medium"]
weight: 5
---

## What This Error Means
RunLoop errors occur when Objective-C code incorrectly manages the run loop, causing UI freezes, missed events, or memory issues.

## Common Causes
- Performing selector on main thread causing deadlock
- Not removing RunLoop sources before deallocation
- Creating recursive run loop situations
- Incorrect timer scheduling
- Blocking main run loop

## How to Fix
```objectivec
// Schedule timer correctly
NSTimer *timer = [NSTimer scheduledTimerWithTimeInterval:1.0
                                                  target:self
                                                selector:@selector(fire:)
                                                userInfo:nil
                                                 repeats:YES];

// Remove timer properly
- (void)dealloc {
    [self.timer invalidate];
}

// Avoid recursive performSelectorOnMainThread
dispatch_async(dispatch_get_main_queue(), ^{
    [self doWork];
});

// Check if running on main thread
if ([NSThread isMainThread]) {
    [self updateUI];
} else {
    dispatch_async(dispatch_get_main_queue(), ^{
        [self updateUI];
    });
}
```