---
title: "Strong Skipping Mode Error"
description: "Fix Compose Strong Skipping Mode and recomposition optimization errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Strong Skipping Mode not working correctly or causing stale data

## Common Causes

- Strong Skipping not enabled in compiler options
- Composable not qualifying for skip
- Stable parameters not actually stable
- Skipped recomposition showing stale UI

## Fixes

- Enable strong skipping mode in compiler
- Ensure parameters are truly stable
- Use @Stable annotation correctly
- Verify with recomposition counters

## Code Example

```kotlin
// Enable in build.gradle:
kotlinOptions {
    freeCompilerArgs += listOf("-P", "plugin:androidx.compose.compiler.plugins.kotlin:strongSkipping=true")
}

// Ensure stability:
@Stable
class MyState(
    val items: List<String>,  // List is stable if contents don't change
    val isLoading: Boolean
)

// In Composable:
@Composable
fun MyScreen(state: MyState) {
    // Will only recompose when state actually changes
}
```

# Strong Skipping: skip recomposition for stable params
# Requires truly stable parameter types
# @Stable/@Immutable annotations enable strong skipping
# Test with recomposition counters
