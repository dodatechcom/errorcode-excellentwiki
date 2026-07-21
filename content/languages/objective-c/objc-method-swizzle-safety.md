---
title: "Objective-C Method Swizzling Safety Error"
description: "Fix Objective-C method swizzling errors when swizzling methods incorrectly causing unexpected behavior."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Swizzling in wrong load order
- Not calling original implementation
- Swizzling same method twice causing infinite loop
- Swizzling class method instead of instance method
- Swizzled method does not match original signature

## How to Fix

```objc
// WRONG: Swizzling without calling original
Method original = class_getInstanceMethod(self.class, @selector(viewDidLoad));
Method swizzled = class_getInstanceMethod(self.class, @selector(my_viewDidLoad));
method_exchangeImplementations(original, swizzled);

- (void)my_viewDidLoad {
    NSLog(@"swizzled!");
    // Forgot to call original!
}

// CORRECT: Call original via swizzled selector
- (void)my_viewDidLoad {
    [self my_viewDidLoad]; // calls original viewDidLoad
    NSLog(@"after viewDidLoad");
}
```

```enrl
// WRONG: Swizzling twice causes loop
method_exchangeImplementations(m1, m2); // swap
method_exchangeImplementations(m1, m2); // swap back!
// Second swap undoes the first

// CORRECT: Ensure swizzling happens only once
static dispatch_once_t onceToken;
dispatch_once(&onceToken, ^{
    method_exchangeImplementations(original, swizzled);
});
```

## Examples

```objc
// Example 1: Safe swizzling in +load
@implementation UIViewController (Tracking)
+ (void)load {
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        Class class = [self class];
        SEL original = @selector(viewWillAppear:);
        SEL swizzled = @selector(tracked_viewWillAppear:);
        
        Method originalMethod = class_getInstanceMethod(class, original);
        Method swizzledMethod = class_getInstanceMethod(class, swizzled);
        
        BOOL added = class_addMethod(class, original,
            method_getImplementation(swizzledMethod),
            method_getTypeEncoding(swizzledMethod));
        
        if (added) {
            class_replaceMethod(class, swizzled,
                method_getImplementation(originalMethod),
                method_getTypeEncoding(originalMethod));
        } else {
            method_exchangeImplementations(originalMethod, swizzledMethod);
        }
    });
}

- (void)tracked_viewWillAppear:(BOOL)animated {
    [self tracked_viewWillAppear:animated];
    NSLog(@"View appeared: %@", NSStringFromClass([self class]));
}
@end
```

## Related Errors

- [Method swizzling error](objc-method-swizzling) -- swizzling issues
- [Runtime error](objc-runtime-error) -- ObjC runtime problems
