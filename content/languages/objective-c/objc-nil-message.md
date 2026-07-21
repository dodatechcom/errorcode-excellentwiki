---
title: "[Solution] Objective-C Nil Message"
description: "Sending message to nil."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Nil Message

Sending message to nil.

### Common Causes
Object not initialized; released too early

### How to Fix
```objc
if (obj != nil) {
    [obj doSomething];
}
```

### Examples
```objc
// In ARC, messaging nil is safe (returns nil/0)
NSString *result = [nil uppercaseString];  // result is nil
```
