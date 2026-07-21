---
title: "[Solution] UIKit UITableView Section Header Configuration Error"
description: "Fix UITableView section header view configuration and sizing errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UITableView Section Header Configuration Error

Section header configuration errors occur when the header view is not properly configured, when the header height does not match the design, or when the header is not displayed due to incorrect delegate implementation.

## Common Causes
- Header view not properly configured
- Header height not matching design
- Delegate method returning wrong height
- Header not registered for reuse

## How to Fix
1. Configure header view content properly
2. Return correct height from delegate
3. Register header for reuse
4. Use estimated heights when possible

```swift
func tableView(_ tableView: UITableView, viewForHeaderInSection section: Int) -> UIView? {
    let header = tableView.dequeueReusableHeaderFooterView(withIdentifier: "Header") as! SectionHeaderView
    header.title = sections[section].title
    return header
}

func tableView(_ tableView: UITableView, heightForHeaderInSection section: Int) -> CGFloat {
    return 44
}
```

## Examples
```swift
// Modern section header with UIListContentConfiguration:
func tableView(_ tableView: UITableView, viewForHeaderInSection section: Int) -> UIView? {
    let header = tableView.dequeueReusableHeaderFooterView(withIdentifier: "Header")!
    var content = header.defaultContentConfiguration()
    content.text = sections[section].title
    header.contentConfiguration = content
    return header
}
```
