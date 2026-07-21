---
title: "[Solution] Objective-C Extended Category"
description: "Category with no new methods."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Extended Category

Category with no new methods.

### Common Causes
Empty category; not useful

### How to Fix
```objc
// Add methods to existing class
@interface NSArray (SafeAccess)
- (id)safeObjectAtIndex:(NSUInteger)index;
@end
```

### Examples
```objc
@implementation NSArray (SafeAccess)
- (id)safeObjectAtIndex:(NSUInteger)index {
    if (index < self.count) return self[index];
    return nil;
}
@end
```
