---
title: "[Solution] Objective-C Retain Cycle"
description: "Strong reference cycle between objects."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Retain Cycle

Strong reference cycle between objects.

### Common Causes
Block captures self strongly; delegate strong

### How to Fix
```objc
// Break cycle with weak
__weak typeof(self) weakSelf = self;
self.completionBlock = ^{
    [weakSelf doWork];
};
```

### Examples
```objc
@property (nonatomic, weak) id<MyDelegate> delegate;
```
