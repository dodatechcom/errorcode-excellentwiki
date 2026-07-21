---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Interactive Error"
description: "Fix UICollectionLayoutListConfiguration section header interactive configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Interactive Error

Section header interactive errors occur when the header is not properly configured for interaction, when the tap gesture conflicts with the header display, or when the header does not respond to user input.

## Common Causes
- Header not configured for interaction
- Tap gesture conflicts with display
- Header not responding to input
- Header interaction not properly implemented

## How to Fix
1. Configure header for interaction
2. Handle tap gestures properly
3. Ensure header responds to input
4. Implement header interaction handlers

```swift
// Interactive header:
let header = collectionView.dequeueReusableSupplementaryView(ofKind: kind, withReuseIdentifier: "Header", for: indexPath)
let tap = UITapGestureRecognizer(target: self, action: #selector(headerTapped(_:)))
header.addGestureRecognizer(tap)
header.tag = indexPath.section
```

## Examples
```swift
// Header with action:
@objc func headerTapped(_ gesture: UITapGestureRecognizer) {
    guard let section = gesture.view?.tag else { return }
    toggleSection(section)
}
```
