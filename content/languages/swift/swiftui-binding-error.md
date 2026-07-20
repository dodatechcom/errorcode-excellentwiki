---
title: "[Solution] SwiftUI Binding Error — @Binding Mismatch & Constants"
description: "Fix SwiftUI binding errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 111
---

SwiftUI binding errors occur when `@Binding` properties aren't properly connected, constant bindings are used incorrectly, or computed bindings produce unexpected results.

## Common Causes

```swift
// Binding type mismatch
struct ParentView: View {
    @State private var isActive = false
    var body: some View {
        ChildView(isOn: $isActive) // Error if type doesn't match
    }
}

struct ChildView: View {
    @Binding var isOn: Bool
}
```

## How to Fix

**1. Match binding types exactly**

```swift
struct ParentView: View {
    @State private var count = 0
    
    var body: some View {
        CounterView(count: $count)
    }
}

struct CounterView: View {
    @Binding var count: Int
    
    var body: some View {
        Button("\(count)") { count += 1 }
    }
}
```

**2. Use constant bindings for preview**

```swift
struct PreviewView: View {
    var body: some View {
        ChildView(isOn: .constant(true))
    }
}
```

**3. Create custom bindings**

```swift
struct ContentView: View {
    @State private var firstName = ""
    @State private var lastName = ""
    
    var fullName: Binding<String> {
        Binding(
            get: { "\(firstName) \(lastName)" },
            set: { newValue in
                let parts = newValue.split(separator: " ")
                firstName = parts.first.map(String.init) ?? ""
                lastName = parts.dropFirst().joined(separator: " ")
            }
        )
    }
    
    var body: some View {
        TextField("Full name", text: fullName)
    }
}
```

**4. Optional bindings with if let**

```swift
struct ParentView: View {
    @State private var selectedItem: Item?
    
    var body: some View {
        if let binding = $selectedItem {
            DetailView(item: binding)
        }
    }
}
```

**5. Two-way bindings with transform**

```swift
struct SettingsView: View {
    @AppStorage("volume") private var volume = 50
    
    var volumeBinding: Binding<Double> {
        Binding(
            get: { Double(volume) },
            set: { volume = Int($0) }
        )
    }
    
    var body: some View {
        Slider(value: volumeBinding, in: 0...100)
    }
}
```

## Examples

Complete binding pattern:
```swift
struct FormView: View {
    @State private var email = ""
    @State private var password = ""
    
    var isValid: Bool {
        email.contains("@") && password.count >= 6
    }
    
    var body: some View {
        Form {
            TextField("Email", text: $email)
            SecureField("Password", text: $password)
            Button("Submit") { submit() }
                .disabled(!isValid)
        }
    }
}
```

## Related Errors

- [Environment Error](/languages/swift/swiftui-environment-error)
- [Observable Error](/languages/swift/swiftui-observable-error)
- [Preference Error](/languages/swift/swiftui-preference-error)
