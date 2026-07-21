---
title: "LazyColumn Mixed Types Error"
description: "Fix LazyColumn with multiple item types and heterogeneous content"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn with mixed item types not displaying correctly or layout broken

## Common Causes

- Different item types not rendered correctly
- Type-specific layouts conflicting
- ViewType pattern not working with Compose
- Mixed items causing layout inconsistencies

## Fixes

- Use different composable for each type
- Switch on item type in items block
- Ensure consistent spacing between types
- Test with varied item type distributions

## Code Example

```kotlin
LazyColumn {
    items(items, key = { it.id }) { item ->
        when (item) {
            is HeaderItem -> HeaderRow(item)
            is ContentItem -> ContentRow(item)
            is AdItem -> AdBanner(item)
            is FooterItem -> FooterRow(item)
        }
    }
}
```

# when expression for type dispatch# Different composable per type# Consistent spacing across types# key for stable identity
