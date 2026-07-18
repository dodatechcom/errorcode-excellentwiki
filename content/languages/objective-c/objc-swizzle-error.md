---
title: "[Solution] Objective-C Method Swizzling Failed Error"
description: "Fix Objective-C method swizzling failed errors. Resolve runtime method exchange and implementation issues."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Method swizzling errors occur when attempting to exchange method implementations at runtime fails. This can cause crashes when the swizzled method is called or silent failures where the swizzle does not take effect.

## Why It Happens

- Method does not exist on target class: The method to swizzle is not found.
- Swizzling same method twice causes loop: Double swizzling restores the original implementation.
- Class method swizzled as instance method: The method type does not match.
- Method implementation has wrong signature: The IMP does not match the expected types.
- Swizzling occurs before class is loaded: The class is not yet available at swizzle time.

## How to Fix It

Use method_exchangeImplementations safely:

```objectivec
@implementation UIViewController (Tracking)
+ (void)load {
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        Class class = [self class];
        
        SEL originalSel = @selector(viewWillAppear:);
        SEL swizzledSel = @selector(swizzled_viewWillAppear:);
        
        Method originalMethod = class_getInstanceMethod(class, originalSel);
        Method swizzledMethod = class_getInstanceMethod(class, swizzledSel);
        
        BOOL didAdd = class_addMethod(class, originalSel,
            method_getImplementation(swizzledMethod),
            method_getTypeEncoding(swizzledMethod));
        
        if (didAdd) {
            class_replaceMethod(class, swizzledSel,
                method_getImplementation(originalMethod),
                method_getTypeEncoding(originalMethod));
        } else {
            method_exchangeImplementations(originalMethod, swizzledMethod);
        }
    });
}
@end
```

Check method existence before swizzling:

```objectivec
Method original = class_getInstanceMethod(class, originalSel);
Method swizzled = class_getInstanceMethod(class, swizzledSel);

if (original == NULL || swizzled == NULL) {
    NSLog(@"Method not found for swizzling");
    return;
}
```

Avoid double swizzling:

```objectivec
static BOOL swizzled = NO;
if (swizzled) return;
swizzled = YES;
// Perform swizzle
```

Use dispatch_once for thread safety:

```objectivec
+ (void)load {
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        // Swizzle here - executed only once
    });
}
```

Use class_replaceMethod for safer swizzling:

```objectivec
void swizzledMethod(id self, SEL _cmd) {
    // Swizzled implementation
    NSLog(@"Swizzled method called");
}

Method originalMethod = class_getInstanceMethod(class, originalSel);
class_replaceMethod(class, originalSel, 
    (IMP)swizzledMethod, 
    method_getTypeEncoding(originalMethod));
```

Test swizzled methods thoroughly:

```objectivec
- (void)testSwizzledMethod {
    UIViewController *vc = [[UIViewController alloc] init];
    [vc viewWillAppear:YES];
    // Verify swizzled behavior
}
```

## Common Mistakes

- Swizzling in init instead of +load. +load is called once per class when the class is loaded.
- Not using dispatch_once for one-time setup. Ensure swizzling happens only once.
- Swizzling methods with same name as category. This causes infinite recursion.
- Forgetting that swizzling is permanent for the process lifetime. There is no undo.
- Not testing swizzled methods in all code paths. Test every usage scenario.
- Not considering that swizzling affects all instances of the class.
- Not handling class methods separately from instance methods.

## Related Pages

- [objc-unrecognized-selector]({{< relref "/languages/objective-c/objc-unrecognized-selector" >}}) - unrecognized selector
- [objc-runtime-error]({{< relref "/languages/objective-c/objc-runtime-error" >}}) - runtime errors
- [objc-category-error]({{< relref "/languages/objective-c/objc-category-error" >}}) - category errors
- [objc-exception]({{< relref "/languages/objective-c/objc-exception" >}}) - general exceptions
