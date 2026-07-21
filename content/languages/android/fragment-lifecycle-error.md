---
title: "Fragment Lifecycle Error"
description: "Fix Android Fragment lifecycle callback errors and state management"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Fragment behaves unexpectedly because lifecycle callbacks are mismanaged

## Common Causes

- Heavy work in onCreate instead of onViewCreated
- Fragment transaction in onStart instead of onResume
- Missing super call in lifecycle methods
- Fragment not removed when detached from activity

## Fixes

- Do UI work in onViewCreated, data in onCreate
- Perform transactions in onResume or later
- Always call super lifecycle methods
- Use FragmentTransaction attach/detach properly

## Code Example

```kotlin
class MyFragment : Fragment() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Load data here (survives config changes)
        viewModel = ViewModelProvider(this)[MyViewModel::class.java]
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        // Setup UI here
        setupRecyclerView()
        observeViewModel()
    }

    override fun onResume() {
        super.onResume()
        // Refresh UI if needed
    }
}
```

# Fragment lifecycle:
# onAttach -> onCreate -> onCreateView -> onViewCreated
# -> onStart -> onResume -> onPause -> onStop
# -> onDestroyView -> onDestroy -> onDetach
