---
title: "Partial Consumption Error"
description: "Fix Compose partial consumable gesture issues with nested touch targets"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Touch events partially consumed causing incorrect gesture handling in nested composables

## Common Causes

- Gesture consumed by child leaving parent without events
- Nested scrollable areas not cooperating
- Touch down consumed but not touch up
- Drag gesture starting but not completing

## Fixes

- Use pointerInput for proper gesture handling
- Use consume() to mark events as handled
- Coordinate nested gestures with nestedScroll
- Test gesture propagation through composables

## Code Example

```kotlin
Modifier.pointerInput(Unit) {
    detectDragGestures(
        onDragStart = { /* Start */ },
        onDrag = { change, offset ->
            change.consume()
            onDrag(offset)
        }
    )
}
```

# consume() marks event as handled# Nested gestures use nestedScroll# Test gesture propagation# Verify all gesture phases
