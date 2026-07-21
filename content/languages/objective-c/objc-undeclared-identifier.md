---
title: "[Solution] Objective-C Undeclared Identifier"
description: "Variable or method not declared."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Undeclared Identifier

Variable or method not declared.

### Common Causes
Missing import; typo; wrong scope

### How to Fix
```objc
#import <Foundation/Foundation.h>
```

### Examples
```objc
@interface MyClass : NSObject
- (void)myMethod;
@end
```
