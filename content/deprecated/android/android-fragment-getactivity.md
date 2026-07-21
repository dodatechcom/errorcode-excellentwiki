---
title: "[Solution] Deprecated Function Migration: getActivity() to viewLifecycleOwner"
description: "Migrate from deprecated getActivity() to viewLifecycleOwner for lifecycle-aware operations."
deprecated_function: "getActivity()"
replacement_function: "viewLifecycleOwner"
languages: ["kotlin"]
deprecated_since: "AndroidX Fragment 1.2+"
---

# [Solution] Deprecated Function Migration: getActivity() to viewLifecycleOwner

The `getActivity()` has been deprecated in favor of `viewLifecycleOwner`.

## Migration Guide

getActivity() can return null after fragment is detached. Use viewLifecycleOwner for lifecycle-aware operations.

## Before (Deprecated)

```kotlin
class MyFragment : Fragment() {
    override fun onResume() {
        super.onResume()
        activity?.let {
            // Activity might be null
            it.title = "My Fragment"
        }
    }
}
```

## After (Modern)

```kotlin
class MyFragment : Fragment() {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // Lifecycle-aware observation
        viewLifecycleOwner.lifecycleScope.launch {
            viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
                // Safe to access UI
            }
        }
    }
}
```

## Key Differences

- viewLifecycleOwner is lifecycle-aware
- repeatOnLifecycle ensures safe collection
- No null checks needed
- Prevents memory leaks
