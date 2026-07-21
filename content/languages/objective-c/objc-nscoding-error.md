---
title: "[Solution] Objective-C NSCoding Error"
description: "NSCoding protocol errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C NSCoding Error

NSCoding protocol errors.

### Common Causes
Missing encode/decode; wrong keys

### How to Fix
```objc
- (void)encodeWithCoder:(NSCoder *)coder {
    [coder encodeObject:self.name forKey:@"name"];
    [coder encodeInteger:self.age forKey:@"age"];
}
```

### Examples
```objc
- (instancetype)initWithCoder:(NSCoder *)coder {
    self = [super init];
    if (self) {
        _name = [coder decodeObjectForKey:@"name"];
        _age = [coder decodeIntegerForKey:@"age"];
    }
    return self;
}
```
