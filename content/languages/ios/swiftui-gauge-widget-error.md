---
title: "[Solution] SwiftUI Gauge Widget Error"
description: "Fix SwiftUI Gauge and progress indicator configuration errors in watchOS and iOS widgets."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI Gauge Widget Error

Gauge errors occur when values exceed the specified range, when the label is not properly configured, or when the gauge style conflicts with the container size.

## Common Causes
- Value outside min/max range
- Label not provided for accessibility
- Gauge style incompatible with widget size
- Multiple gauges conflicting in layout

## How to Fix
1. Clamp values within the specified range
2. Always provide a label for VoiceOver
3. Choose appropriate gauge style for available space
4. Use proper spacing in gauge containers

```swift
// Basic gauge:
Gauge(value: currentProgress) {
    Text("Progress")
} currentValueLabel: {
    Text("\(Int(currentProgress * 100))%")
}
.gaugeStyle(.accessoryCircular)
```

## Examples
```swift
// Gauge with range:
Gauge(value: temperature, in: 0...100) {
    Text("Temperature")
} currentValueLabel: {
    Text("\(Int(temperature))°")
} markedValueMarks: {
    GaugeMark(value: 50)
    GaugeMark(value: 75)
}
.gaugeStyle(.linear)
.frame(width: 200)
```
