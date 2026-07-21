---
title: "[Solution] NSString Format Error"
description: "Format string errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# NSString Format Error

Format string errors.

### Common Causes
Wrong specifier; missing arguments

### How to Fix
```objc
NSString *str = [NSString stringWithFormat:@"Hello %@, age %d", name, age];
```

### Examples
```objc
// Use correct specifiers
NSString *str = [NSString stringWithFormat:@"Name: %@, Age: %ld, Score: %.2f", 
    name, (long)age, score];
```
