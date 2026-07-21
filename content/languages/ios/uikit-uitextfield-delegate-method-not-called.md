---
title: "[Solution] UIKit UITextField Delegate Method Not Called"
description: "Fix UITextField delegate methods not being triggered in iOS apps."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UITextField Delegate Method Not Called

UITextField delegate methods fail to trigger when the delegate is not set, is deallocated, or when the delegate method signature is incorrect.

## Common Causes
- Delegate property not assigned
- Delegate object deallocated (not retained or weak properly)
- Method signature does not match protocol requirement
- Text field interaction disabled in storyboard

## How to Fix
1. Set the delegate property explicitly
2. Ensure delegate object lifecycle covers the text field
3. Verify method signatures match UITextFieldDelegate exactly
4. Check storyboard text field interaction settings

```swift
// Set delegate properly:
class ViewController: UIViewController, UITextFieldDelegate {
    @IBOutlet weak var textField: UITextField!

    override func viewDidLoad() {
        super.viewDidLoad()
        textField.delegate = self
    }

    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        return true
    }
}
```

## Examples
```swift
// Common delegate methods:
func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
    // Validate input
    return true
}

func textFieldDidBeginEditing(_ textField: UITextField) {
    // Handle editing start
}

func textFieldDidEndEditing(_ textField: UITextField) {
    // Handle editing end
    processInput(textField.text ?? "")
}
```
