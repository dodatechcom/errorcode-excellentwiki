---
title: "[Solution] SwiftUI .digitalCrownAccessory Modifier Error"
description: "Fix SwiftUI .digitalCrownAccessory modifier Apple Watch Digital Crown errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .digitalCrownAccessory Modifier Error

DigitalCrownAccessory modifier errors occur when the accessory is not properly configured, when the accessory conflicts with the content, or when the accessory does not match the design.

## Common Causes
- Accessory not configured
- Accessory conflicts with content
- Accessory not matching design
- Accessory not updating with content

## How to Fix
1. Configure accessory properly
2. Ensure accessory is compatible with content
3. Match design specifications
4. Update accessory with content

```swift
struct ContentView: View {
    @State private var crownValue = 0.0

    var body: some View {
        Text("Value: \(crownValue)")
            .digitalCrownAccessory($crownValue, from: 0, through: 100, by: 1)
    }
}
```

## Examples
```swift
// Simple crown value
.digitalCrownAccessory($crownValue, from: 0, through: 100)

// With sensitivity
.digitalCrownAccessory($crownValue, from: 0, through: 100, by: 1, sensitivity: .low)

// With continuous
.digitalCrownAccessory($crownValue, from: 0, through: 100, isContinuous: true)
```
