---
title: "[Solution] SpriteKit Physics Body Collision Error"
description: "Fix SpriteKit physics body collision detection errors in game scenes."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SpriteKit Physics Body Collision Error

Physics body collisions fail to detect when collision bit masks are not configured correctly or when physics bodies are not properly added to the scene.

## Common Causes
- Category and collision bit masks not set
- Physics body not attached to the node
- Contact delegate not set on SKScene
- isDynamic set to false on the wrong body

## How to Fix
1. Configure categoryBitMask, collisionBitMask, and contactTestBitMask
2. Ensure physicsBody property is set on nodes
3. Set the scene as physics contact delegate
4. Set isDynamic correctly based on use case

```swift
// Configure physics categories:
struct PhysicsCategory {
    static let player: UInt32 = 0x1 << 0
    static let enemy: UInt32 = 0x1 << 1
}

playerNode.physicsBody?.categoryBitMask = PhysicsCategory.player
enemyNode.physicsBody?.categoryBitMask = PhysicsCategory.enemy
enemyNode.physicsBody?.contactTestBitMask = PhysicsCategory.player
```

## Examples
```swift
// Contact detection:
class GameScene: SKScene, SKPhysicsContactDelegate {
    override func didMove(to view: SKView) {
        physicsWorld.contactDelegate = self
    }

    func didBegin(_ contact: SKPhysicsContact) {
        let bodyA = contact.bodyA
        let bodyB = contact.bodyB
        if bodyA.categoryBitMask == PhysicsCategory.player {
            handlePlayerCollision(with: bodyB.node)
        }
    }
}
```
