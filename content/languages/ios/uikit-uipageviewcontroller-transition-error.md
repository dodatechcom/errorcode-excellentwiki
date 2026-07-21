---
title: "[Solution] UIKit UIPageViewController Transition Error"
description: "Fix UIPageViewController page transition and navigation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIPageViewController Transition Error

Page transitions fail when the data source returns incorrect view controllers, when the transition style does not match the content, or when page navigation direction is misconfigured.

## Common Causes
- Data source methods return wrong view controllers
- Transition style not matching content type
- Navigation direction not configured
- View controller reference lost between transitions

## How to Fix
1. Implement data source methods correctly
2. Match transition style to content (scroll vs page curl)
3. Configure navigation direction
4. Maintain strong references to child view controllers

```swift
// Page view controller setup:
let pageVC = UIPageViewController(transitionStyle: .scroll, navigationOrientation: .horizontal, options: [UIPageViewControllerOptionInterPageSpacingKey: 20])
pageVC.dataSource = self
pageVC.setViewControllers([pages[0]], direction: .forward, animated: false)
```

## Examples
```swift
// Data source implementation:
func pageViewController(_ pageViewController: UIPageViewController, viewControllerBefore viewController: UIViewController) -> UIViewController? {
    guard let index = pages.firstIndex(of: viewController), index > 0 else { return nil }
    return pages[index - 1]
}

func pageViewController(_ pageViewController: UIPageViewController, viewControllerAfter viewController: UIViewController) -> UIViewController? {
    guard let index = pages.firstIndex(of: viewController), index < pages.count - 1 else { return nil }
    return pages[index + 1]
}
```
