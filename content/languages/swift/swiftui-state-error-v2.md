---
title: "[Solution] SwiftUI @State Mutation Error Fix"
description: "Fix SwiftUI @State property wrapper mutation errors."
languages: ["swift"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SwiftUI: @State Mutation Error Fix

A SwiftUI @State mutation error occurs when you try to modify a @State property from outside its owning view or in an invalid context.

## What This Error Means

`@State` properties are managed by SwiftUI and can only be mutated within the view that owns them. Modifying @State from a different view or from a non-main-actor context causes runtime errors or warnings.

## Common Causes

- Modifying @State from a child view
- Setting @State in async context without MainActor
- Using @State on reference types
- Trying to mutate @State in view initializer

## How to Fix

### 1. Use @Binding for child views

```swift
// WRONG: Child tries to modify parent's @State
struct ChildView: View {
    @State var count = 0  // Separate state

    var body: some View {
        Button("Tap") { count += 1 }
    }
}

// CORRECT: Use @Binding
struct ChildView: View {
    @Binding var count: Int

    var body: some View {
        Button("Tap") { count += 1 }
    }
}

struct ParentView: View {
    @State private var count = 0

    var body: some View {
        ChildView(count: $count)
    }
}
```

### 2. Use MainActor for async updates

```swift
// WRONG: Modifying @State from background
func loadData() {
    Task {
        let data = await fetchFromAPI()
        count = data.count  // Warning: mutation from non-isolated context
    }
}

// CORRECT: Dispatch to MainActor
func loadData() {
    Task {
        let data = await fetchFromAPI()
        await MainActor.run {
            count = data.count
        }
    }
}
```

### 3. Use @ObservedObject for reference types

```swift
// WRONG: @State with class
@State var user = User()  // Wrong: State for reference types

// CORRECT: Use @StateObject or @ObservedObject
@StateObject var user = User()
// Or
@ObservedObject var user: User
```

### 4. Don't mutate in view body

```swift
// WRONG: Mutating in body
var body: some View {
    count += 1  // Error: mutation in computed property
    Text("\(count)")
}

// CORRECT: Use task modifier
var body: some View {
    Text("\(count)")
        .task {
            count = await fetchCount()
        }
}
```

## Related Errors

- [SwiftUI Error](swiftui-error) — general SwiftUI errors
- [Swift Concurrency Error](swift-concurrency-error-v2) — concurrency issues
- [SwiftUI List Error](swiftui-list-error) — list rendering
