---
title: "[Solution] Objective-C Description Error"
description: "description method not overridden."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Description Error

description method not overridden.

### Common Causes
Default description not useful

### How to Fix
```objc
- (NSString *)description {
    return [NSString stringWithFormat:@"%@: %@", NSStringFromClass([self class]), self.name];
}
```

### Examples
```objc
- (NSString *)debugDescription {
    return [NSString stringWithFormat:@"<%@: %p> name=%@", 
        NSStringFromClass([self class]), self, self.name];
}
```
