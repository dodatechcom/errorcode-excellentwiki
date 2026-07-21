---
title: "[Solution] Deprecated Function Migration: manual Codable to synthesized conformance"
description: "Migrate from deprecated manual Codable to synthesized conformance."
deprecated_function: "Manual encode/decode"
replacement_function: "Automatic Codable synthesis"
languages: ["swift"]
deprecated_since: "Swift 4.0+"
---

# [Solution] Deprecated Function Migration: manual Codable to synthesized conformance

The `Manual encode/decode` has been deprecated in favor of `Automatic Codable synthesis`.

## Migration Guide

Synthesized conformance is simpler.

## Before (Deprecated)

```swift
struct User: Codable {
    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(name, forKey: .name)
    }
}
```

## After (Modern)

```swift
struct User: Codable {
    let name: String
    let age: Int
}
```

## Key Differences

- Automatic Codable synthesis
