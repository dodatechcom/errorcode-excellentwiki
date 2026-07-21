---
title: "ViewModel Factory Error"
description: "Fix ViewModel factory and assisted injection errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
ViewModel cannot be instantiated because factory is not provided or misconfigured

## Common Causes

- ViewModel constructor has parameters without factory
- Hilt @HiltViewModel not properly configured
- Custom factory not returning correct ViewModel
- Factory parameter mismatch with ViewModel constructor

## Fixes

- Use @HiltViewModel with @Inject constructor
- Create custom ViewModelProvider.Factory
- Pass parameters through SavedStateHandle
- Use by viewModels() delegate with factory

## Code Example

```kotlin
// With Hilt:
@HiltViewModel
class MyViewModel @Inject constructor(
    private val repository: Repository,
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {
    // No factory needed - Hilt provides it
}

// Without Hilt:
class MyViewModel(private val repo: Repository) : ViewModel() {
    class Factory(private val repo: Repository) : ViewModelProvider.Factory {
        override fun <T : ViewModel> create(modelClass: Class<T>): T {
            return MyViewModel(repo) as T
        }
    }
}

// Usage:
val viewModel: MyViewModel by viewModels {
    MyViewModel.Factory(repository)
}
```

# @HiltViewModel handles factory automatically
# Use SavedStateHandle for state that survives process death
# Use viewModels() delegate for ViewModel access
