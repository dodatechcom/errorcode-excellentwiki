---
title: "[Solution] Objective-C Unrecognized Selector Error"
description: "Fix Objective-C unrecognized selector sent to instance. Resolve method dispatch and dynamic invocation issues."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `unrecognized selector sent to instance` error occurs when Objective-C attempts to call a method that does not exist on an object. The runtime cannot find a matching implementation in the method dispatch table or through dynamic resolution.

## Why It Happens

- Method name typo in message send: The selector name is misspelled.
- Method defined in category but not linked: The category file is not included in the build.
- Protocol method not implemented: The object claims to conform to a protocol but does not implement required methods.
- Dynamic method resolution failed: The runtime cannot resolve the method through any mechanism.
- Method removed during refactoring: The method was deleted but callers were not updated.

## How to Fix It

Implement `doesNotRecognizeSelector:` for custom handling:

```objectivec
- (void)doesNotRecognizeSelector:(SEL)selector {
    NSLog(@"Unrecognized selector: %@", NSStringFromSelector(selector));
    [super doesNotRecognizeSelector:selector];
}
```

Use `respondsToSelector:` before calling:

```objectivec
if ([self respondsToSelector:@selector(targetMethod:)]) {
    [self targetMethod:@"value"];
} else {
    NSLog(@"Method not available");
}
```

Check protocol conformance:

```objectivec
if ([object conformsToProtocol:@protocol(MyProtocol)]) {
    [object protocolMethod];
} else {
    NSLog(@"Object does not conform to protocol");
}
```

Use `performSelector:` with error handling:

```objectivec
SEL selector = NSSelectorFromString(@"methodName");
if ([object respondsToSelector:selector]) {
    IMP imp = [object methodForSelector:selector];
    imp(object, selector, argument);
}
```

Use `objc_msgSend` carefully for dynamic dispatch:

```objectivec
#import <objc/message.h>

// Only use with proper type casting
((void (*)(id, SEL, id))objc_msgSend)(object, selector, argument);
```

Use performSelector:withObject: for dynamic calls:

```objectivec
SEL selector = NSSelectorFromString(@"methodWithName:");
if ([object respondsToSelector:selector]) {
    [object performSelector:selector withObject:@"argument"];
}
```

Handle protocol optional methods:

```objectivec
@protocol MyProtocol <NSObject>
@required
- (void)requiredMethod;
@optional
- (void)optionalMethod;
@end

if ([object respondsToSelector:@selector(optionalMethod)]) {
    [object optionalMethod];
}
```

Use method signature for complex invocations:

```objectivec
NSMethodSignature *signature = [object methodSignatureForSelector:selector];
if (signature) {
    NSInvocation *invocation = [NSInvocation 
        invocationWithMethodSignature:signature];
    [invocation setTarget:object];
    [invocation setSelector:selector];
    [invocation invoke];
}
```

## Common Mistakes

- Not linking category files in build phases. Categories must be compiled and linked.
- Forgetting to declare methods in header files. Methods should be declared in the interface or protocol.
- Using string-based selectors that can break at runtime. Use @selector() syntax instead.
- Not implementing all required protocol methods. Check protocol documentation for required vs optional methods.
- Assuming method exists because it works in one context but not another.
- Not using respondsToSelector: before performSelector: for safety.

## Related Pages

- [objc-kvc-error]({{< relref "/languages/objective-c/objc-kvc-error" >}}) - key not found
- [objc-message-error]({{< relref "/languages/objective-c/objc-message-error" >}}) - message send error
- [objc-exception]({{< relref "/languages/objective-c/objc-exception" >}}) - general exception
- [objc-swizzle-error]({{< relref "/languages/objective-c/objc-swizzle-error" >}}) - swizzling errors
