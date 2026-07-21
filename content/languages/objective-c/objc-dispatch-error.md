---
title: "[Solution] Objective-C GCD Error"
description: "Grand Central Dispatch errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C GCD Error

Grand Central Dispatch errors.

### Common Causes
Wrong queue; sync vs async confusion

### How to Fix
```objc
dispatch_async(dispatch_get_main_queue(), ^{
    [self updateUI];
});
```

### Examples
```objc
// Background work
dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
    // long running
    dispatch_async(dispatch_get_main_queue(), ^{
        // update UI
    });
});
```
