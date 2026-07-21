---
title: "Layout Inspector Error"
description: "Fix Compose Layout Inspector debugging and recomposition tracking errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose Layout Inspector does not show recomposition counts or semantics

## Common Causes

- Layout Inspector not connecting to device
- Recomposition count not displaying
- Semantics tree not showing in inspector
- Compose version incompatible with inspector

## Fixes

- Update Android Studio to latest stable
- Use compatible Compose BOM version
- Enable developer options on device
- Check Compose version matches inspector

## Code Example

```kotlin
// Debug recomposition in code:
SideEffect {
    Log.d("Recomposition", "Composable recomposed")
}

// Or use derivedStateOf to reduce recompositions
// Profile with:
// 1. Layout Inspector in Android Studio
// 2. compose-metrics report
// 3. Recomposition counters in developer options
```

# Layout Inspector: visual debugging tool
# recompositionCounts: see how often composables recompose
# recompositionHighlighter: highlight recomposing composables
# Use Compose Compiler metrics for optimization
