---
title: "[Solution] SwiftUI @StateObject Initialization Error"
description: "Fix SwiftUI @StateObject initialization lifecycle errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @StateObject Initialization Error

StateObject initialization errors occur when the object is not properly initialized, when the initializer has side effects, or when the object is recreated on view updates.

## Common Causes
- Object not initialized properly
- Side effects in initializer
- Object recreated on view updates
- Missing ObservableObject conformance

## How to Fix
1. Initialize object in StateObject
2. Avoid side effects in initializer
3. StateObject preserves object across updates
4. Ensure ObservableObject conformance

```swift
struct ContentView: View {
    @StateObject private var viewModel = MyViewModel()

    var body: some View {
        Text(viewModel.title)
    }
}

class MyViewModel: ObservableObject {
    @Published var title = "Hello"
}
```

## Examples
```swift
// StateObject vs ObservedObject:
// StateObject: Owns the object, creates it once
@StateObject private var vm = MyViewModel()

// ObservedObject: Does not own, receives from parent
@ObservedObject var vm: MyViewModel

// Initialization with parameters:
@StateObject private var vm = MyViewModel(name: "User")
```
