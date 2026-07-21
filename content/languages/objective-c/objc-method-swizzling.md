---
title: "[Solution] Objective-C Method Swizzling"
description: "Method swizzling errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Method Swizzling

Method swizzling errors.

### Common Causes
Wrong method replacement; side effects

### How to Fix
```objc
// Safe swizzling
- (void)load {
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        Class class = [self class];
        Method original = class_getInstanceMethod(class, @selector(viewDidLoad));
        Method swizzled = class_getInstanceMethod(class, @selector(my_viewDidLoad));
        method_exchangeImplementations(original, swizzled);
    });
}
```

### Examples
```objc
- (void)my_viewDidLoad {
    [self my_viewDidLoad];  // calls original
    NSLog(@"viewDidLoad called");
}
```
