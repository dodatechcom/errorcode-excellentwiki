---
title: "[Solution] Objective-C NSObject Error"
description: "NSObject method errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C NSObject Error

NSObject method errors.

### Common Causes
init not called; wrong equality

### How to Fix
```objc
- (instancetype)init {
    self = [super init];
    if (self) {
        // initialize
    }
    return self;
}
```

### Examples
```objc
- (BOOL)isEqual:(id)object {
    if (self == object) return YES;
    if (![object isKindOfClass:[self class]]) return NO;
    return [self.name isEqualToString:((MyClass *)object).name];
}
```
