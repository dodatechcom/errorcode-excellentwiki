---
title: "ChipGroup Selection Error"
description: "Fix Material ChipGroup selection and layout errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
ChipGroup does not handle single or multi-selection correctly

## Common Causes

- Selection mode not configured (single vs multi)
- Checked change listener not firing
- Chip not properly styled as selectable
- Selection state not restored on configuration change

## Fixes

- Set selectionRequired and singleSelection attributes
- Set onCheckedStateChangeListener on ChipGroup
- Use @style/Widget.Material3.Chip.Filter or .Choice
- Save selection state in ViewModel

## Code Example

```kotlin
<!-- Single selection -->
<com.google.android.material.chip.ChipGroup
    android:id="@+id/chipGroup"
    app:singleSelection="true"
    app:selectionRequired="true">

    <com.google.android.material.chip.Chip
        android:id="@+id/chip1"
        style="@style/Widget.Material3.Chip.Filter"
        android:text="Option 1" />

    <com.google.android.material.chip.Chip
        android:id="@+id/chip2"
        style="@style/Widget.Material3.Chip.Filter"
        android:text="Option 2" />
</com.google.android.material.chip.ChipGroup>

// In code:
chipGroup.setOnCheckedStateChangeListener { group, checkedIds ->
    // Handle selection
}
```

# singleSelection: only one chip selected
# Filter chips: toggling selection
# Choice chips: single selection
# Input chips: editable
