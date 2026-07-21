---
title: "[Solution] Objective-C Autorelease Error"
description: "Autorelease pool errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Autorelease Error

Autorelease pool errors.

### Common Causes
Not draining pool; wrong scope

### How to Fix
```objc
@autoreleasepool {
    // create many temporary objects
    for (int i = 0; i < 100000; i++) {
        NSString *str = [NSString stringWithFormat:@"%d", i];
    }
}
```

### Examples
```objc
// In main.m
@autoreleasepool {
    return UIApplicationMain(argc, argv, nil, NSStringFromClass([AppDelegate class]));
}
```
