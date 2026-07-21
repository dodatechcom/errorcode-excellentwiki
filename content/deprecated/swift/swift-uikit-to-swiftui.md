---
title: "[Solution] Deprecated Function Migration: UIKit to SwiftUI"
description: "Migrate from deprecated UIKit patterns to SwiftUI."
deprecated_function: "UIKit (UIViewController)"
replacement_function: "SwiftUI (View)"
languages: ["swift"]
deprecated_since: "iOS 13+"
---

# [Solution] Deprecated Function Migration: UIKit to SwiftUI

The `UIKit (UIViewController)` has been deprecated in favor of `SwiftUI (View)`.

## Migration Guide

SwiftUI is Apple's modern declarative UI

UIKit is imperative. SwiftUI uses declarative syntax.

## Before (Deprecated)

```swift
class MyVC: UIViewController {
    let label = UILabel()
    override func viewDidLoad() {
        super.viewDidLoad()
        label.text = "Hello"
        view.addSubview(label)
    }
}
```

## After (Modern)

```swift
struct MyView: View {
    var body: some View {
        VStack {
            Text("Hello").font(.title)
            Button("Tap me") { }
        }
    }
}
```

## Key Differences

- SwiftUI uses declarative syntax
- No storyboards needed
- Automatic UI updates with state
