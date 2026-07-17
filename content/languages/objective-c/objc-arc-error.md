---
title: "[Solution] Objective-C ARC Error"
description: "Fix Objective-C Automatic Reference Counting compilation and runtime errors"
languages: ["objective-c"]
error-types: ["memory-error"]
severities: ["high"]
weight: 5
---

## What This Error Means
ARC errors occur when Objective-C code violates Automatic Reference Counting rules or has incorrect memory management patterns.

## Common Causes
- Using retain/release/autorelease under ARC
- Incorrect bridge casts between ObjC and Core Foundation
- Assigning to ivar without proper ownership
- Mixing ARC and non-ARC code
- Circular strong references

## How to Fix
```objectivec
// Don't call retain/release under ARC
// [object retain];  // WRONG
// [object release]; // WRONG

// Use proper bridge casts
CFStringRef cfString = (__bridge_retained CFStringRef)nsString; // +1 ref
CFRelease(cfString); // Balance

// Use weak for delegates
@property (nonatomic, weak) id<MyDelegate> delegate;

// Use __block to avoid retain cycles in blocks
__block id weakSelf = self;
self.block = ^{
    id strongSelf = weakSelf;
    [strongSelf doWork];
};
```