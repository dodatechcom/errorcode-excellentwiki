---
title: "Nested Scroll Error"
description: "Fix LazyColumn nested scroll behavior with parent scrollable containers"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn does not scroll properly inside parent scrollable containers like Scaffold or ScrollView

## Common Causes

- LazyColumn not receiving scroll events
- Parent container intercepting LazyColumn scroll
- Nested scroll not working with Scaffold
- Scroll conflict between header and list

## Fixes

- Use nestedScroll modifier to coordinate scroll
- Ensure LazyColumn is the only scrollable in chain
- Use CoordinatorLayout pattern with Compose
- Test with Scaffold top bar collapse

## Code Example

```kotlin
LazyColumn(modifier = Modifier.nestedScroll(nestedScrollConnection)) { items(items) { ItemRow(it) } }
```

# nestedScroll: coordinate multiple scroll targets# Only one primary scrollable in vertical chain# Use Scaffold topBar with LazyColumn for collapse effects# Test with multiple nested scrollables
