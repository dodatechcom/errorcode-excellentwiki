---
title: "[Solution] Objective-C UIKit Error"
description: "UIKit framework errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C UIKit Error

UIKit framework errors.

### Common Causes
Wrong class; missing delegate; storyboard

### How to Fix
```objc
UILabel *label = [[UILabel alloc] initWithFrame:CGRectMake(10, 10, 200, 40)];
label.text = @"Hello";
[self.view addSubview:label];
```

### Examples
```objc
- (void)viewDidLoad {
    [super viewDidLoad];
    self.tableView.dataSource = self;
    self.tableView.delegate = self;
}
```
