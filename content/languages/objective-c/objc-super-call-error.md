---
title: "[Solution] Objective-C Super Call"
description: "Missing or wrong super calls."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Super Call

Missing or wrong super calls.

### Common Causes
Forgot [super viewDidLoad]; wrong method

### How to Fix
```objc
- (void)viewDidLoad {
    [super viewDidLoad];
    // custom setup
}
```

### Examples
```objc
- (void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
    [self refreshData];
}
```
