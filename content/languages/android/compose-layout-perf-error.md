---
title: "Compose Layout Performance Error"
description: "Fix Compose layout measurement performance and deep nesting issues"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose layout is slow because of deep nesting or expensive measurements

## Common Causes

- Column/Row nested more than 10 levels deep
- Layout measuring all children unnecessarily
- Large LazyColumn without fixed item heights
- Custom Layout not caching measurements

## Fixes

- Flatten layout hierarchy with ConstraintLayout
- Use BoxWithConstraints only when needed
- Set fixed heights for LazyColumn items
- Cache measurement results in custom Layout

## Code Example

```kotlin
// Use ConstraintLayout for flat hierarchy
ConstraintLayout {
    val (title, subtitle, image) = createRefs()
    Text("Title", modifier = Modifier.constrainAs(title) {
        top.linkTo(parent.top)
    })
}

// Avoid unnecessary recomposition in LazyColumn
LazyColumn {
    items(items, key = { it.id }) { item ->
        ListItem(item)  // Keep simple
    }
}

// Use key for stable item identity
```

# Deep nesting causes O(n²) measurement
# Use ConstraintLayout for complex flat layouts
# LazyColumn with keys for efficient diffing
