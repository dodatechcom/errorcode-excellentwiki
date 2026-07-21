---
title: "[Solution] Objective-C NSArray Error"
description: "NSArray creation and access errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C NSArray Error

NSArray creation and access errors.

### Common Causes
Index out of bounds; wrong initialization

### How to Fix
```objc
NSArray *arr = @[@"a", @"b", @"c"];
NSString *first = arr[0];
```

### Examples
```objc
if (index < arr.count) {
    id obj = arr[index];
} else {
    // handle out of bounds
}
```
