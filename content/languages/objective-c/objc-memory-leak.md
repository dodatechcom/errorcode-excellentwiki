---
title: "[Solution] Objective-C Memory Leak"
description: "Object not properly released (pre-ARC)."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Memory Leak

Object not properly released (pre-ARC).

### Common Causes
Missing release/autorelease; retain cycle

### How to Fix
```objc
// Modern ARC handles this
NSString *str = @"Hello";  // ARC manages
```

### Examples
```objc
// Avoid retain cycles with __weak
__weak typeof(self) weakSelf = self;
dispatch_async(dispatch_get_main_queue(), ^{
    [weakSelf updateUI];
});
```
