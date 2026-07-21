---
title: "[Solution] Objective-C Dealloc Error"
description: "dealloc errors in ARC."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Dealloc Error

dealloc errors in ARC.

### Common Causes
Missing [super dealloc] (pre-ARC); wrong cleanup

### How to Fix
```objc
// Pre-ARC only
- (void)dealloc {
    [_name release];
    [super dealloc];
}
```

### Examples
```objc
// ARC - remove observers in dealloc
- (void)dealloc {
    [[NSNotificationCenter defaultCenter] removeObserver:self];
}
```
