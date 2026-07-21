---
title: "[Solution] SwiftUI @ObservedObject Update Cycle Error"
description: "Fix SwiftUI @ObservedObject update cycle and re-render errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @ObservedObject Update Cycle Error

ObservedObject update cycle errors occur when the object triggers unnecessary updates, when the update causes a cycle, or when the update does not reflect in the UI.

## Common Causes
- Unnecessary updates triggered
- Update cycle causing infinite loop
- Update not reflecting in UI
- Missing @Published property

## How to Fix
1. Minimize published properties
2. Break update cycles
3. Ensure UI reflects updates
4. Use @Published for necessary properties only

```swift
struct ContentView: View {
    @ObservedObject var viewModel: MyViewModel

    var body: some View {
        Text(viewModel.title)
    }
}

class MyViewModel: ObservableObject {
    @Published var title = "Hello"
    @Published var count = 0
}
```

## Examples
```swift
// Avoid update cycles:
class ViewModel: ObservableObject {
    @Published var items: [String] = []
    
    func loadItems() {
        // Do not trigger objectWillChange from within willSet
        items = ["a", "b", "c"]
    }
}

// Use Combine to filter updates:
$title
    .removeDuplicates()
    .assign(to: &$displayTitle)
```
