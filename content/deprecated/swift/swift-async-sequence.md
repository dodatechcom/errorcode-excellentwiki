---
title: "[Solution] Deprecated Function Migration: AsyncSequence to for await"
description: "Migrate from deprecated AsyncSequence manual iteration to for await."
deprecated_function: "for try await value in sequence { }"
replacement_function: "for await value in sequence { }"
languages: ["swift"]
deprecated_since: "Swift 5.5+"
---

# [Solution] Deprecated Function Migration: AsyncSequence to for await

The `for try await value in sequence { }` has been deprecated in favor of `for await value in sequence { }`.

## Migration Guide

for await is simpler.

## Before (Deprecated)

```swift
for try await value in sequence {
    process(value)
}
```

## After (Modern)

```swift
for await value in sequence {
    process(value)
}
```

## Key Differences

- for await is simpler
