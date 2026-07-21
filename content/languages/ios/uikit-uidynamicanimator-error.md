---
title: "[Solution] UIKit UIDynamicAnimator Error"
description: "Fix UIDynamicAnimator physics simulation and behavior errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIDynamicAnimator Error

Dynamic animator errors occur when behaviors conflict, when items are removed during simulation, or when the animator reference frame becomes invalid.

## Common Causes
- Multiple behaviors on same item conflicting
- Item removed while behavior is active
- Reference frame does not contain all items
- Behavior parameters cause unrealistic physics

## How to Fix
1. Check for conflicting behaviors before adding
2. Remove behaviors before removing items
3. Set reference frame to cover all items
4. Tune behavior parameters for realistic motion

```swift
let animator = UIDynamicAnimator(referenceView: view)

let gravity = UIGravityBehavior(items: [item])
animator.addBehavior(gravity)

let collision = UICollisionBehavior(items: [item])
collision.translatesReferenceBoundsIntoBoundary = true
animator.addBehavior(collision)
```

## Examples
```swift
// Snap behavior:
let snap = UISnapBehavior(item: item, snapTo: CGPoint(x: 200, y: 300))
snap.damping = 0.5
animator.addBehavior(snap)

// Spring behavior:
let spring = UIAttachmentBehavior(item: item, attachedToAnchor: item.center)
spring.length = 0
spring.damping = 0.5
spring.frequency = 2.0
animator.addBehavior(spring)
```
