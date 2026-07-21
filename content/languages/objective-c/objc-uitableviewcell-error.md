---
title: "[Solution] Objective-C UITableViewCell Error"
description: "UITableViewCell reuse errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C UITableViewCell Error

UITableViewCell reuse errors.

### Common Causes
Wrong identifier; not dequeuing

### How to Fix
```objc
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    static NSString *CellIdentifier = @"Cell";
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    if (!cell) {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:CellIdentifier];
    }
    return cell;
}
```

### Examples
```objc
// Register class first
[self.tableView registerClass:[UITableViewCell class] forCellReuseIdentifier:@"Cell"];
```
