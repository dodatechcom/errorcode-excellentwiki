---
title: "Multi-Touch Consumption Error"
description: "Fix Compose partial gesture consumption with multi-touch pointer events"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Multi-touch gestures not handled correctly because of partial pointer consumption

## Common Causes

- Second pointer not tracked correctly
- Pinch gesture not detected with partial consumption
- Pointer events lost between composables
- Multi-touch causing incorrect drag behavior

## Fixes

- Track each pointer separately with awaitPointerEvent
- Do not consume events meant for other pointers
- Use PointerEventType.Press/Move/Release correctly
- Test with multi-touch on physical device

## Code Example

```kotlin
Modifier.pointerInput(Unit) {
    awaitPointerEventScope {
        while (true) {
            val event = awaitPointerEvent()
            event.changes.forEach { change ->
                if (change.pressed) {
                    change.consume()
                }
            }
        }
    }
}
```

# Track each pointer separately# Do not consume for other composables# Test multi-touch on physical device# Use awaitPointerEvent for custom handling
