---
title: "[Solution] Objective-C GCD Error"
description: "Dispatch queue and group errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C GCD Error

Dispatch queue and group errors.

### Common Causes
Wrong queue type; not waiting

### How to Fix
```objc
dispatch_group_t group = dispatch_group_create();
dispatch_group_enter(group);
// async work
dispatch_group_leave(group);
```

### Examples
```objc
dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
// or
dispatch_group_notify(group, dispatch_get_main_queue(), ^{
    NSLog(@"All done");
});
```
