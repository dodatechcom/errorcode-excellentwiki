---
title: "[Solution] UIKit UIView Property Animator Error"
description: "Fix UIViewPropertyAnimator configuration and interruption errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIView Property Animator Error

Property animator errors occur when the animator is interrupted and not properly resumed, when the timing parameters are incorrect, or when the animator state is inconsistent.

## Common Causes
- Animator interrupted and not resumed
- Timing curve incompatible with animation type
- Animator state not checked before starting
- Multiple animators on same property conflicting

## How to Fix
1. Handle animator interruption and resume properly
2. Use appropriate timing parameters
3. Check animator state before operations
4. Cancel conflicting animators before starting new ones

```swift
// Property animator:
let animator = UIViewPropertyAnimator(duration: 0.5, curve: .easeInOut) {
    self.view.transform = CGAffineTransform(rotationAngle: .pi / 2)
}
animator.startAnimation()

// Interrupt and resume:
animator.pauseAnimation()
animator.isReversed = true
animator.startAnimation()
```

## Examples
```swift
// Interactive animator:
let animator = UIViewPropertyAnimator(duration: 0.3, dampingRatio: 0.7) {
    self.button.transform = .identity
    self.button.alpha = 1
}

// Start when button pressed:
func buttonPressed() {
    animator.fractionComplete = 0
    animator.startAnimation()
}

// Scrub with gesture:
@objc func handlePan(_ gesture: UIPanGestureRecognizer) {
    let translation = gesture.translation(in: view)
    let fraction = translation.x / view.bounds.width
    animator.fractionComplete = fraction
}
```
