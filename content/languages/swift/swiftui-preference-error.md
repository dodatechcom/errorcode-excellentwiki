---
title: "[Solution] SwiftUI Preference Error — Key, Reduce & Anchor"
description: "Fix SwiftUI preference key errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 109
---

SwiftUI preference errors occur when `PreferenceKey` implementations have incorrect `reduce` methods, anchor preferences are misused, or GeometryReader is incorrectly positioned.

## Common Causes

```swift
// Incorrect PreferenceKey reduce
struct SizePreferenceKey: PreferenceKey {
    static var defaultValue: CGSize = .zero
    static func reduce(value: inout CGSize, nextValue: () -> CGSize?) {
        value = nextValue() ?? value // Incorrect logic
    }
}

// Missing GeometryReader wrapper for anchor preferences
Button("Tap") { }
    .anchorPreference(\.buttonFrame, bounds: .global)
```

## How to Fix

**1. Correct PreferenceKey reduce implementation**

```swift
struct SizePreferenceKey: PreferenceKey {
    static var defaultValue: CGSize = .zero
    
    static func reduce(value: inout CGSize, nextValue: () -> CGSize?) {
        value = nextValue() ?? value
    }
}
```

**2. Use Anchor preferences with GeometryReader**

```swift
struct ContentView: View {
    @State private var buttonFrame: Anchor<CGRect>?
    
    var body: some View {
        VStack {
            Button("Tap") { }
                .anchorPreference(\.buttonFrame, bounds: .global)
            
            GeometryReader { proxy in
                Color.clear
                    .overlayPreferenceValue(\.buttonFrame) { anchor in
                        if let anchor {
                            let rect = proxy[anchor]
                            Text("Button at: \(rect.origin.x)")
                        }
                    }
            }
        }
    }
}
```

**3. Propagate preferences through views**

```swift
struct ChildView: View {
    var body: some View {
        Text("Hello")
            .background(
                GeometryReader { proxy in
                    Color.clear.preference(
                        key: SizePreferenceKey.self,
                        value: proxy.size
                    )
                }
            )
    }
}
```

**4. Handle multiple preference values**

```swift
struct AllSizesKey: PreferenceKey {
    static var defaultValue: [CGSize] = []
    
    static func reduce(value: inout [CGSize], nextValue: () -> [CGSize]?) {
        value.append(contentsOf: nextValue() ?? [])
    }
}
```

**5. Use overlayPreferenceValue**

```swift
var body: some View {
    ScrollView {
        content
    }
    .overlayPreferenceValue(\.buttonFrame) { anchor in
        // Read preference in overlay
    }
}
```

## Examples

Complete preference key usage:
```swift
struct TitleKey: PreferenceKey {
    static var defaultValue: String = ""
    static func reduce(value: inout String, nextValue: () -> String?) {
        value = nextValue() ?? value
    }
}

struct ParentView: View {
    @State private var title = ""
    
    var body: some View {
        VStack {
            ChildView()
            Text(title)
        }
        .onPreferenceChange(TitleKey.self) { newTitle in
            title = newTitle
        }
    }
}
```

## Related Errors

- [Environment Error](/languages/swift/swiftui-environment-error)
- [Binding Error](/languages/swift/swiftui-binding-error)
- [Gesture Error](/languages/swift/swiftui-gesture-error)
