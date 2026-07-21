---
title: "Snackbar Error"
description: "Fix Snackbar display and action configuration errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Snackbar does not appear or is hidden behind other UI elements

## Common Causes

- Snackbar attached to wrong view hierarchy
- Snackbar duration too short to read
- Snackbar action callback not implemented
- Snackbar obscured by bottom navigation or FAB

## Fixes

- Use coordinatorLayout as Snackbar parent view
- Use LENGTH_LONG or custom duration
- SetAction callback for snackbar actions
- Use coordinatorLayout to auto-adjust for FAB

## Code Example

```kotlin
// CORRECT: use CoordinatorLayout as parent
val snackbar = Snackbar.make(
    coordinatorLayout,
    "Item deleted",
    Snackbar.LENGTH_LONG
)
snackbar.setAction("Undo") {
    viewModel.undoDelete()
}
snackbar.show()

// Wrong: using Activity as parent
// Snackbar.make(activityView, "msg", duration)  // May be hidden
```

# Always use CoordinatorLayout as parent
# LENGTH_SHORT: 2 seconds
# LENGTH_LONG: 3.5 seconds
# LENGTH_INDEFINITE: until dismissed
