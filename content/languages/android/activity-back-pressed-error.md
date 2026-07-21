---
title: "Back Pressed Handling Error"
description: "Fix Android back button handling errors and deprecated onBackPressed"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Back button does not behave as expected or uses deprecated API

## Common Causes

- onBackPressed() deprecated in API 33
- Back press not intercepted in Fragment
- Double back press to exit not working
- Back navigation stack incorrect

## Fixes

- Use OnBackPressedCallback for back press handling
- Register callback in onViewCreated for Fragments
- Use countdown timer for double-back-to-exit
- Manage back stack with Navigation component

## Code Example

```kotlin
// Modern back press handling (API 33+)
onBackPressedDispatcher.addCallback(this) {
    if (webView.canGoBack()) {
        webView.goBack()
    } else {
        isEnabled = false
        onBackPressedDispatcher.onBackPressed()
    }
}

// Fragment callback:
requireActivity().onBackPressedDispatcher.addCallback(viewLifecycleOwner) {
    // Handle back press
}
```

# Use OnBackPressedDispatcher
# Register in Activity or Fragment
# Disable callback when not needed
