---
title: "[Solution] Objective-C Message Error"
description: "Fix Objective-C unrecognized-selector and message-sent-to-deallocated-instance errors"
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["high"]
weight: 5
---

## What This Error Means
Message errors occur when an Objective-C object receives a message it cannot respond to, or when memory has been freed before the message arrives.

## Common Causes
- Calling a method not declared in the object's interface
- Typo in method name
- Using a protocol without implementing required methods
- Object deallocated before message delivery
- Incorrect method signature between declaration and implementation

## How to Fix
```objectivec
// Declare methods in header file
@interface MyClass : NSObject
- (void)myMethod;
@end

// Verify protocol conformance
@interface MyClass : NSObject <MyProtocol>
// Must implement all required @protocol methods
@end

// Use performSelector for dynamic dispatch
if ([object respondsToSelector:@selector(myMethod)]) {
    [object performSelector:@selector(myMethod)];
}
```