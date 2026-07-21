---
title: "[Solution] SwiftUI Charts Data Error"
description: "Fix SwiftUI Charts framework data configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI Charts Data Error

Charts fail to render when data types do not match chart mark requirements, when data is empty, or when chart marks conflict with the provided data.

## Common Causes
- Data type does not conform to required protocols
- Chart mark parameters mismatch data types
- Empty data array causes rendering failure
- Multiple chart marks with incompatible data

## How to Fix
1. Ensure data conforms to Identifiable and Plottable
2. Match chart mark parameters to data properties
3. Provide fallback view for empty data
4. Use correct mark types for your data

```swift
import Charts

struct DataPoint: Identifiable, Plottable {
    let id = UUID()
    let category: String
    let value: Double
}

Chart(dataPoints, id: \.id) { point in
    BarMark(x: .value("Category", point.category), y: .value("Value", point.value))
}
```

## Examples
```swift
// Line chart with multiple series:
Chart {
    ForEach(series1) { point in
        LineMark(x: .value("Date", point.date), y: .value("Value", point.value))
            .foregroundStyle(.blue)
    }
    ForEach(series2) { point in
        LineMark(x: .value("Date", point.date), y: .value("Value", point.value))
            .foregroundStyle(.red)
    }
}
.chartYAxis {
    AxisMarks(position: .leading)
}
```
