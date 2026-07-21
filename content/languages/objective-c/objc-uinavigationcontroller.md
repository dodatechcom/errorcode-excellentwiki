---
title: "[Solution] UINavigationController Error"
description: "Navigation controller push/pop errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# UINavigationController Error

Navigation controller push/pop errors.

### Common Causes
Wrong animation; nil view controller

### How to Fix
```objc
DetailViewController *detail = [[DetailViewController alloc] init];
[self.navigationController pushViewController:detail animated:YES];
```

### Examples
```objc
[self.navigationController popViewControllerAnimated:YES];
```
