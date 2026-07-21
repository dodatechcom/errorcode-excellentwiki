---
title: "[Solution] SwiftUI @Bindable Property Wrapper Error"
description: "Fix SwiftUI @Bindable property wrapper two-way binding errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @Bindable Property Wrapper Error

Bindable errors occur when the binding is not properly established, when the binding path is incorrect, or when the binding does not update with Observable changes.

## Common Causes
- Binding not established
- Binding path incorrect
- Binding not updating
- Missing @Observable class

## How to Fix
1. Establish binding properly
2. Use correct binding path
3. Ensure binding updates
4. Use @Observable class

```swift
@Observable class FormViewModel {
    var name = ""
    var email = ""
}

struct FormView: View {
    @Bindable var viewModel = FormViewModel()

    var body: some View {
        TextField("Name", text: $viewModel.name)
        TextField("Email", text: $viewModel.email)
    }
}
```

## Examples
```swift
// Bindable with custom binding
@Bindable var viewModel = FormViewModel()

var nameBinding: Binding<String> {
    Binding(
        get: { viewModel.name },
        set: { viewModel.name = $0.uppercased() }
    )
}
```
