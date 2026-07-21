---
title: "Fragment Transaction Error"
description: "Fix Android Fragment transaction errors and FragmentManager issues"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Fragment transactions fail because of FragmentManager state or configuration

## Common Causes

- Committing fragment transaction after onSaveInstanceState
- Fragment not added to container correctly
- Fragment tag not found when trying to findFragmentByTag
- Duplicate fragment added on configuration change

## Fixes

- Use commitAllowingStateLoss for late commits
- Use replace() with correct container ID
- Use unique tags for each fragment instance
- Check if fragment already exists before adding

## Code Example

```kotlin
// CORRECT fragment transaction
supportFragmentManager.commit {
    replace(R.id.fragment_container, MyFragment.newInstance())
    addToBackStack(null)
    setReorderingAllowed(true)
}

// Or with FragmentContainerView:
supportFragmentManager.commit {
    replace<MyFragment>(R.id.fragment_container)
    addToBackStack(null)
}

// Find existing fragment:
val fragment = supportFragmentManager.findFragmentByTag("my_tag")
```

# Use commitAllowingStateLoss() if needed
# addToBackStack() allows back navigation
# setReorderingAllowed(true) for animations
