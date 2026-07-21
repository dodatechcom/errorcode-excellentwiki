---
title: "Modifier Extension Error"
description: "Fix Compose custom Modifier extension function errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Custom Modifier extensions do not compose correctly or produce wrong layout

## Common Causes

- Modifier.then() not properly chaining
- Modifier factory not creating new instance
- Modifier not respecting parent constraints
- Custom modifier causing infinite measurement

## Fixes

- Use Modifier.Node for custom modifiers
- Chain modifiers with Modifier.then()
- Respect parent constraints in layout
- Test modifier on multiple screen sizes

## Code Example

```kotlin
// Custom Modifier extension
fun Modifier.shimmer(): Modifier = this.then(
    composed {
        val transition = rememberInfiniteTransition()
        val alpha by transition.animateFloat(
            initialValue = 0.2f,
            targetValue = 0.9f,
            animationSpec = infiniteRepeatable(
                animation = tween(1000),
                repeatMode = RepeatMode.Reverse
            )
        )
        background(Color.LightGray.copy(alpha = alpha))
    }
)

// Usage:
Box(
    modifier = Modifier
        .fillMaxWidth()
        .height(200.dp)
        .shimmer()
)
```

# composed: create stateful Modifier
# then(): chain Modifiers
# Modifier.Node: modern modifier API
# Test on multiple configurations
