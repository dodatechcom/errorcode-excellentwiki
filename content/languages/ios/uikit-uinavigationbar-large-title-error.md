---
title: "[Solution] UIKit UINavigationBar Large Title Error"
description: "Fix UINavigationBar large title display and transition issues in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UINavigationBar Large Title Error

Large titles fail to display when the navigation bar appearance is misconfigured, when the view controller does not support large titles, or during transitions between controllers.

## Common Causes
- Navigation bar appearance set incorrectly
- View controller not set up for large titles
- Scroll view content offset conflicts
- Bar appearance differences between view controllers

## How to Fix
1. Set prefersLargeTitles on the navigation item
2. Configure navigation bar appearance properly
3. Ensure scroll view works with large title collapsing
4. Use navigation bar appearance APIs for iOS 13+

```swift
// Enable large titles:
navigationItem.largeTitleDisplayMode = .always
navigationController?.navigationBar.prefersLargeTitles = true

// Configure appearance:
let appearance = UINavigationBarAppearance()
appearance.configureWithDefaultBackground()
navigationController?.navigationBar.standardAppearance = appearance
```

## Examples
```swift
// Large title configuration:
class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        title = "Home"
        navigationItem.largeTitleDisplayMode = .always
        navigationController?.navigationBar.prefersLargeTitles = true

        let appearance = UINavigationBarAppearance()
        appearance.configureWithOpaqueBackground()
        appearance.backgroundColor = .systemBackground
        navigationController?.navigationBar.standardAppearance = appearance
        navigationController?.navigationBar.scrollEdgeAppearance = appearance
    }
}
```
