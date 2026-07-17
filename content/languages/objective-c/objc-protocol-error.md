---
title: "[Solution] Objective-C Protocol Error"
description: "Fix Objective-C protocol conformance and adoption errors"
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["medium"]
weight: 5
---

## What This Error Means
Protocol errors occur when Objective-C classes don't properly implement required protocol methods or incorrectly adopt protocols.

## Common Causes
- Missing required protocol methods
- Typo in method signature
- Protocol not declared in interface
- Required vs optional method confusion
- Protocol method not public in declaration

## How to Fix
```objectivec
// Adopt protocol in interface
@interface MyClass : NSObject <MyProtocol>
@end

// Implement all required methods
@implementation MyClass
- (void)requiredMethod {
    // Implementation
}

- (void)optionalMethod {
    // Optional implementation
}
@end

// Check protocol conformance
if ([object conformsToProtocol:@protocol(MyProtocol)]) {
    [object requiredMethod];
}

// Respond to selector check
if ([object respondsToSelector:@selector(optionalMethod)]) {
    [object optionalMethod];
}
```