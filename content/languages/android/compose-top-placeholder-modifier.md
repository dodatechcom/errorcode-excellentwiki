---
title: "Placeholder Error"
description: "Fix Compose placeholder modifier for content placeholder and loading states"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Placeholder not appearing correctly during loading or content not transitioning

## Common Causes

- Placeholder not visible during loading
- Placeholder size not matching content
- Placeholder not hiding after content loads
- Placeholder animation not working

## Fixes

- Use placeholder modifier for loading states
- Use shimmer effect for placeholder
- Control placeholder visibility with state
- Animate placeholder appearance

## Code Example

```kotlin
var isLoading by remember { mutableStateOf(true) }

Box(modifier = Modifier.placeholder(visible = isLoading)) {
    if (!isLoading) {
        Content()
    }
}

// Shimmer effect:
Box(
    modifier = Modifier
        .fillMaxWidth()
        .height(200.dp)
        .shimmer(
            shimmer = shimmerProvider.shimmer,
            enabled = isLoading
        )
)
```

# placeholder: loading state# visible: control placeholder visibility# shimmer: animated placeholder# Transition from placeholder to content
