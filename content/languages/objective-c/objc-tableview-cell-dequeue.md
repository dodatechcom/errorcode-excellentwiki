---
title: "Objective-C UITableViewCell Dequeue Reuse Error"
description: "Fix Objective-C UITableViewCell dequeue errors when cell reuse identifiers do not match or cells are not registered."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Cell reuse identifier mismatch between registration and dequeue
- Cell class does not match registered class/nib
- Dequeueing cell for non-existent reuse identifier
- Not registering cell class or nib before dequeuing
- Using dequeueReusableCellWithIdentifier without forIndexPath

## How to Fix

```objc
// WRONG: No cell registered
UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"MyCell"];
// Returns nil every time

// CORRECT: Register cell class first
[tableView registerClass:[MyCell class] forCellReuseIdentifier:@"MyCell"];
UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"MyCell"
    forIndexPath:indexPath];
```

```objc
// WRONG: Mismatched identifiers
// Registration
[tableView registerClass:[MyCell class] forCellReuseIdentifier:@"Cell"];
// Dequeue
UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"MyCell"];
// Returns nil

// CORRECT: Use same identifier
[tableView registerClass:[MyCell class] forCellReuseIdentifier:@"MyCell"];
UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"MyCell"
    forIndexPath:indexPath];
```

## Examples

```objc
// Example 1: Basic cell registration and dequeue
- (void)viewDidLoad {
    [super viewDidLoad];
    [self.tableView registerClass:[UITableViewCell class]
        forCellReuseIdentifier:@"DefaultCell"];
}

- (UITableViewCell *)tableView:(UITableView *)tableView
    cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"DefaultCell"
        forIndexPath:indexPath];
    cell.textLabel.text = self.data[indexPath.row];
    return cell;
}

// Example 2: Multiple cell types
- (UITableViewCell *)tableView:(UITableView *)tableView
    cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    if (indexPath.row == 0) {
        HeaderCell *cell = [tableView dequeueReusableCellWithIdentifier:@"Header"
            forIndexPath:indexPath];
        return cell;
    }
    ContentCell *cell = [tableView dequeueReusableCellWithIdentifier:@"Content"
        forIndexPath:indexPath];
    return cell;
}
```

## Related Errors

- [UITableViewCell error](objc-uitableviewcell-error) -- cell-related issues
- [UITableView error](objc-uitableview-error) -- table view problems
