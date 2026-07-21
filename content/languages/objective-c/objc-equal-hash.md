---
title: "[Solution] Objective-C Equal/Hash Error"
description: "isEqual and hash not consistent."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Equal/Hash Error

isEqual and hash not consistent.

### Common Causes
hash not overridden when isEqual is

### How to Fix
```objc
- (NSUInteger)hash {
    return [self.name hash] ^ [@(self.age) hash];
}
```

### Examples
```objc
- (BOOL)isEqual:(id)object {
    if (self == object) return YES;
    if (![object isKindOfClass:[self class]]) return NSOrderedSame;
    MyClass *other = (MyClass *)object;
    return [self.name isEqualToString:other.name] && self.age == other.age;
}
```
