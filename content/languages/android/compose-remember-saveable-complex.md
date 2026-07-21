---
title: "rememberSaveable Complex Type Error"
description: "Fix rememberSaveable complex type serialization errors in Jetpack Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
rememberSaveable does not persist complex objects across process death

## Common Causes

- Custom class not implementing Serializable
- rememberSaveable with non-primitive type
- MutableState not properly saved
- List or Map not surviving configuration change

## Fixes

- Implement Serializable or Parcelable on data class
- Use Saver for custom types
- Store primitives in rememberSaveable
- Use ViewModel for complex state

## Code Example

```kotlin
// Simple types work directly:
var text by rememberSaveable { mutableStateOf("") }

// For complex types, use Saver:
val nameSaver = Saver<Name, Bundle>(
    save = { bundleOf("first" to it.first, "last" to it.last) },
    restore = { Name(it.getString("first") ?: "", it.getString("last") ?: "") }
)
var name by rememberSaveable(stateSaver = nameSaver) {
    mutableStateOf(Name("John", "Doe"))
}

// Or use ViewModel for complex state:
val viewModel: MyViewModel = hViewModel()
val uiState by viewModel.uiState.collectAsStateWithLifecycle()
```

# rememberSaveable: primitives and serializable
# Saver: custom types with explicit save/restore
# ViewModel: complex state that survives everything
