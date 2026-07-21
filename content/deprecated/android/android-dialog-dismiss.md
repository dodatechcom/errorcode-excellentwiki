---
title: "[Solution] Deprecated Function Migration: Dialog.dismiss to DialogFragment"
description: "Migrate from deprecated Dialog patterns to DialogFragment for proper lifecycle handling."
deprecated_function: "Dialog / AlertDialog direct"
replacement_function: "DialogFragment"
languages: ["kotlin"]
deprecated_since: "AndroidX"
---

# [Solution] Deprecated Function Migration: Dialog.dismiss to DialogFragment

The `Dialog / AlertDialog direct` has been deprecated in favor of `DialogFragment`.

## Migration Guide

DialogFragment handles configuration changes and lifecycle properly.

## Before (Deprecated)

```kotlin
val dialog = AlertDialog.Builder(context)
    .setTitle("Confirm")
    .setMessage("Are you sure?")
    .setPositiveButton("Yes") { _, _ -> confirm() }
    .setNegativeButton("No") { _, _ -> cancel() }
    .create()
dialog.show()
```

## After (Modern)

```kotlin
class ConfirmDialog : DialogFragment() {
    override fun onCreateDialog(savedInstanceState: Bundle?): Dialog {
        return AlertDialog.Builder(requireContext())
            .setTitle("Confirm")
            .setMessage("Are you sure?")
            .setPositiveButton("Yes") { _, _ -> confirm() }
            .setNegativeButton("No") { _, _ -> cancel() }
            .create()
    }
}

// Show
ConfirmDialog().show(supportFragmentManager, "confirm")
```

## Key Differences

- DialogFragment handles lifecycle
- Survives configuration changes
- Proper fragment transaction management
- show() with tag for identification
