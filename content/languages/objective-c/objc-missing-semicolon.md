---
title: "[Solution] Objective-C Missing Semicolon"
description: "Statement missing trailing semicolon."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Missing Semicolon

Statement missing trailing semicolon.

### Common Causes
Forgot semicolon at end of line

### How to Fix
```objc
// Wrong
int x = 5
// Correct
int x = 5;
```

### Examples
```objc
NSString *message = @"Hello";
NSLog(@"%@", message);
```
