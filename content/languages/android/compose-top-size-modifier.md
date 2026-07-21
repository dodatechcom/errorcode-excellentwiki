---
title: "Size Modifier Error"
description: "Fix Compose size modifier for setting composable dimensions and constraints"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Composable not sizing correctly because of size modifier configuration

## Common Causes

- Size not matching expected dimensions
- Composable overflowing parent bounds
- Size modifier not respecting constraints
- Content not fitting within specified size

## Fixes

- Use size modifier for explicit sizing
- Use fillMaxSize/fillMaxWidth/fillMaxHeight for fill
- Use wrapContent for content-based sizing
- Test with different size configurations

## Code Example

```kotlin
Modifier
    .size(100.dp)  // Fixed size

// Fill available space:
Modifier.fillMaxWidth()
Modifier.fillMaxHeight()
Modifier.fillMaxSize()

// Content-based:
Modifier.wrapContentSize()
Modifier.width(IntrinsicSize.Max)
Modifier.height(IntrinsicSize.Min)
```

# size(): fixed dimensions# fillMax*: fill available space# wrapContent: content-based sizing# IntrinsicSize: content-based with bounds
