---
title: "[Solution] Xcode Previews Canvas Error"
description: "Fix Xcode Previews canvas rendering failures for SwiftUI views."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Previews Canvas Error

Previews fail when the preview provider contains errors, when the view depends on external state not provided, or when derived data is corrupt.

## Common Causes
- Preview provider contains compilation errors
- Missing dependencies for preview context
- Derived data corrupted
- Preview requires runtime state not available

## How to Fix
1. Fix all compilation errors in the preview file
2. Provide mock data for preview dependencies
3. Clean derived data and restart Xcode
4. Use preview-specific mock objects

```swift
// Preview with mock data:
struct MyView_Previews: PreviewProvider {
    static var previews: some View {
        MyView(viewModel: MockViewModel())
    }
}

class MockViewModel: ViewModelProtocol {
    var items = ["Preview 1", "Preview 2"]
}
```

## Examples
```swift
// Multiple preview variants:
struct Button_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            MyButton(title: "Primary", style: .primary)
                .previewDisplayName("Primary")
            MyButton(title: "Secondary", style: .secondary)
                .previewDisplayName("Secondary")
            MyButton(title: "Disabled", style: .primary)
                .disabled(true)
                .previewDisplayName("Disabled")
        }
    }
}
```
