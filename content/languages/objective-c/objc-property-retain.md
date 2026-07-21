---
title: "[Solution] Objective-C Property Retain"
description: "Property memory management errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Property Retain

Property memory management errors.

### Common Causes
Wrong attribute; mismatched getter/setter

### How to Fix
```objc
// ARC - use strong or weak
@property (nonatomic, strong) NSString *name;
@property (nonatomic, weak) id<MyDelegate> delegate;
```

### Examples
```objc
// Manual reference counting (pre-ARC)
- (void)setName:(NSString *)newName {
    [newName retain];
    [_name release];
    _name = newName;
}
```
