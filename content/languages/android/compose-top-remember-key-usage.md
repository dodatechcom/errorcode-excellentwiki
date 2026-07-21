---
title: "Remember Key Error"
description: "Fix remember and rememberSaveable key usage in Compose for correct state preservation"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Composable state not preserved correctly because of incorrect remember key usage

## Common Causes

- State reset on recomposition
- rememberSaveable not restoring state
- Key change causing unnecessary state reset
- State shared between composables incorrectly

## Fixes

- Use correct key parameter for remember
- Use rememberSaveable for process death
- Ensure keys are stable and meaningful
- Test state preservation across config changes

## Code Example

```kotlin
// remember: survives recomposition, not config change
val data = remember { mutableStateOf("initial") }

// rememberSaveable: survives config change and process death
val scrollPosition = rememberSaveable { mutableStateOf(0) }

// Key-based remember:
val processedData = remember(inputData) { processData(inputData) }
```

# remember: recomposition only# rememberSaveable: config change + process death# Key-based: re-runs when key changes# Test preservation across scenarios
