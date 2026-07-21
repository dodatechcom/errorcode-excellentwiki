---
title: "[Solution] UIKit UIViewControllerTransition Error"
description: "Fix UIViewController custom transition configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIViewControllerTransition Error

Custom transitions fail when the transitioning delegate is not set, when the transition coordinator is not properly configured, or when the transition context is incomplete.

## Common Causes
- Transitioning delegate not assigned
- Animation controller not returning proper duration
- Transition context not properly used
- Interactive transition not connected

## How to Fix
1. Set transitioningDelegate on the presented view controller
2. Return proper duration from animation controller
3. Use transition context for all animations
4. Connect interactive transition to gesture recognizer

```swift
// Custom transition setup:
class CustomTransition: NSObject, UIViewControllerAnimatedTransitioning {
    func transitionDuration(using transitionContext: UIViewControllerContextTransitioning?) -> TimeInterval { 0.3 }

    func animateTransition(using transitionContext: UIViewControllerContextTransitioning) {
        let toView = transitionContext.view(forKey: .to)!
        transitionContext.containerView.addSubview(toView)
        toView.alpha = 0
        UIView.animate(withDuration: 0.3, animations: { toView.alpha = 1 }) { _ in
            transitionContext.completeTransition(true)
        }
    }
}
```

## Examples
```swift
// Transition delegate:
class ViewController: UIViewController, UIViewControllerTransitioningDelegate {
    func animationController(forPresented presented: UIViewController, presenting: UIViewController, source: UIViewController) -> UIViewControllerAnimatedTransitioning? {
        return CustomTransition()
    }

    func animationController(forDismissed dismissed: UIViewController) -> UIViewControllerAnimatedTransitioning? {
        return CustomDismissTransition()
    }
}
```
