---
title: "[Solution] Objective-C Block Typedef"
description: "Block type definition errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Block Typedef

Block type definition errors.

### Common Causes
Wrong signature; missing typedef

### How to Fix
```objc
typedef void (^CompletionBlock)(BOOL success, NSError *error);
```

### Examples
```objc
- (void)performTaskWithCompletion:(CompletionBlock)completion {
    // do work
    completion(YES, nil);
}
```
