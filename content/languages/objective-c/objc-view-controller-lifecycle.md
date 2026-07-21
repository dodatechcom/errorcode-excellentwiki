---
title: "[Solution] VC Lifecycle Error"
description: "ViewController lifecycle errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# VC Lifecycle Error

ViewController lifecycle errors.

### Common Causes
Missing super; wrong method

### How to Fix
```objc
- (void)viewDidLoad {
    [super viewDidLoad];
    // setup
}
- (void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
    // refresh
}
```

### Examples
```objc
- (void)viewDidAppear:(BOOL)animated {
    [super viewDidAppear:animated];
    // analytics
}
```
