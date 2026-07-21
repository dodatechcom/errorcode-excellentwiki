---
title: "[Solution] Objective-C UIImage Error"
description: "UIImage loading and manipulation errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C UIImage Error

UIImage loading and manipulation errors.

### Common Causes
Wrong name; scale; orientation

### How to Fix
```objc
UIImage *img = [UIImage imageNamed:@"photo"];
```

### Examples
```objc
UIImage *img = [UIImage imageNamed:@"photo" inBundle:nil compatibleWithTraitCollection:nil];
```
