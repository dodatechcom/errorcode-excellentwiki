---
title: "Bottom Sheet Navigation Error"
description: "Fix Navigation component inside BottomSheetDialogFragment errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Navigation does not work inside BottomSheetDialogFragment or crashes

## Common Causes

- NavHostFragment not properly configured in BottomSheet
- NavController not finding correct graph
- Bottom sheet dismissing on navigation
- Fragment transactions failing in bottom sheet

## Fixes

- Use NavHostFragment inside BottomSheet layout
- Get NavController from child FragmentManager
- Configure bottom sheet to not dismiss on navigation
- Use findNavController() from child fragments

## Code Example

```kotlin
class MyBottomSheet : BottomSheetDialogFragment() {
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        return inflater.inflate(R.layout.bottom_sheet_with_nav, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val navHostFragment = childFragmentManager
            .findFragmentById(R.id.nav_host_fragment) as NavHostFragment
        val navController = navHostFragment.navController

        // Navigate within bottom sheet:
        navController.navigate(R.id.innerScreen)
    }
}
```

# Use childFragmentManager for NavHostFragment
# Set navGraph on NavHostFragment in XML
# Navigate with NavController from child
