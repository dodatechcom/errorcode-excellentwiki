---
title: "[Solution] Objective-C Block Capture"
description: "Block capturing variables incorrectly."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Block Capture

Block capturing variables incorrectly.

### Common Causes
By-value capture; needs __block for mutation

### How to Fix
```objc
__block int counter = 0;
void (^inc)(void) = ^{
    counter++;
};
inc();  // counter is 1
```

### Examples
```objc
int x = 10;
void (^printX)(void) = ^{
    NSLog(@"%d", x);  // captured by value
};
```
