---
title: "Modifier Order Error"
description: "Fix modifier chain order in Compose affecting layout and drawing"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Composable layout or drawing incorrect because modifier order matters

## Common Causes

- Background appearing inside padding instead of outside
- Clickable area wrong size
- Border not aligned with padding
- DrawBehind not covering correct area

## Fixes

- Modifiers applied left to right / top to bottom
- padding before background means background inside padded area
- background before padding means background fills original area
- Test modifier order changes for correct rendering

## Code Example

```kotlin
// WRONG: background inside padding
Modifier.padding(16.dp).background(Color.Red)

// CORRECT: background fills area then padding applied
Modifier.background(Color.Red).padding(16.dp)
```

# Modifiers applied sequentially left-to-right# padding().background() = bg inside padding# background().padding() = bg outside padding# Test each modifier order change
