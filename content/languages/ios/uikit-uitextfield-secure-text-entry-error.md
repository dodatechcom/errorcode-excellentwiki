---
title: "[Solution] UIKit UITextField Secure Text Entry Error"
description: "Fix UITextField secure text entry and password field configuration errors."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UITextField Secure Text Entry Error

Secure text entry errors occur when the secure text entry is toggled incorrectly, when the text field does not properly mask input, or when autocorrect interferes with password fields.

## Common Causes
- isSecureTextEntry toggled without updating UI
- Autocorrect enabled on password field
- Text field reused for both secure and non-secure input
- Placeholder text visible in secure fields

## How to Fix
1. Set isSecureTextEntry at initialization
2. Disable autocorrect on password fields
3. Use separate text fields for secure and non-secure input
4. Configure placeholder appropriately for secure fields

```swift
// Password text field:
let passwordField = UITextField()
passwordField.isSecureTextEntry = true
passwordField.autocorrectionType = .no
passwordField.autocapitalizationType = .none
passwordField.textContentType = .password
```

## Examples
```swift
// Secure text field with toggle:
func toggleSecureEntry() {
    let wasFirstResponder = passwordField.isFirstResponder
    passwordField.resignFirstResponder()
    passwordField.isSecureTextEntry.toggle()
    if wasFirstResponder {
        passwordField.becomeFirstResponder()
    }
}

// Modern password field (iOS 15+):
let passwordField = UITextField()
passwordField.textContentType = .newPassword
passwordField.passwordRules = UITextInputPasswordRules(descriptor: "required: upper; required: lower; required: digit; max-length: 20;")
```
