---
title: "[Solution] UIKit Table View Cell Reuse Identifier Error"
description: "Fix UITableViewCell reuse identifier issues causing blank cells or crashes in UITableView."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit Table View Cell Reuse Identifier Error

This error occurs when the reuse identifier passed to dequeueReusableCell does not match the one registered in the storyboard or code.

## Common Causes
- Reuse identifier typo
- Cell not registered in storyboard or code
- Dequeuing without registering first
- Using wrong identifier for different cell types

## How to Fix
1. Verify the reuse identifier matches exactly between registration and dequeue
2. Register the cell class or nib before dequeuing
3. Use separate identifiers for different cell types

```swift
// Register before use:
tableView.register(UITableViewCell.self, forCellReuseIdentifier: "MyCell")
let cell = tableView.dequeueReusableCell(withIdentifier: "MyCell", for: indexPath)
```

## Examples
```swift
// Cell registration pattern:
func setupTableView() {
    tableView.register(UINib(nibName: "CustomCell", bundle: nil), forCellReuseIdentifier: "CustomCell")
}

func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let cell = tableView.dequeueReusableCell(withIdentifier: "CustomCell", for: indexPath) as! CustomCell
    cell.titleLabel.text = items[indexPath.row]
    return cell
}
```
