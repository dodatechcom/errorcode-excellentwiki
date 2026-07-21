---
title: "[Solution] MapKit Annotation View Reuse Error"
description: "Fix MapKit MKAnnotationView reuse issues causing blank or incorrect annotations."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# MapKit Annotation View Reuse Error

Annotation views fail to display correctly when reuse identifiers do not match or when annotation data is not properly configured in viewFor delegate.

## Common Causes
- Reuse identifier mismatch between dequeueReusableAnnotationView and registerAnnotationView
- Annotation view not configured with correct image or callout
- Delegate method not returning the annotation view
- Annotation view reused without updating content

## How to Fix
1. Match reuse identifiers exactly
2. Always update annotation view content when reusing
3. Return the annotation view from the delegate
4. Register annotation views in viewDidLoad

```swift
func mapView(_ mapView: MKMapView, viewFor annotation: MKAnnotation) -> MKAnnotationView? {
    guard let annotation = annotation as? MyAnnotation else { return nil }
    let identifier = "MyAnnotation"
    let view = mapView.dequeueReusableAnnotationView(withIdentifier: identifier, for: annotation)
    view.image = UIImage(named: "pin")
    return view
}
```

## Examples
```swift
// Register and dequeue annotation views:
override func viewDidLoad() {
    super.viewDidLoad()
    mapView.register(MKMarkerAnnotationView.self, forAnnotationWithReuseIdentifier: "marker")
}

func mapView(_ mapView: MKMapView, viewFor annotation: MKAnnotation) -> MKAnnotationView? {
    let view = mapView.dequeueReusableAnnotationView(withIdentifier: "marker", for: annotation) as! MKMarkerAnnotationView
    view.markerTintColor = .blue
    view.canShowCallout = true
    return view
}
```
