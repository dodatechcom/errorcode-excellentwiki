---
title: "[Solution] Objective-C Modal View Error"
description: "Present/dismiss modal errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Modal View Error

Present/dismiss modal errors.

### Common Causes
Missing completion; wrong transition

### How to Fix
```objc
[self presentViewController:modalVC animated:YES completion:nil];
```

### Examples
```objc
[self dismissViewControllerAnimated:YES completion:^{
    NSLog(@"Dismissed");
}];
```
