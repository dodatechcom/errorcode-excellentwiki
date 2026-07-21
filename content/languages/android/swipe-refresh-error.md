---
title: "Swipe Refresh Error"
description: "Fix SwipeRefreshLayout pull-to-refresh configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
SwipeRefreshLayout does not trigger refresh or conflicts with nested scrolling

## Common Causes

- SwipeRefreshLayout wrapping wrong view
- onRefreshListener not set
- NestedScrollView conflicts with SwipeRefresh
- Refresh indicator stuck showing after completion

## Fixes

- Wrap only the scrollable content view
- Set onRefreshListener callback
- Disable SwipeRefresh when nested scrolling child handles it
- Call setRefreshing(false) when refresh completes

## Code Example

```kotlin
<SwipeRefreshLayout
    android:id="@+id/swipeRefresh"
    app:layout_behavior="@string/appbar_scrolling_view_behavior">

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/recyclerView"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</SwipeRefreshLayout>

// In code:
swipeRefresh.setOnRefreshListener {
    viewModel.refresh()
    // When done:
    swipeRefresh.isRefreshing = false
}
```

# SwipeRefreshLayout should wrap single scrollable child
# Use app:layout_behavior with AppBarLayout
# Set isRefreshing = false when done
