---
title: "[Solution] Objective-C MRC Error"
description: "Fix Objective-C Manual Reference Counting errors in legacy code"
languages: ["objective-c"]
error-types: ["memory-error"]
severities: ["high"]
weight: 5
---

## What This Error Means
MRC errors occur in legacy Objective-C code using manual retain/release, leading to memory leaks or crashes from incorrect reference counting.

## Common Causes
- Missing retain/release calls
- Over-releasing objects
- Not retaining objects stored in collections
- Incorrect autorelease pool usage
- Accessing ivar after release

## How to Fix
```objectivec
// Retain objects you want to keep
self.myObject = [[MyObject alloc] init]; // Retains

// Release in dealloc
- (void)dealloc {
    [_myObject release];
    [super dealloc];
}

// Use autorelease for temporary objects
NSString *temp = [[[NSString alloc] initWithFormat:@"Hello %@", name] autorelease];

// Use NSAutoreleasePool for loops
NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
// Code creating autoreleased objects
[pool drain];
```