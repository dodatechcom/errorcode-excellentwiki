---
title: "[Solution] Objective-C @dynamic Error"
description: "@dynamic property not implemented."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C @dynamic Error

@dynamic property not implemented.

### Common Causes
Missing implementation; dynamic binding

### How to Fix
```objc
@interface MyClass : NSObject
@property (nonatomic, strong) NSString *name;
@end

@implementation MyClass
@dynamic name;
@end
```

### Examples
```objc
// If dynamic, must provide getter/setter at runtime
- (NSString *)name {
    return objc_getAssociatedObject(self, @selector(name));
}
```
