---
title: "[Solution] Core Animation CATransaction Completion Error"
description: "Fix CATransaction completion block timing and execution errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Core Animation CATransaction Completion Error

Completion blocks may not fire when transactions are nested incorrectly, when the commit is disabled, or when the transaction contains only non-animating changes.

## Common Causes
- Nested transactions with shared completion blocks
- Transaction disabled actions but completion still expected
- Completion called before animation starts
- Transaction committed before completion registered

## How to Fix
1. Use separate completion blocks for each transaction
2. Ensure transaction is committed for completion to fire
3. Register completion before committing
4. Do not disable actions when expecting completion

```swift
// Transaction with completion:
CATransaction.begin()
CATransaction.setCompletionBlock {
    print("Animation completed")
}
UIView.animate(withDuration: 0.3) {
    self.view.alpha = 0
}
CATransaction.commit()
```

## Examples
```swift
// Sequential animations with completions:
func animateIn() {
    CATransaction.begin()
    CATransaction.setCompletionBlock {
        self.animateOut()
    }
    UIView.animate(withDuration: 0.3) {
        self.view.transform = .identity
        self.view.alpha = 1
    }
    CATransaction.commit()
}

func animateOut() {
    UIView.animate(withDuration: 0.3) {
        self.view.transform = CGAffineTransform(scaleX: 0.1, y: 0.1)
        self.view.alpha = 0
    }
}
```
