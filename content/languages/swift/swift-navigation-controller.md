---
title: "[Solution] Swift UINavigationController Error — Push/Pop Stack"
description: "Fix Swift UINavigationController errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 128
---

UINavigationController errors occur when push/pop operations fail, view controller stack is mismanaged, or navigation bar configuration is incorrect.

## Common Causes

```swift
// Pushing when navigation controller is nil
let vc = DetailViewController()
navigationController?.pushViewController(vc, animated: true) // Silently fails

// Pop to non-existent view controller
navigationController?.popToViewController(rootVC, animated: true)
```

## How to Fix

**1. Safe push**

```swift
func pushViewController(_ viewController: UIViewController) {
    guard let nav = navigationController else {
        present(viewController, animated: true)
        return
    }
    nav.pushViewController(viewController, animated: true)
}
```

**2. Pop to specific controller**

```swift
if let targetVC = navigationController?.viewControllers.first(where: { $0 is SettingsVC }) {
    navigationController?.popToViewController(targetVC, animated: true)
}
```

**3. Set view controllers directly**

```swift
navigationController?.setViewControllers([rootVC, detailVC], animated: true)
```

**4. Configure navigation bar**

```swift
navigationItem.title = "Detail"
navigationController?.navigationBar.prefersLargeTitles = true
navigationItem.rightBarButtonItem = UIBarButtonItem(
    barButtonSystemItem: .action,
    target: self,
    action: #selector(shareTapped)
)
```

**5. Handle navigation delegate**

```swift
extension ViewController: UINavigationControllerDelegate {
    func navigationController(_ navigationController: UINavigationController, willShow viewController: UIViewController, animated: Bool) {
        // Prepare for transition
    }
    
    func navigationController(_ navigationController: UINavigationController, didShow viewController: UIViewController, animated: Bool) {
        // Transition complete
    }
}
```

## Examples

Programmatic navigation:
```swift
class Coordinator {
    let navigationController: UINavigationController
    
    init(navigationController: UINavigationController) {
        self.navigationController = navigationController
    }
    
    func showDetail(for item: Item) {
        let detailVC = DetailViewController(item: item)
        navigationController.pushViewController(detailVC, animated: true)
    }
    
    func goHome() {
        navigationController.popToRootViewController(animated: true)
    }
}
```

## Related Errors

- [ViewController Lifecycle](/languages/swift/swift-view-controller-lifecycle)
- [Auto Layout Error](/languages/swift/swift-autolayout-error)
- [UITableView Error](/languages/swift/swift-tableview-error)
