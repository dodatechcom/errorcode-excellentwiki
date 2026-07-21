---
title: "Scrollable Modifier Error"
description: "Fix Compose scrollable modifier for adding scroll behavior to composables"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Scroll behavior not working correctly or scroll state not preserved

## Common Causes

- Scroll not working on composable
- Scroll state not preserved across recomposition
- Scroll not matching expected direction
- Scroll interfering with parent scrollable

## Fixes

- Use verticalScroll or horizontalScroll for scrolling
- Use rememberScrollState for scroll state
- Use nestedScroll for coordinated scrolling
- Test scroll with different content sizes

## Code Example

```kotlin
Modifier.verticalScroll(rememberScrollState())
Modifier.horizontalScroll(rememberScrollState())

// With nested scroll:
val nestedScrollConnection = rememberNestedScrollConnection()
Modifier
    .nestedScroll(nestedScrollConnection)
    .verticalScroll(rememberScrollState())
```

# verticalScroll/horizontalScroll: scrolling# rememberScrollState: scroll state# nestedScroll: coordinated scrolling# Test scroll behavior
