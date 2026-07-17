---
title: "[Solution] Objective-C Property Error"
description: "Fix Objective-C property declaration and synthesis errors"
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["medium"]
tags: ["cocoa-touch", "properties", "objective-c-runtime"]
weight: 5
---

## What This Error Means
Property errors occur when Objective-C properties are declared incorrectly or have mismatched ivars, accessors, or memory management semantics.

## Common Causes
- Missing @synthesize or @dynamic directives
- Incorrect property attributes (nonatomic vs atomic)
- Memory management mismatch (strong vs weak)
- Property name collision with ivar
- Accessing ivar directly instead of property

## How to Fix
```objectivec
// Correct property declaration
@property (nonatomic, strong) NSString *name;
@property (nonatomic, weak) id<MyDelegate> delegate;
@property (nonatomic, copy) NSArray *items;

// Use @dynamic for Core Data properties
@dynamic name;

// Access properties through self.property
self.name = @"Value";  // Correct
_name = @"Value";      // Avoid unless in init/dealloc

// Override accessors if needed
- (void)setName:(NSString *)name {
    _name = [name copy];
}
```