---
title: "Bottom Sheet State Error"
description: "Fix Material BottomSheet behavior and state management errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
BottomSheet does not expand, collapse, or respond to gestures correctly

## Common Causes

- BottomSheetBehavior not set on CoordinatorLayout child
- Peek height not configured for collapsed state
- BottomSheetDialogFragment not showing full screen
- State callback not properly registered

## Fixes

- Set BottomSheetBehavior on CoordinatorLayout child view
- Configure peekHeight and state in XML or code
- Use BottomSheetDialogFragment for modal sheets
- Register BottomSheetCallback for state changes

## Code Example

```kotlin
// XML configuration
<com.google.android.material.bottomsheet.BottomSheetBehavior
    app:behavior_peekHeight="64dp"
    app:behavior_hideable="false"
    app:behavior_skipCollapsed="true" />

// Programmatic:
val bottomSheet = BottomSheetBehavior.from(view)
bottomSheet.state = BottomSheetBehavior.STATE_EXPANDED

// State callback:
bottomSheet.addBottomSheetCallback(object : BottomSheetCallback() {
    override fun onStateChanged(bottomSheet: View, newState: Int) {
        when (newState) {
            BottomSheetBehavior.STATE_EXPANDED -> { /* expanded */ }
            BottomSheetBehavior.STATE_COLLAPSED -> { /* collapsed */ }
        }
    }
    override fun onSlide(bottomSheet: View, slideOffset: Float) {}
})
```

# States: EXPANDED, COLLAPSED, HIDDEN, SETTLING, DRAGGING
# peekHeight: collapsed height
# hideable: allows swipe to dismiss
