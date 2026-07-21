---
title: "[Solution] SwiftUI StateObject Not Updating"
description: "Fix SwiftUI StateObject not triggering view updates when published properties change."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI StateObject Not Updating

StateObject may not trigger view updates if the object is recreated unnecessarily or if the published property change happens off the main thread.

## Common Causes
- Object recreated on every view body evaluation
- Published property updated off main thread
- StateObject used where ObservedObject should be
- Object mutation not going through @Published

## How to Fix
1. Create the StateObject only once using @StateObject
2. Update @Published properties on the main thread
3. Use @ObservedObject for externally created objects
4. Ensure mutations go through @Published properties

```swift
// Correct usage:
struct ParentView: View {
    @StateObject var viewModel = MyViewModel() // Created once

    var body: some View {
        ChildView()
            .environmentObject(viewModel)
    }
}
```

## Examples
```swift
// Thread-safe updates:
class ViewModel: ObservableObject {
    @Published var data: [String] = []

    func fetch() {
        URLSession.shared.dataTask(with: url) { [weak self] data, _, _ in
            DispatchQueue.main.async {
                self?.data = parsedItems  // Must be on main thread
            }
        }.resume()
    }
}
```
