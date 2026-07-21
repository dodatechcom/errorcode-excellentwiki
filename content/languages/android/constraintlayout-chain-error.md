---
title: "ConstraintLayout Chain Error"
description: "Fix ConstraintLayout chain configuration errors for distributed layouts"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
ConstraintLayout chain does not distribute views as expected

## Common Causes

- Chain style not set (spread, packed, spreadInside)
- Guideline percentage not correctly configured
- Views not properly constrained in chain
- Chain head element not first in XML

## Fixes

- Set app:layout_constraintVertical_chainStyle or horizontal
- Use guidelines with app:layout_constraintGuide_percent
- Ensure all views in chain have both top/bottom constraints
- First view in XML is the chain head

## Code Example

```kotlin
<androidx.constraintlayout.widget.ConstraintLayout
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <!-- Vertical chain with packed style -->
    <TextView
        android:id="@+id/title"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintBottom_toTopOf="@+id/subtitle"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintVertical_chainStyle="packed" />

    <TextView
        android:id="@+id/subtitle"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        app:layout_constraintTop_toBottomOf="@+id/title"
        app:layout_constraintBottom_toBottomOf="parent" />
</androidx.constraintlayout.widget.ConstraintLayout>
```

# Chain styles:
# spread: equal spacing
# spreadInside: spacing at edges
# packed: centered together
