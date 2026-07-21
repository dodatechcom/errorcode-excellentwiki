---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Accessibility Error"
description: "Fix UICollectionLayoutListConfiguration section header accessibility configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Accessibility Error

Section header accessibility errors occur when accessibility labels are not properly set, when accessibility traits conflict with header behavior, or when accessibility is not properly configured for VoiceOver.

## Common Causes
- Accessibility label not set on header
- Accessibility traits conflicting with behavior
- VoiceOver not properly reading header
- Accessibility elements not properly ordered

## How to Fix
1. Set accessibility label on header
2. Configure accessibility traits properly
3. Test with VoiceOver
4. Order accessibility elements correctly

```swift
header.accessibilityLabel = "Section: \(sections[section].title)"
header.accessibilityTraits = .header
header.isAccessibilityElement = true
```

## Examples
```swift
// Accessible header:
let header = tableView.dequeueReusableHeaderFooterView(withIdentifier: "Header")!
var content = header.defaultContentConfiguration()
content.text = sections[section].title
header.contentConfiguration = content
header.accessibilityLabel = "\(sections[section].title) section"
header.accessibilityTraits = .header
header.isAccessibilityElement = true
```
