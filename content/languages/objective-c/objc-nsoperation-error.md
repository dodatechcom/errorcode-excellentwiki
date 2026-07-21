---
title: "[Solution] Objective-C NSOperation Error"
description: "NSOperation queue errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C NSOperation Error

NSOperation queue errors.

### Common Causes
Missing dependencies; wrong priority

### How to Fix
```objc
NSBlockOperation *op1 = [NSBlockOperation blockOperationWithBlock:^{
    NSLog(@"Task 1");
}];
[[NSOperationQueue mainQueue] addOperation:op1];
```

### Examples
```objc
NSOperationQueue *queue = [[NSOperationQueue alloc] init];
queue.maxConcurrentOperationCount = 3;
[queue addOperationWithBlock:^{
    // background work
}];
```
