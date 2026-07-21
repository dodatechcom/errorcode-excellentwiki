---
title: "DialogFragment Error"
description: "Fix DialogFragment lifecycle and display errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
DialogFragment crashes, does not show, or loses state on configuration change

## Common Causes

- DialogFragment not using newInstance pattern
- onCreateDialog vs onCreateView confusion
- Dialog not dismissed properly causing leak
- FragmentTransaction commit after onSaveInstanceState

## Fixes

- Use newInstance() with arguments for DialogFragment
- Use onCreateDialog for AlertDialog, onCreateView for custom
- Dismiss dialog in onDestroyView
- Use showAllowingStateLoss for late commits

## Code Example

```kotlin
class MyDialogFragment : DialogFragment() {
    companion object {
        fun newInstance(title: String): MyDialogFragment {
            return MyDialogFragment().apply {
                arguments = bundleOf("title" to title)
            }
        }
    }

    override fun onCreateDialog(savedInstanceState: Bundle?): Dialog {
        val title = arguments?.getString("title") ?: "Title"
        return AlertDialog.Builder(requireContext())
            .setTitle(title)
            .setMessage("Message content")
            .setPositiveButton("OK") { _, _ -> dismiss() }
            .setNegativeButton("Cancel") { _, _ -> dismiss() }
            .create()
    }
}

// Show dialog:
MyDialogFragment.newInstance("Confirm").show(supportFragmentManager, "dialog")
```

# newInstance() pattern for arguments
# onCreateDialog: AlertDialog builder
# onCreateView: custom dialog layout
# showAllowingStateLoss: safe late commit
