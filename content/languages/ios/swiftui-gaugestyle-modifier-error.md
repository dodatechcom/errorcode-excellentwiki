---
title: "[Solution] SwiftUI .gaugeStyle Modifier Error"
description: "Fix SwiftUI .gaugeStyle modifier gauge appearance style errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .gaugeStyle Modifier Error

GaugeStyle modifier errors occur when the style is not properly configured, when the style conflicts with the gauge, or when the style does not match the design.

## Common Causes
- Style not configured
- Style conflicts with gauge
- Style not matching design
- Style not updating

## How to Fix
1. Configure style properly
2. Ensure style is compatible with gauge
3. Match design specifications
4. Update style

```swift
struct ContentView: View {
    @State private var value = 0.5

    var body: some View {
        Gauge(value: value) {
            Text("Gauge")
        }
        .gaugeStyle(.accessoryCircular)
    }
}
```

## Examples
```swift
// Accessory circular
.gaugeStyle(.accessoryCircular)

// Accessory linear
.gaugeStyle(.accessoryLinear)

// Automatic
.gaugeStyle(.automatic)

// Custom
struct CustomGaugeStyle: GaugeStyle {
    func makeBody(configuration: Configuration) -> some View {
        ZStack {
            Circle()
                .stroke(.gray.opacity(0.2), lineWidth: 10)
            Circle()
                .trim(from: 0, to: configuration.fractionFilled)
                .stroke(.blue, style: StrokeStyle(lineWidth: 10, lineCap: .round))
                .rotationEffect(.degrees(-90))
        }
    }
}
```
