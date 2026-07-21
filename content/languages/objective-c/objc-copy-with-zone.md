---
title: "[Solution] Objective-C CopyWithZone"
description: "NSCopying protocol errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C CopyWithZone

NSCopying protocol errors.

### Common Causes
Missing copyWithZone; wrong implementation

### How to Fix
```objc
- (id)copyWithZone:(NSZone *)zone {
    MyClass *copy = [[[self class] allocWithZone:zone] init];
    copy.name = self.name;
    return copy;
}
```

### Examples
```objc
- (id)copyWithZone:(NSZone *)zone {
    MyClass *copy = [[MyClass allocWithZone:zone] init];
    copy->_name = [_name copyWithZone:zone];
    return copy;
}
```
