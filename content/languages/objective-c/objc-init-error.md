---
title: "[Solution] Objective-C Init Error"
description: "Designated initializer errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Init Error

Designated initializer errors.

### Common Causes
Missing self = [super init]; wrong init

### How to Fix
```objc
- (instancetype)initWithName:(NSString *)name {
    self = [super init];
    if (self) {
        _name = [name copy];
    }
    return self;
}
```

### Examples
```objc
- (instancetype)init {
    return [self initWithName:@"Default"];
}
```
