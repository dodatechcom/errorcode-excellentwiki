---
title: "[Solution] Core Animation Implicit Animation Error"
description: "Fix Core Animation implicit animation conflicts preventing expected transitions."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Core Animation Implicit Animation Error

Implicit animations conflict when multiple CALayer properties are modified simultaneously without proper animation disabling or when transaction groups interfere.

## Common Causes
- Multiple properties animated without disabling implicit animations
- CATransaction actions interfering with animations
- Animation delegate methods called out of order
- Layer hierarchy changes during animation

## How to Fix
1. Disable implicit animations with CATransaction.begin()
2. Use explicit animations for complex transitions
3. Set animation delegate before adding animation
4. Complete hierarchy changes before animating

```swift
// Disable implicit animations:
CATransaction.begin()
CATransaction.setDisableActions(true)
layer.opacity = 0
layer.cornerRadius = 20
CATransaction.commit()
```

## Examples
```swift
// Explicit animation with delegate:
let animation = CABasicAnimation(keyPath: "transform.scale")
animation.fromValue = 1.0
animation.toValue = 1.2
animation.duration = 0.3
animation.delegate = self
animation.isRemovedOnCompletion = false
animation.fillMode = .forwards
view.layer.add(animation, forKey: "scaleUp")
```
