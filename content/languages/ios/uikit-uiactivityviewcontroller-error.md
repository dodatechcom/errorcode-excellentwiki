---
title: "[Solution] UIKit UIActivityViewController Error"
description: "Fix UIActivityViewController configuration and share sheet errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIActivityViewController Error

Activity view controller fails when the shared items are not properly configured, when excluded activity types conflict, or when the presentation is attempted from a deallocated source.

## Common Causes
- Shared items array contains unsupported types
- Excluded activity types preventing useful sharing
- Presentation from nil source view
- Multiple share sheets trying to present

## How to Fix
1. Use compatible shared item types
2. Selectively exclude activity types
3. Provide valid source view and rect
4. Present one share sheet at a time

```swift
// Share text and image:
let activityVC = UIActivityViewController(activityItems: [text, image], applicationActivities: nil)
activityVC.excludedActivityTypes = [.assignToContact, .saveToCameraRoll]
present(activityVC, animated: true)
```

## Examples
```swift
// Share with custom activities:
class CustomShareActivity: UIActivity {
    override var activityTitle: String? { "Custom Share" }
    override var activityImage: UIImage? { UIImage(systemName: "star") }
    override var activityType: UIActivity.ActivityType? { UIActivity.ActivityType("custom.share") }

    override func perform() {
        // Custom share action
        activityDidFinish(true)
    }
}

let activityVC = UIActivityViewController(activityItems: [shareText], applicationActivities: [CustomShareActivity()])
```
