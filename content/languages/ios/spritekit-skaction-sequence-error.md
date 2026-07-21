---
title: "[Solution] SpriteKit SKAction Sequence Error"
description: "Fix SpriteKit SKAction sequence completion and timing issues."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SpriteKit SKAction Sequence Error

SKAction sequences fail when actions reference nodes that have been removed, when timing is incorrect, or when group actions conflict with sequence timing.

## Common Causes
- Node removed before sequence completes
- Action references stale node reference
- Duration of group action does not match sequence
- completion block called on deallocated node

## How to Fix
1. Check node is in scene before running actions
2. Use weak references in completion blocks
3. Calculate group durations correctly
4. Remove specific actions by key when needed

```swift
// Safe action sequence:
let sequence = SKAction.sequence([
    SKAction.moveBy(x: 100, y: 0, duration: 0.5),
    SKAction.fadeOut(withDuration: 0.3),
    SKAction.removeFromParent()
])
node.run(sequence, withKey: "moveAndFade")
```

## Examples
```swift
// Complex action sequence:
let moveRight = SKAction.moveBy(x: 100, y: 0, duration: 0.5)
let moveLeft = SKAction.moveBy(x: -100, y: 0, duration: 0.5)
let pause = SKAction.wait(forDuration: 0.2)
let group = SKAction.group([
    SKAction.sequence([moveRight, pause, moveLeft]),
    SKAction.repeatForever(SKAction.sequence([
        SKAction.colorize(with: .red, colorBlendFactor: 1, duration: 0.25),
        SKAction.colorize(withColorBlendFactor: 0, duration: 0.25)
    ]))
])
node.run(group)
```
