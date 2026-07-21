---
title: "[Solution] SwiftUI .buttonStyle Modifier Error"
description: "Fix SwiftUI .buttonStyle modifier button appearance and interaction style errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .buttonStyle Modifier Error

ButtonStyle modifier errors occur when the style is not properly configured, when the style conflicts with the button, or when the style does not match the design.

## Common Causes
- Style not configured
- Style conflicts with button
- Style not matching design
- Style not updating

## How to Fix
1. Configure style properly
2. Ensure style is compatible with button
3. Match design specifications
4. Update style

```swift
struct ContentView: View {
    var body: some View {
        Button("Tap Me") { }
            .buttonStyle(.borderedProminent)
    }
}
```

## Examples
```swift
// Prominent
.buttonStyle(.borderedProminent)

// Bordered
.buttonStyle(.bordered)

// Borderless
.buttonStyle(.borderless)

// Plain
.buttonStyle(.plain)

// Custom
struct CustomButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .padding()
            .background(.blue)
            .foregroundColor(.white)
            .cornerRadius(10)
    }
}
```
