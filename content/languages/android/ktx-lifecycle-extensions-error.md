---
title: "Lifecycle KTX Error"
description: "Fix AndroidX Lifecycle KTX extensions and lifecycleScope errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Lifecycle KTX extensions do not work correctly with coroutine scopes

## Common Causes

- lifecycleScope not available in Fragment
- repeatOnLifecycle not pausing collection
- viewLifecycleOwner not used for Fragment scope
- Coroutine launched in wrong lifecycle state

## Fixes

- Import lifecycle-runtime-ktx dependency
- Use repeatOnLifecycle(STARTED) for collection
- Use viewLifecycleOwner.lifecycleScope in Fragments
- Launch in correct lifecycle state

## Code Example

```kotlin
// Activity:
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.uiState.collect { updateUI(it) }
    }
}

// Fragment:
viewLifecycleOwner.lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.uiState.collect { updateUI(it) }
    }
}

// Dependencies:
implementation "androidx.lifecycle:lifecycle-runtime-ktx:2.7.0"
implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:2.7.0" 
```

# lifecycleScope: coroutine scope tied to lifecycle
# repeatOnLifecycle: collection pauses when not started
# Use viewLifecycleOwner in Fragments
