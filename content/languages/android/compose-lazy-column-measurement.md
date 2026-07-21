---
title: "LazyColumn Measurement Error"
description: "Fix LazyColumn item measurement and sizing issues with dynamic content"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn items not measuring correctly causing layout shifts or incorrect sizes

## Common Causes

- Item height varying based on content causing jumping
- Text wrapping changing item size
- Image aspect ratio affecting item measurement
- Nested composables causing measurement issues

## Fixes

- Use fixed height items when possible
- Use ConstraintLayout for complex item sizing
- Use aspect ratio modifier for images
- Pre-compute item heights for stable layout

## Code Example

```kotlin
LazyColumn {
    items(items, key = { it.id }) { item ->
        Box(modifier = Modifier.fillMaxWidth().heightIn(min = 64.dp)) {
            ItemContent(item)
        }
    }
}
```

# Fixed heights prevent jumping# heightIn for minimum height# aspectRatio for image sizing# Pre-compute heights when possible
