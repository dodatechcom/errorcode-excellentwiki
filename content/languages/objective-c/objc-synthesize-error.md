---
title: "[Solution] Objective-C @synthesize Error"
description: "@synthesize usage errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C @synthesize Error

@synthesize usage errors.

### Common Causes
Wrong name; not needed with auto-synthesis

### How to Fix
```objc
@implementation MyClass
@synthesize name = _name;
@end
```

### Examples
```objc
@implementation MyClass
- (NSString *)description {
    return [NSString stringWithFormat:@"MyClass: %@", self.name];
}
@end
```
