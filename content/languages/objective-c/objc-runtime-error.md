---
title: "[Solution] Objective-C Runtime Error"
description: "Fix Objective-C runtime errors including message-sent-to-deallocated-instance and unrecognized-selector"
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["high"]
tags: ["cocoa-touch", "memory-management", "objective-c-runtime"]
weight: 5
---

## What This Error Means
Runtime errors occur when the Objective-C runtime encounters an invalid operation during program execution, typically involving message passing or memory management issues.

## Common Causes
- Sending a message to a nil object
- Calling an undefined method on an object
- Memory corruption from incorrect retain/release cycles
- Accessing deallocated memory
- Mismatched method signatures

## How to Fix
```objectivec
// Check for nil before sending messages
if (object != nil) {
    [object doSomething];
}

// Use respondsToSelector for optional methods
if ([object respondsToSelector:@selector(optionalMethod)]) {
    [object optionalMethod];
}

// Use @try/@catch for exception handling
@try {
    [object riskyOperation];
} @catch (NSException *exception) {
    NSLog(@"Exception: %@", exception.reason);
}
```