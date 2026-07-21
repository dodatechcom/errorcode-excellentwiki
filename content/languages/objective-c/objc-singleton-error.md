---
title: "[Solution] Objective-C Singleton Pattern"
description: "Singleton implementation errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Singleton Pattern

Singleton implementation errors.

### Common Causes
Thread safety; multiple instances

### How to Fix
```objc
+ (instancetype)sharedInstance {
    static MyClass *instance = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        instance = [[MyClass alloc] init];
    });
    return instance;
}
```

### Examples
```objc
// Use dispatch_once for thread safety
+ (instancetype)shared {
    static id sharedInstance = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        sharedInstance = [[self alloc] initPrivate];
    });
    return sharedInstance;
}
```
