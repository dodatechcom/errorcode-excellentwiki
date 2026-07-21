---
title: "DataBinding Lifecycle Error"
description: "Fix DataBinding lifecycle owner and LiveData observation errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
DataBinding does not update UI when LiveData values change

## Common Causes

- lifecycleOwner not set on binding
- LiveData not used as binding data type
- Binding not executing pending changes
- Fragment view lifecycle owner not correct

## Fixes

- Set binding.lifecycleOwner = this in Activity
- Use viewLifecycleOwner in Fragment
- Call executePendingBindings() for immediate update
- Use LiveData or StateFlow as variable type

## Code Example

```kotlin
// In Activity:
binding.lifecycleOwner = this

// In Fragment:
binding.lifecycleOwner = viewLifecycleOwner

// Force immediate update:
binding.executePendingBindings()

// In layout, LiveData auto-updates with lifecycle:
<TextView
    android:text="@{viewModel.name}" />
```

# lifecycleOwner required for LiveData observation
# Use viewLifecycleOwner in Fragments
# DataBinding will automatically unsubscribe
