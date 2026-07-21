---
title: "[Solution] SwiftUI @ScaledMetric Dynamic Type Error"
description: "Fix SwiftUI @ScaledMetric dynamic type size adaptation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @ScaledMetric Dynamic Type Error

ScaledMetric Dynamic Type errors occur when the metric does not scale with Dynamic Type, when the metric type is incorrect, or when the metric does not update.

## Common Causes
- Metric does not scale
- Metric type incorrect
- Metric not updating
- Missing relativeTo parameter

## How to Fix
1. Scale metric with Dynamic Type
2. Use correct type
3. Ensure metric updates
4. Set relativeTo parameter

```swift
struct ContentView: View {
    @ScaledMetric(relativeTo: .body) private var iconSize: CGFloat = 20
    @ScaledMetric(relativeTo: .headline) private var fontSize: CGFloat = 16

    var body: some View {
        HStack {
            Image(systemName: "star.fill")
                .frame(width: iconSize, height: iconSize)
            Text("Hello")
                .font(.system(size: fontSize))
        }
    }
}
```

## Examples
```swift
// Relative to body
@ScaledMetric(relativeTo: .body) var size: CGFloat = 20

// Relative to headline
@ScaledMetric(relativeTo: .headline) var size: CGFloat = 16

// Relative to largeTitle
@ScaledMetric(relativeTo: .largeTitle) var size: CGFloat = 24

// Without relativeTo (scales with default)
@ScaledMetric var size: CGFloat = 20
```
