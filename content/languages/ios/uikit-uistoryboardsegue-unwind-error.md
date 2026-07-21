---
title: "[Solution] UIKit UIStoryboardSegue Unwind Error"
description: "Fix UIStoryboardSegue unwind segue configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIStoryboardSegue Unwind Error

Unwind segue errors occur when the unwind action method is not properly declared, when the segue identifier does not match, or when the source view controller is not in the navigation stack.

## Common Causes
- Unwind action method not declared
- Segue identifier mismatch
- Source view controller not in stack
- Unwind handler not properly implemented

## How to Fix
1. Declare unwind action method with @IBAction
2. Match segue identifier in Interface Builder
3. Ensure source view controller is in navigation stack
4. Implement unwind handler correctly

```swift
// Unwind action method:
@IBAction func unwindToHome(segue: UIStoryboardSegue) {
    // Handle unwind
}

// Trigger unwind programmatically:
performSegue(withIdentifier: "unwindToHome", sender: nil)
```

## Examples
```swift
// Unwind with data passing:
@IBAction func unwindWithResult(segue: UIStoryboardSegue) {
    guard let sourceVC = segue.source as? ResultViewController else { return }
    result = sourceVC.result
}

// Prepare for unwind:
override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
    if segue.identifier == "unwindWithResult" {
        let destVC = segue.destination as? ResultViewController
        destVC?.result = selectedResult
    }
}
```
