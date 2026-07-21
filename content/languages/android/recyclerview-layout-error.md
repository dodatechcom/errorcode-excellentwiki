---
title: "RecyclerView Layout Error"
description: "Fix RecyclerView LayoutManager and layout configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
RecyclerView displays incorrectly because of LayoutManager configuration issues

## Common Causes

- LayoutManager not set on RecyclerView
- Wrong LayoutManager for desired scroll direction
- LinearLayoutManager span count incorrect
- GridLayoutManager not spanning full width

## Fixes

- Set LayoutManager before setting adapter
- Use LinearLayoutManager for single column lists
- Use GridLayoutManager with appropriate span count
- Use StaggeredGridLayoutManager for variable height items

## Code Example

```kotlin
// In Activity or Fragment:
recyclerView.layoutManager = LinearLayoutManager(context)

// Grid layout:
recyclerView.layoutManager = GridLayoutManager(context, 2)

// Staggered grid:
recyclerView.layoutManager = StaggeredGridLayoutManager(
    2, StaggeredGridLayoutManager.VERTICAL
)

// XML alternative:
<androidx.recyclerview.widget.RecyclerView
    app:layoutManager="androidx.recyclerview.widget.LinearLayoutManager"
    app:orientation="vertical"
    ... />
```

# LinearLayoutManager: lists
# GridLayoutManager: grid
# StaggeredGridLayoutManager: Pinterest-style
