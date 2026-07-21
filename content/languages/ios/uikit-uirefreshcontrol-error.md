---
title: "[Solution] UIKit UIRefreshControl Error"
description: "Fix UIRefreshControl pull-to-refresh configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIRefreshControl Error

Refresh control fails to appear when not properly configured, when the scrollView content is too short, or when the end refreshing call is missing.

## Common Causes
- Refresh control not added to scrollView
- Content too short for pull-to-refresh
- End refreshing not called after data load
- Refresh control tint color not visible

## How to Fix
1. Add refresh control to the scrollView
2. Ensure content is long enough to pull
3. Call endRefreshing when data load completes
4. Set tintColor to match your theme

```swift
let refreshControl = UIRefreshControl()
refreshControl.addTarget(self, action: #selector(refresh), for: .valueChanged)
scrollView.refreshControl = refreshControl

@objc func refresh() {
    loadData { [weak self] in
        self?.scrollView.refreshControl?.endRefreshing()
    }
}
```

## Examples
```swift
// Table view refresh:
func setupRefreshControl() {
    tableView.refreshControl = UIRefreshControl()
    tableView.refreshControl?.attributedTitle = NSAttributedString(string: "Pull to refresh")
    tableView.refreshControl?.addTarget(self, action: #selector(handleRefresh), for: .valueChanged)
}

@objc func handleRefresh() {
    fetchNewData()
}
```
