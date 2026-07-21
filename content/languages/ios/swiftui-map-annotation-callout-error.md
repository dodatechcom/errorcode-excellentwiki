---
title: "[Solution] SwiftUI Map Annotation Callout Error"
description: "Fix SwiftUI Map annotation callout display and interaction errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI Map Annotation Callout Error

Map annotation callouts fail to display when the annotation does not support callouts, when the callout content is not properly configured, or when the callout size exceeds available space.

## Common Causes
- Annotation does not support callouts
- Callout content not configured
- Callout view too large for display area
- Callout interaction handlers not implemented

## How to Fix
1. Ensure annotation supports callout display
2. Configure callout content and accessories
3. Set appropriate callout size
4. Implement callout delegate methods

```swift
// Map annotation with callout:
Annotation("Location", coordinate: coordinate) {
    VStack {
        Image(systemName: "mappin.circle.fill")
            .foregroundColor(.red)
    }
}
.mapAnnotationCalloutAttachment { attachment in
    Text("Details")
}
```

## Examples
```swift
// Custom annotation with callout:
struct CustomAnnotation: View {
    let coordinate: CLLocationCoordinate2D
    let title: String

    var body: some View {
        VStack {
            Circle()
                .fill(.blue)
                .frame(width: 30, height: 30)
                .shadow(radius: 3)
        }
        .mapAnnotationCalloutAttachment { attachment in
            VStack(alignment: .leading) {
                Text(title).font(.headline)
                Button("Navigate") { }
            }
            .padding()
        }
    }
}
```
