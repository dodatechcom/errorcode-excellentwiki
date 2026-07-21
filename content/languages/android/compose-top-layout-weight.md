---
title: "Layout Weight Error"
description: "Fix Compose Row/Column weight modifier for proportional space distribution"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Row or Column items not correctly distributing available space using weight modifier

## Common Causes

- Weight items not filling available space
- Uneven distribution of space
- Weight not working with wrapContent parent
- Items overflowing when weighted

## Fixes

- Use Modifier.weight(fraction) for proportional space
- Ensure parent has fixed or fillMax size
- Use fillMaxWidth on Row/Column for weight to work
- Test with different weight distributions

## Code Example

```kotlin
Row(modifier = Modifier.fillMaxWidth()) {
    Box(modifier = Modifier.weight(1f)) { Text("25%") }
    Box(modifier = Modifier.weight(3f)) { Text("75%") }
}

Column(modifier = Modifier.fillMaxHeight()) {
    Box(modifier = Modifier.weight(2f)) { TopContent() }
    Box(modifier = Modifier.weight(1f)) { BottomContent() }
}
```

# weight(fraction): proportional space# Parent must have fixed/fillMax size# Multiple weights: fractions add up# Test with different distributions
