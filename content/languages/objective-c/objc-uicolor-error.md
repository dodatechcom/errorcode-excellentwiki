---
title: "[Solution] Objective-C UIColor Error"
description: "UIColor creation errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C UIColor Error

UIColor creation errors.

### Common Causes
Wrong initializer; wrong values

### How to Fix
```objc
UIColor *red = [UIColor colorWithRed:1.0 green:0.0 blue:0.0 alpha:1.0];
UIColor *hex = [UIColor colorWithRed:0.2 green:0.4 blue:0.6 alpha:1.0];
```

### Examples
```objc
UIColor *color = [UIColor colorWithCGColor:cgColor];
```
