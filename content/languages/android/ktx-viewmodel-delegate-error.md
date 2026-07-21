---
title: "KTX ViewModel Delegate Error"
description: "Fix Kotlin KTX ViewModel delegate and activityViewModels errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
ViewModel delegate fails to provide correct ViewModel instance

## Common Causes

- viewModels() delegate not finding ViewModel factory
- activityViewModels() returning wrong scope ViewModel
- HiltViewModel not compatible with delegate
- ViewModel not sharing between fragments

## Fixes

- Ensure ViewModel has default or injected constructor
- Use activityViewModels() for shared ViewModel
- Use @HiltViewModel with @Inject for Hilt
- Verify fragment is properly attached to activity

## Code Example

```kotlin
// ViewModel scoped to Fragment
val viewModel: MyViewModel by viewModels()

// ViewModel shared with Activity
val sharedViewModel: SharedViewModel by activityViewModels()

// With Hilt:
@AndroidEntryPoint
class MyFragment : Fragment() {
    @Inject lateinit var repository: Repository

    val viewModel: MyViewModel by viewModels()
}

// Manual factory:
val viewModel: MyViewModel by viewModels {
    MyViewModel.Factory(repository)
}
```

# viewModels(): Fragment-scoped
# activityViewModels(): Activity-scoped (shared)
# viewModels() with factory: custom creation
