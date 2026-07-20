---
title: "[Solution] SwiftUI.StateObject: Missing @StateObject initialization"
description: "Fix SwiftUI StateObject missing initialization errors. Learn why @StateObject must be initialized with a struct conforming to ObservableObject and how to resolve it."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "swift"
tags: ["swift", "swiftui", "stateobject", "observable-object"]
severity: "error"
---

# SwiftUI.StateObject: Missing @StateObject initialization

## Error Message

```
StateObject' initializer 'init(wrappedValue:_:)' requires that 'ViewModel' conform to 'ObservableObject'
```

## Common Causes

- Using @StateObject with a type that does not conform to ObservableObject
- Forgetting to assign a concrete type when @StateObject is used with a protocol
- Declaring @StateObject without providing an initial value in the view body

## Solutions

### Solution 1: Ensure the wrapped value conforms to ObservableObject

Mark the class backing your @StateObject with the ObservableObject protocol and publish changes using @Published.

```swift
class UserViewModel: ObservableObject {
    @Published var username: String = ""
    @Published var isLoggedIn: Bool = false

    func login(username: String) {
        self.username = username
        self.isLoggedIn = true
    }
}

struct ProfileView: View {
    @StateObject private var viewModel = UserViewModel()

    var body: some View {
        VStack {
            Text("Welcome, \(viewModel.username)")
            Button("Log In") {
                viewModel.login(username: "swift_dev")
            }
        }
    }
}
```

### Solution 2: Initialize @StateObject only once using @StateObject

Use @StateObject so that SwiftUI owns the lifecycle. Do not create the object inside a @Binding or pass a pre-existing reference.

```swift
struct SettingsView: View {
    @StateObject private var settings = AppSettings()

    var body: some View {
        Form {
            Toggle("Dark Mode", isOn: $settings.isDarkMode)
            Toggle("Notifications", isOn: $settings.notificationsEnabled)
        }
    }
}
```

### Solution 3: Use @ObservedObject for externally owned objects

If the view does not own the object, use @ObservedObject instead. @StateObject is only for objects the view creates itself.

```swift
// Parent view owns the ViewModel
struct ParentView: View {
    @StateObject private var viewModel = SharedViewModel()

    var body: some View {
        ChildView(viewModel: viewModel)
    }
}

struct ChildView: View {
    @ObservedObject var viewModel: SharedViewModel

    var body: some View {
        Text("Data: \(viewModel.data)")
    }
}
```

## Prevention Tips

- Always make @StateObject wrapped types conform to ObservableObject
- Use @Published inside ObservableObject classes to trigger view updates
- Prefer @StateObject over @ObservedObject when the view creates the object
- Initialize @StateObject at declaration time to avoid unnecessary re-creation

## Related Errors

- [SwiftUI navigation error]({{< relref "/languages/swift/swiftui-navigation-error" >}})
- [SwiftUI list error]({{< relref "/languages/swift/swiftui-list-error" >}})
- [Combine error]({{< relref "/languages/swift/combine-error" >}})
