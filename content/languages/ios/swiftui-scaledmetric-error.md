---
title: "[Solution] SwiftUI @ScaledMetric Error"
description: "Fix SwiftUI @ScaledMetric dynamic font scaling errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @ScaledMetric Error

ScaledMetric errors occur when the metric is not properly configured, when the metric does not scale with Dynamic Type, or when the metric type is incorrect.

## Common Causes
- Metric not configured
- Metric not scaling with Dynamic Type
- Metric type incorrect
- Metric not updating

## How to Fix
1. Configure metric with base value
2. Use correct relative type
3. Ensure metric is in view scope
4. Update metric with content changes

```swift
struct ContentView: View {
    @ScaledMetric(relativeTo: .body) private var imageSize: CGFloat = 44

    var body: some View {
        Image(systemName: "star.fill")
            .font(.largeTitle)
            .frame(width: imageSize, height: imageSize)
    }
}
```

## Examples
```swift
// Multiple scaled metrics:
@ScaledMetric(relativeTo: .headline) private var iconSize: CGFloat = 20
@ScaledMetric(relativeTo: .body) private var spacing: CGFloat = 8
@ScaledMetric(relativeTo: .largeTitle) private var cornerRadius: CGFloat = 12
```
