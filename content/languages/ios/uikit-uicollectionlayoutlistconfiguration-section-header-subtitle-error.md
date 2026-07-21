---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Subtitle Error"
description: "Fix UICollectionLayoutListConfiguration section header subtitle configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Subtitle Error

Section header subtitle errors occur when the subtitle is not properly configured, when the subtitle conflicts with the title, or when the subtitle is not visible due to layout issues.

## Common Causes
- Subtitle not configured properly
- Subtitle conflicts with title
- Subtitle not visible
- Subtitle not updating with content changes

## How to Fix
1. Configure subtitle properly
2. Ensure subtitle does not conflict with title
3. Verify subtitle visibility
4. Update subtitle with content changes

```swift
var content = UIListContentConfiguration.subtitleHeader()
content.text = "Section Title"
content.secondaryText = "Subtitle text"
header.contentConfiguration = content
```

## Examples
```swift
// Header with subtitle:
var content = UIListContentConfiguration.subtitleHeader()
content.text = "Messages"
content.secondaryText = "12 unread"
content.textProperties.font = .preferredFont(forTextStyle: .headline)
content.secondaryTextProperties.font = .preferredFont(forTextStyle: .subheadline)
content.secondaryTextProperties.color = .secondaryLabel
header.contentConfiguration = content
```
