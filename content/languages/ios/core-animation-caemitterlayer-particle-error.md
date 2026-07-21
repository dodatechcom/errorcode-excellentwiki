---
title: "[Solution] Core Animation CAEmitterLayer Particle Error"
description: "Fix CAEmitterLayer particle emitter configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Core Animation CAEmitterLayer Particle Error

Emitter layer errors occur when emission rates are negative, when particle properties are incompatible, or when the emitter shape does not contain emission regions.

## Common Causes
- Negative birth or death rate values
- Emitter cell shape exceeds layer bounds
- Particle properties conflicting with each other
- Emitter layer not added to view hierarchy

## How to Fix
1. Ensure all emission rates are non-negative
2. Set emitter size within layer bounds
3. Verify particle property compatibility
4. Add emitter layer to a visible view

```swift
// Configure emitter layer:
let emitterLayer = CAEmitterLayer()
emitterLayer.emitterPosition = CGPoint(x: view.bounds.midX, y: view.bounds.midY)
emitterLayer.emitterSize = CGSize(width: 100, height: 100)
emitterLayer.emitterShape = .circle

let cell = CAEmitterCell()
cell.contents = UIImage(named: "particle")?.cgImage
cell.birthRate = 5
cell.lifetime = 3
cell.velocity = 50
emitterLayer.emitterCells = [cell]
view.layer.addSublayer(emitterLayer)
```

## Examples
```swift
// Firework emitter:
let emitter = CAEmitterLayer()
emitter.emitterPosition = CGPoint(x: view.bounds.midX, y: view.bounds.height)
emitter.emitterSize = CGSize(width: 1, height: 1)
emitter.emitterShape = .point

let particle = CAEmitterCell()
particle.contents = UIImage(named: "spark")?.cgImage
particle.birthRate = 200
particle.lifetime = 1.5
particle.lifetimeRange = 0.5
particle.velocity = 150
particle.velocityRange = 50
particle.emissionLongitude = -.pi
particle.emissionRange = .pi / 4
particle.spin = 2
particle.spinRange = 4
particle.scale = 0.15
particle.scaleRange = 0.05
particle.alphaSpeed = -0.5
emitter.emitterCells = [particle]
view.layer.addSublayer(emitter)
```
