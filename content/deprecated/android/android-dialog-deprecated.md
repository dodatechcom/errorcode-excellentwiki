---
title: "[Solution] Deprecated Function Migration: Dialog to DialogFragment"
description: "Migrate from deprecated Dialog to DialogFragment."
deprecated_function: "Dialog(context)"
replacement_function: "DialogFragment"
languages: ["android"]
deprecated_since: "AndroidX"
---

# [Solution] Deprecated Function Migration: Dialog to DialogFragment

The `Dialog(context)` has been deprecated in favor of `DialogFragment`.

## Migration Guide

DialogFragment is lifecycle-aware.

## Before (Deprecated)

```android
val dialog = Dialog(context)
dialog.setContentView(R.layout.my_dialog)
dialog.show()
```

## After (Modern)

```android
class MyDialogFragment : DialogFragment() {
    override fun onCreateDialog(savedInstanceState: Bundle?): Dialog {
        return AlertDialog.Builder(requireContext())
            .setTitle("Title")
            .setPositiveButton("OK") { _, _ -> }
            .create()
    }
}
```

## Key Differences

- DialogFragment is lifecycle-aware
