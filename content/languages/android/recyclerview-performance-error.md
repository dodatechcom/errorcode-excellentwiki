---
title: "RecyclerView Performance Error"
description: "Fix RecyclerView performance issues and jank during scrolling"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
RecyclerView stutters or janks during fast scrolling

## Common Causes

- ViewHolder doing heavy work in onBindViewHolder
- ImageView not downscaled to view size
- Layout measurements not cached
- notifyDataSetChanged used instead of DiffUtil

## Fixes

- Keep onBindViewHolder lightweight
- Load images at view size with Glide
- Use setHasFixedSize(true) for constant-size items
- Use DiffUtil for efficient updates

## Code Example

```kotlin
// Optimize RecyclerView
recyclerView.apply {
    setHasFixedSize(true)
    itemAnimator = DefaultItemAnimator()
}

// In ViewHolder:
override fun onBindViewHolder(holder: ViewHolder, position: Int) {
    // Light binding only - no I/O, no heavy computation
    holder.bind(getItem(position))
}

// Use DiffUtil, not notifyDataSetChanged:
adapter.submitList(newList)

// Set view cache:
recyclerView.setItemViewCacheSize(20)
```

# setHasFixedSize(true) for constant item size
# Use DiffUtil/ListAdapter for efficient updates
# Avoid notifyItemChanged() on large ranges
# Profile with GPU rendering and systrace
