---
title: "[Solution] UIKit UITableView Estimated Height Error"
description: "Fix UITableView estimated row height calculation and performance errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UITableView Estimated Height Error

Estimated row height errors occur when the estimated height is too different from the actual height, when it is not set, or when it conflicts with automatic dimension.

## Common Causes
- Estimated height not set
- Estimated height too different from actual
- Conflicts with automatic dimension
- Performance degradation from recalculation

## How to Fix
1. Set estimated row height
2. Keep estimated height close to average actual height
3. Use automatic dimension with proper estimated height
4. Profile performance with Instruments

```swift
// Set estimated row height:
tableView.estimatedRowHeight = 80
tableView.rowHeight = UITableView.automaticDimension

// Or per-section:
tableView.estimatedRowHeight(forSection: 0)
```

## Examples
```swift
// Dynamic cell height:
tableView.estimatedRowHeight = UITableView.automaticDimension
tableView.rowHeight = UITableView.automaticDimension

// Custom estimated height:
func tableView(_ tableView: UITableView, estimatedHeightForRowAt indexPath: IndexPath) -> CGFloat {
    return items[indexPath.row].hasDetail ? 120 : 60
}
```
